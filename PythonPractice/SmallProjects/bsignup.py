import json
import passwordmodule as pm
import random as rd
import hashlib
import os
from pathlib import Path


class Signup:

    CREDENTIALS_FILE = "credentials.json"  # Centralized file path

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = self._generate_id()

    def _generate_id(self):
        """Generate unique ID once during initialization"""
        id_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&'
        return ''.join(rd.choices(id_chars, k=10))

    def is_valid_email(self):
        """Improved email validation"""
        if '@' not in self.email:
            return False
        local, domain = self.email.rsplit('@', 1)
        if not local or not domain or '.' not in domain:
            return False
        return True

    def is_valid_password(self):
        """Password validation using passwordmodule"""
        return pm.final_count(self.password)

    def email_exists(self):
        """Check if email is already registered"""
        try:
            if not os.path.exists(self.CREDENTIALS_FILE):
                return False
            with open(self.CREDENTIALS_FILE, 'r') as file:
                for line in file:
                    if line.strip():
                        user = json.loads(line)
                        if user['email'] == self.email:
                            return True
            return False
        except Exception as e:
            print(f"Error checking email: {e}")
            return False

    def _hash_password(self):
        """Hash password using SHA-256 for security"""
        return hashlib.sha256(self.password.encode()).hexdigest()

    def gen_json(self):
        """Generate user data dictionary with hashed password"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email,
            # Store hashed password
            'password': self._hash_password()
        }

    def file_open_write(self):
        """Save user credentials to JSON file with error handling"""
        try:
            # Check if email already exists
            if self.email_exists():
                print("Error: Email already registered!")
                return False

            # Validate inputs
            if not self.is_valid_email():
                print("Error: Invalid email format!")
                return False

            if not self.is_valid_password():
                print("Error: Password doesn't meet requirements!")
                return False

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(self.CREDENTIALS_FILE)
                        or '.', exist_ok=True)

            # Write to file
            with open(self.CREDENTIALS_FILE, 'a') as file:
                json.dump(self.gen_json(), file)
                file.write('\n')

            print("Signup successful!")
            return True

        except IOError as e:
            print(f"Error writing to file: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during signup: {e}")
            return False


class Login:
    
    CREDENTIALS_FILE = "credentials.json"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.user_data = None

    def _hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def find_user(self):
        """Search for user by email in credentials file"""
        try:
            if not os.path.exists(self.CREDENTIALS_FILE):
                return None
            with open(self.CREDENTIALS_FILE, 'r') as file:
                for line in file:
                    if line.strip():
                        user = json.loads(line)
                        if user['email'] == self.email:
                            return user
            return None
        
        except Exception as e:
            print(f"Error finding user: {e}")
            return None

    def verify_password(self, stored_hash):
        """Verify if input password matches stored hash"""
        input_hash = self._hash_password(self.password)
        return input_hash == stored_hash

    def login(self):
        """Authenticate user with email and password"""
        try:
            # Find user in credentials file
            user = self.find_user()
            
            if not user:
                print("Error: Email not found!")
                return False
            
            # Verify password
            if self.verify_password(user['password']):
                self.user_data = user
                print(f"Login successful! Welcome {user['name']}!")
                return True
            else:
                print("Error: Incorrect password!")
                return False
        
        except Exception as e:
            print(f"Unexpected error during login: {e}")
            return False


print(" ---------- Welcome ----------\n ------ Bus Ticket System -----\n 1. Login \n 2. Signup")
user_ln = int(input("Choice: "))
