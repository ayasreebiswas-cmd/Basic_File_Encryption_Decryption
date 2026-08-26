import os
from cryptography.fernet import Fernet
import streamlit as st

# --- Core Cryptography Helpers ---


def generate_or_load_key() -> bytes:
    """Generates a new Fernet key or fetches it from state."""
    if "secret_key" not in st.session_state:
        st.session_state["secret_key"] = Fernet.generate_key()
    return st.session_state["secret_key"]


def encrypt_data(file_bytes: bytes, key: bytes) -> bytes:
    """Encrypts raw byte data using Fernet symmetric encryption."""
    cipher = Fernet(key)
    return cipher.encrypt(file_bytes)


def decrypt_data(file_bytes: bytes, key: bytes) -> bytes:
    """Decrypts Fernet-encrypted byte data back to original form."""
    cipher = Fernet(key)
    return cipher.decrypt(file_bytes)


# --- Dashboard Configuration ---

st.set_page_config(
    page_title="Secure File Vault", page_icon="🔒", layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
        .stApp { max-width: 800px; margin: 0 auto; }
        .success-box { padding: 10px; background-color: #d4edda; border-radius: 5px; color: #155724; }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🔒 CipherVault")
st.caption("Symmetric File Encryption & Decryption Utility")

# --- Application Logic ---

secret_key = generate_or_load_key()

# Sidebar Setup
with st.sidebar:
    st.header("⚙️ Security Dashboard")
    st.subheader("Encryption Key")
    st.code(secret_key.decode(), language="text")

    if st.button("Generate New Key", help="Warning: invalidates previous key"):
        st.session_state["secret_key"] = Fernet.generate_key()
        st.rerun()

    st.markdown("---")
    st.markdown(
        "**Algorithm:** Fernet (AES-128-CBC + HMAC-SHA256)\n\n"
        "**Note:** Keep your key safe. Without the matching key, decryption is impossible."
    )

# Main UI Tabs
tab_encrypt, tab_decrypt = st.tabs(["🔒 Encrypt File", "🔓 Decrypt File"])

with tab_encrypt:
    st.subheader("Encrypt a File")
    uploaded_file = st.file_uploader(
        "Choose a text file to encrypt", type=["txt", "csv", "log", "json"]
    )

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()

        if st.button("Encrypt Content", type="primary"):
            try:
                encrypted_content = encrypt_data(file_bytes, secret_key)
                output_filename = f"encrypted_{uploaded_file.name}"

                st.success("File encrypted successfully!")
                st.download_button(
                    label="⬇️ Download Encrypted File",
                    data=encrypted_content,
                    file_name=output_filename,
                    mime="application/octet-stream",
                )
            except Exception as e:
                st.error(f"Encryption failed: {str(e)}")

with tab_decrypt:
    st.subheader("Decrypt a File")
    encrypted_file = st.file_uploader(
        "Upload an encrypted file", type=None, key="dec_upload"
    )

    if encrypted_file is not None:
        enc_bytes = encrypted_file.read()

        if st.button("Decrypt Content"):
            try:
                decrypted_content = decrypt_data(enc_bytes, secret_key)
                original_filename = encrypted_file.name.replace(
                    "encrypted_", "decrypted_"
                )

                st.success("File decrypted successfully!")
                st.download_button(
                    label="⬇️ Download Decrypted File",
                    data=decrypted_content,
                    file_name=original_filename,
                    mime="text/plain",
                )
            except Exception:
                st.error(
                    "Decryption failed! The file may be corrupt or encrypted with a different key."
                )