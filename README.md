# Basic_File_Encryption_Decryption

A Streamlit-based web application for **secure symmetric file encryption and decryption** named **CipherVault**. The application allows users to encrypt raw file contents and decrypt them back to their original form using Fernet symmetric cryptography.

## Features

* 🔒 Symmetric file encryption using Fernet cryptography


* 🔓 File decryption back to original form


* 🔑 Session-based secret key generation and management


* 🔄 One-click key regeneration capability


* 📂 Support for text-based file formats (`.txt`, `.csv`, `.log`, `.json`)


* ⬇️ Automated file renaming and downloading for encrypted and decrypted files


* 🌐 Streamlit-based responsive web interface


* 🎨 Custom CSS styling for interactive layout



## Technologies Used

* **Python**
* **Streamlit**
* **cryptography (Fernet)**

* **CSS**

* **Git & GitHub**

## Project Structure

```text
Basic_File_Encryption_Decryption/
│
├── app.py
├── README.md
├── requirements.txt
│
└── venv/

```

> **Note:** `venv/` should not be uploaded to GitHub.

## How It Works

The application follows these basic steps:

1. The user launches the Streamlit web application.
2. A random Fernet secret key is generated and stored in the session state.


3. The user selects either the **Encrypt File** or **Decrypt File** tab.


4. To encrypt:
* The user uploads a valid file (`.txt`, `.csv`, `.log`, `.json`).


* The file is converted into bytes and encrypted using Fernet cryptography.


* The encrypted output file is downloaded with an `encrypted_` prefix.




5. To decrypt:
* The user uploads an encrypted file.


* The application attempts decryption using the active session key.


* The restored original content is downloaded with a `decrypted_` prefix.





## Cryptographic Architecture

The application implements Fernet symmetric encryption, which includes:

* **AES-128 in CBC mode** for encryption


* **HMAC-SHA256** for message authentication and integrity verification


* **PKCS7 Padding** for standardized block formatting

### Security Considerations

* Encrypted files can **only** be decrypted using the exact key active during encryption.


* Regenerating the secret key invalidates previous keys, making previously encrypted files unrecoverable unless the matching key is preserved.



## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Basic_File_Encryption_Decryption.git

```

### 2. Open the Project

```bash
cd Basic_File_Encryption_Decryption

```

### 3. Create a Virtual Environment

On Windows:

```cmd
python -m venv venv

```

### 4. Activate the Virtual Environment

```cmd
venv\Scripts\activate

```

### 5. Install Dependencies

```cmd
pip install streamlit cryptography

```

Then generate the requirements file:

```cmd
pip freeze > requirements.txt

```

## Running the Application

Activate the virtual environment:

```cmd
venv\Scripts\activate

```

Run the Streamlit app:

```cmd
python -m streamlit run app.py

```

> Alternatively, run `streamlit run app.py` if Streamlit is registered in your PATH.

The application will run locally and automatically open in your web browser:

```text
http://localhost:8501

```

## Usage Example

### Encryption Process

1. Navigate to the **Encrypt File** tab.


2. Upload a file (e.g., `data.txt`).


3. Click **Encrypt Content**.


4. Download the resulting encrypted file (`encrypted_data.txt`).



### Decryption Process

1. Navigate to the **Decrypt File** tab.


2. Upload `encrypted_data.txt`.


3. Click **Decrypt Content**.


4. Download the restored file (`decrypted_data.txt`).



## GitHub Workflow

After making changes to the project:

```cmd
git status
git add .
git commit -m "Update project files"
git push

```

Ensure temporary files or virtual environments are excluded via `.gitignore`.

## Future Improvements

* User key input/passphrase derivation using PBKDF2
* Support for arbitrary file types (PDF, images, archives)
* Key exporting and manual key loading features
* User authentication and cloud file storage support
* File hashing (SHA-256) display before and after processing

## Author

ayasree biswas

## License

This project is intended for educational and project-development purposes.
