## Vulnerability Description
Cryptographic failure occurs when applications encrypts sensitive user data before storing it in a database. However, the encryption key is hardcoded in the source code, which allows an attacker to decrypt all stored data offline.

## 1. Vulnerable implementation
1. Hardcoded encryption key in encrypting file
```python
KEY = b'randomestKey1234'
```
This is used for AES encryption
### 2. Encryption Process
- AES-128 in CBC mode
- Random IV generated per encryption
- Encrypted data stored in SQLite database

	Although encryption is applied correctly, the key is stored in the source code, which makes the protection ineffective.

## 3. Workflow
1. Register a user
	 -  `POST /register`
	-   secret is encrypted before getting into the database
	 -  Body:
```json
{
	"username": "randomUser",
	"secret": "randomSecret"
}
```
2. View a profile 
	 - `GET /profile/<id>`
	 - The encrypted secret is retrieved from the database and decrypted using the hardcoded key.

## 3.  Exploit scenerio
1. Attacker gains access to a source code, which reveals the hardcoded key  
2. Then the threat actor gets the copy of the database
3. He decrypts the encrypted data in it with the key

## 4. Impact
- Complete loss of confidentiality
- Exposure of sensitive user data
- Potential identity theft or financial fraud
We have to remember that the key is meaningless, if its accessible to the attacker
## 5. Root cause
- Hardcoded encryption key in source code
- Lack of secure key storage
- No key rotation mechanism
- No separation between code and secret material
## 6. Mitigation
- Use environment variables instead
- Secure secret management system
- Key rotation

