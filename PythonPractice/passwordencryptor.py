"""
Triple Encryption Password Manager
Encrypts passwords 3 times using different algorithms before storing
"""

import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
from cryptography.hazmat.backends import default_backend
import getpass

class TripleEncryptionPasswordManager:
    def __init__(self, master_password):
        """Initialize with a master password"""
        self.master_password = master_password
        self.password_file = "encrypted_passwords.json"
        self.key_file = "encryption_keys.key"
        
        # Generate 3 different encryption keys from master password
        self.key1 = self._derive_key(master_password, b"salt1_unique")
        self.key2 = self._derive_key(master_password, b"salt2_unique")
        self.key3 = self._derive_key(master_password, b"salt3_unique")
        
        self.cipher1 = Fernet(self.key1)
        self.cipher2 = Fernet(self.key2)
        self.cipher3 = Fernet(self.key3)
    
    def _derive_key(self, password, salt):
        """Derive encryption key from password using PBKDF2"""
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    
    def encrypt_password(self, password):
        """Encrypt password 3 times with different keys"""
        # First encryption
        encrypted1 = self.cipher1.encrypt(password.encode())
        print("✓ First encryption complete")
        
        # Second encryption
        encrypted2 = self.cipher2.encrypt(encrypted1)
        print("✓ Second encryption complete")
        
        # Third encryption
        encrypted3 = self.cipher3.encrypt(encrypted2)
        print("✓ Third encryption complete")
        
        # Convert to base64 for safe storage
        final_encrypted = base64.b64encode(encrypted3).decode()
        return final_encrypted
    
    def decrypt_password(self, encrypted_password):
        """Decrypt password (reverse 3 layers of encryption)"""
        try:
            # Decode from base64
            encrypted3 = base64.b64decode(encrypted_password.encode())
            
            # First decryption (reverse of third encryption)
            decrypted1 = self.cipher3.decrypt(encrypted3)
            print("✓ First decryption layer complete")
            
            # Second decryption (reverse of second encryption)
            decrypted2 = self.cipher2.decrypt(decrypted1)
            print("✓ Second decryption layer complete")
            
            # Third decryption (reverse of first encryption)
            original_password = self.cipher1.decrypt(decrypted2).decode()
            print("✓ Third decryption layer complete")
            
            return original_password
        except Exception as e:
            print(f"❌ Decryption failed: {e}")
            return None
    
    def save_password(self, service_name, username, password):
        """Save encrypted password to file"""
        # Load existing passwords
        passwords = self._load_passwords()
        
        # Encrypt the password
        print(f"\n🔒 Encrypting password for {service_name}...")
        encrypted_pwd = self.encrypt_password(password)
        
        # Store with service name and username
        passwords[service_name] = {
            "username": username,
            "password": encrypted_pwd
        }
        
        # Save to file
        with open(self.password_file, 'w') as f:
            json.dump(passwords, f, indent=4)
        
        print(f"✅ Password saved successfully for {service_name}!\n")
    
    def get_password(self, service_name):
        """Retrieve and decrypt password"""
        passwords = self._load_passwords()
        
        if service_name not in passwords:
            print(f"❌ No password found for {service_name}")
            return None
        
        entry = passwords[service_name]
        print(f"\n🔓 Decrypting password for {service_name}...")
        
        decrypted_pwd = self.decrypt_password(entry["password"])
        
        if decrypted_pwd:
            print(f"✅ Password retrieved successfully!\n")
            return {
                "username": entry["username"],
                "password": decrypted_pwd
            }
        return None
    
    def list_services(self):
        """List all stored services"""
        passwords = self._load_passwords()
        if not passwords:
            print("📂 No passwords stored yet.")
            return []
        
        print("\n📂 Stored Services:")
        print("-" * 40)
        for service, data in passwords.items():
            print(f"  • {service} (username: {data['username']})")
        print("-" * 40)
        return list(passwords.keys())
    
    def delete_password(self, service_name):
        """Delete a stored password"""
        passwords = self._load_passwords()
        
        if service_name in passwords:
            del passwords[service_name]
            with open(self.password_file, 'w') as f:
                json.dump(passwords, f, indent=4)
            print(f"✅ Password for {service_name} deleted successfully!")
        else:
            print(f"❌ No password found for {service_name}")
    
    def _load_passwords(self):
        """Load passwords from file"""
        if os.path.exists(self.password_file):
            with open(self.password_file, 'r') as f:
                return json.load(f)
        return {}


def main():
    """Main program interface"""
    print("=" * 50)
    print("🔐 TRIPLE ENCRYPTION PASSWORD MANAGER 🔐")
    print("=" * 50)
    
    # Get master password
    master_password = getpass.getpass("\n🔑 Enter your MASTER PASSWORD: ")
    
    if not master_password:
        print("❌ Master password cannot be empty!")
        return
    
    # Initialize password manager
    pm = TripleEncryptionPasswordManager(master_password)
    
    while True:
        print("\n" + "=" * 50)
        print("MENU:")
        print("1. 💾 Save a new password")
        print("2. 🔍 Retrieve a password")
        print("3. 📋 List all services")
        print("4. 🗑️  Delete a password")
        print("5. 🚪 Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            service = input("\n📝 Enter service name (e.g., Gmail, Facebook): ").strip()
            username = input("👤 Enter username/email: ").strip()
            password = getpass.getpass("🔒 Enter password to encrypt: ")
            
            if service and username and password:
                pm.save_password(service, username, password)
            else:
                print("❌ All fields are required!")
        
        elif choice == '2':
            service = input("\n🔍 Enter service name to retrieve: ").strip()
            result = pm.get_password(service)
            
            if result:
                print(f"Username: {result['username']}")
                print(f"Password: {result['password']}")
        
        elif choice == '3':
            pm.list_services()
        
        elif choice == '4':
            service = input("\n🗑️  Enter service name to delete: ").strip()
            pm.delete_password(service)
        
        elif choice == '5':
            print("\n👋 Goodbye! Your passwords are safely encrypted.\n")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()