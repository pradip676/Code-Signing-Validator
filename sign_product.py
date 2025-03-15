from Crypto.PublicKey import ECC 
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

with open ("privateKey.pem", "rt") as f:
    private_key = ECC.import_key(f.read())

with open ("product.py", "rb") as f:
    product = f.read()

product_hash = SHA256.new(product)
sign_obj = DSS.new(private_key, 'fips-186-3')
signature = sign_obj.sign(product_hash)

with open ("product.sig", "wb") as f:
    f.write(signature)

