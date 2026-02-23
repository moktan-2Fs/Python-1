import json
import hashlib
import os
import random as rd
import time as t


class Users:
    identity = 'User'

    def __init__(self, name, email, id, **kwargs):
        super().__init__(id, **kwargs)
        self.name = name
        self.email = email
        self.id = id

    def view_items(self):
        li = ['apple', 'mango', 'orange', 'banana', 'kiwi']
        print(li.index('kiwi'))
        return li

    def search_items(self):
        ser = input('Search: ')
        print(f"Searching for {ser}.....")
        t.sleep(3)
        for _ in self.view_items():
            if _ == ser:
                print(f'{ser} found....')
            continue


# ob = Users('sagar', "sgar@gs", 'SFS24')
# print(ob.view_items())
# ob.search_items()

class Signup(Users):
    identity = "Signup"

    CREDENTIALS_FILE = "credentials.json"  # Centralized file path

    def __init__(self, name, email, password, **kwargs):
        super().__init__(name=name, email=email, **kwargs)
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
            if self.email_exists():
                print("Error: Email already registered!")
                return False

            if not self.is_valid_email():
                print("Error: Invalid email format!")
                return False

            os.makedirs(os.path.dirname(self.CREDENTIALS_FILE)
                        or '.', exist_ok=True)

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


class Login(Signup):
    identity = "Login"
    CREDENTIALS_FILE = "credentials.json"

    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password
        super().__init__(email=email, passowrd=password, **kwargs)
        self.user_data = None

    def _hash_password(self, password):
        return super(Login, self)._hash_password(password)

    def find_user(self):
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
        input_hash = self._hash_password(self.password)
        return input_hash == stored_hash

    def login(self):
        try:
            user = self.find_user()

            if not user:
                print("Error: Email not found!")
                return False

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


class Customer(Login, Signup, Users):
    identity = 'Customer'

    def __init__(self, name, email, id, password):
        super().__init__(name=name, email=email, id=id, password=password)
        self.password = password

    def login(self):
        pass


class Admin(Signup, Users):
    identity = "Admin"
    pass


print(Customer.__mro__)
