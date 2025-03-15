from Crypto.PublicKey import ECC 
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import subprocess

def validate_product():
    try:
        with open ("publicKey.pem", "rt") as f:
            pub_key = f.read()
        print("Verified public key of the Vendor:")
        print(pub_key)

        public_key = ECC.import_key(pub_key)

        with open ("product.py", "rb") as f:
            product = f.read()

        with open ("product.sig", "rb") as f:
            signature = f.read()

        product_hash = SHA256.new(product)
        validator = DSS.new(public_key, 'fips-186-3')
        validator.verify(product_hash, signature)
        
        print("\nCode certificate valid: execution allowed")
        subprocess.run(["python", "product.py"]) 

    except ValueError:
        print("\nCode certificate invalid: execution denied")

    except FileNotFoundError as e:
        print(f"\nMissing File: {str(e)}")

def main():
    validate_product()

if __name__ == "__main__":
    main()