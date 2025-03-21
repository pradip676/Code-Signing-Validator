#This program generate the key pairs used to sign and validate the software

from Crypto.PublicKey import ECC 

#Generate ECDSA key pairs and save to the file 
private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

#Save the secret key to privateKey.pem
with open("privateKey.pem", "wt") as f:
    f.write(private_key.export_key(format='PEM'))

#Save the public key to publicKey.pem
with open ("publicKey.pem", "wt") as f:
    f.write(public_key.export_key(format='PEM'))  