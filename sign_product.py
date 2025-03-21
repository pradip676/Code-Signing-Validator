#This program signs the product file to create the certificate

from Crypto.PublicKey import ECC 
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

#Get the secret key of the vendor
with open ("privateKey.pem", "rt") as f:
    private_key = ECC.import_key(f.read())

#Read the executing product code
with open ("product.py", "rb") as f:
    product = f.read()

product_hash = SHA256.new(product)  #SHA256 hash of the product
sign_obj = DSS.new(private_key, 'fips-186-3') #Digital signature using ECDSA
signature = sign_obj.sign(product_hash) #Signing the hash 

#Save the signature to product.sig 
with open ("product.sig", "wb") as f:
    f.write(signature)

