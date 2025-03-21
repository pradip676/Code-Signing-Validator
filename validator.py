#This program validates the product using publicly known key

from Crypto.PublicKey import ECC 
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import subprocess
import sys

def validate_product():
    try:
        # Display the public key to the screen
        with open ("publicKey.pem", "rt") as f:
            pub_key = f.read()
        print(f"Verified public key of the Vendor:\n{'-'*40}\n{pub_key}\n{'-'*40}")   

        # Get the public key to validate
        public_key = ECC.import_key(pub_key)

        # Get the product to be verified
        with open ("product.py", "rb") as f:
            product = f.read()

        # Get the certificate
        with open ("product.sig", "rb") as f:
            signature = f.read()

        # Make the product hash,create the verifier with public key and 
        # check if signature matches the hash
        product_hash = SHA256.new(product)
        validator = DSS.new(public_key, 'fips-186-3')
        validator.verify(product_hash, signature)
        
        # Output for successful verification
        print("\nCode certificate valid: execution allowed")
        print("\nExecuting product:")
        subprocess.run([sys.executable, "product.py"])  # Execute product

    # Handle the invalid signature
    except ValueError:
        print("\nCode certificate invalid: execution denied")

    # Handle missing files
    except FileNotFoundError as e:
        print(f"\nMissing File: {str(e)}")

def main():
    validate_product()

if __name__ == "__main__":
    main()