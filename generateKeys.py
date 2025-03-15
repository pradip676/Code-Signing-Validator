from Crypto.PublicKey import ECC 

#ECDSA Key Pair 
private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

with open("privateKey.pem", "wt") as f:
    f.write(private_key.export_key(format='PEM'))

with open ("publicKey.pem", "wt") as f:
    f.write(public_key.export_key(format='PEM'))  