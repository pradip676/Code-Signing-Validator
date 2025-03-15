from Crypto.PublicKey import ECC 
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import subprocess

def validate_product():
    try:
        with open ("publicKey.pem", "rt") as f:
            public_key = ECC.import_key(f.read())

        with open ("product.py", "rb") as f:
            product = f.read()

        with open ("product.sig", "rb") as f:
            signature = f.read()

        product_hash = SHA256.new(product)
        validator = DSS.new(public_key, 'fips-186-3')
        validator.verify(product_hash, signature)
        
        print("Code certificate valid: execution allowed")
        subprocess.run(["python", "product.py"]) 

    except ValueError:
        print("Code certificate invalid: execution denied")

    except FileNotFoundError as e:
        print(f"Code certificate invalid: execution denied - {str(e)}")

def main():
    validate_product()

if __name__ == "__main__":
    main()