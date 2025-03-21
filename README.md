# Code Signing Validator - ECDSA Implementation

## Project Overview

This project implements **code signing** using the **Elliptic Curve Digital Signature Algorithm (ECDSA)** to ensure the authenticity and integrity of software. The purpose is to prevent unauthorized modifications by verifying a **digital signature** before executing a program.

The project follows a structured cryptographic approach:

1. **Key Generation** – Creating public/private key pairs.
2. **Signing Process** – Digitally signing the software using the private key.
3. **Validation** – Checking the signature before execution to detect tampering.

## Group Members

- **Niall Chiweshe (11850393)**
- **Bishesh Dulal (11821780)**
- **Pradip Sapkota (11821781)**

## Environment Setup

### **System Requirements**

- **Python Version:** Python 3.8 or newer
- **Supported Operating Systems:** Windows, macOS, Linux
- **Required Libraries:** Install dependencies using:
  ```sh
  pip install pycryptodome
  ```
  or 
  ```sh
  pip3 install pycryptodome
  ```

## Project Structure

```
 Code-Signing-Validator/
 ├── generateKeys.py    # Generates ECDSA key pair (private & public keys)
 ├── sign_product.py    # Signs the product.py file using the private key
 ├── validator.py       # Verifies signature & executes product.py if valid
 ├── product.py         # The software being signed & validated
 ├── privateKey.pem    # Private key (kept secret)
 ├── publicKey.pem     # Public key (for validation)
 ├── product.sig       # Digital signature of product.py
 ├── README.md         # Documentation & usage guide
```

## Step-by-Step Instructions to Duplicate This Environment

### **1️⃣ Install Python**
Ensure you have **Python 3.8 or later** installed.  
Check your version by running:
```sh
python --version  # For Windows/macOS/Linux
```

### **2️⃣ Install Required Libraries**
Install the cryptographic library:
```sh
pip install pycryptodome
```
```sh
pip3 install pycryptodome
```

### **3️⃣ Download the Project Files**
Clone the GitHub repository and navigate into the project folder:
```sh
git clone https://github.com/pradip676/Code-Signing-Validator.git
cd Code-Signing-Validator
```

### **4️⃣ Generate the ECDSA Key Pair**
Run `generateKeys.py` to get key pairs as `privateKey.pem` and `publicKey.pem`:
```sh
python generateKeys.py
```

### **5️⃣ Sign the Product**
Sign `product.py` to generate a valid signature:
```sh
python sign_product.py
```

### **6️⃣ Verify and Execute**
Validate the signature and execute the program:
```sh
python validator.py
```

### **7️⃣ Test for Tampering**
Modify `product.py`, then try running `validator.py` again:
```sh
python validator.py
```
- **Sample output for original product**:
```sh
  Verified public key of the Vendor:
----------------------------------------
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAENXbK1o6ubAQ3kYr+0olZoRnQA+9z
1kgTuge4V6xNibTvKoGGeamXkp9FqLogmuOVtgnNYZ0r9YFKsyUi0q8JQg==
-----END PUBLIC KEY-----
----------------------------------------

Code certificate valid: execution allowed

Executing product...
I am a software made by 11850393
```
- **Sample output for modified product**:
  ```sh
  Verified public key of the Vendor:
----------------------------------------
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAENXbK1o6ubAQ3kYr+0olZoRnQA+9z
1kgTuge4V6xNibTvKoGGeamXkp9FqLogmuOVtgnNYZ0r9YFKsyUi0q8JQg==
-----END PUBLIC KEY-----
----------------------------------------

Code certificate invalid: execution denied
  ```

## References

- **Boneh, D. & Shoup, V.** - *A Graduate Course in Applied Cryptography* (2020).
- **NIST Report (2018)** - *Security Considerations for Code Signing*.
- **Kim et al. (2021)** - *Mitigating Software Supply Chain Attacks with Code Signing*.
- **Singh & Gupta (2019)** - *Comparative Analysis of Digital Signature Algorithms*.

## GitHub Repository

🔗 **[Code-Signing Validator](https://github.com/pradip676/Code-Signing-Validator)**

