import hashlib
import sys
import platform

def get_password_with_asterisks(prompt="Enter your password: "):
    """
    Gets password input with asterisks displayed for each character.
    Works on both Windows and Unix-like systems.
    """
    print(prompt, end='', flush=True)
    password = ""
    
    if platform.system() == "Windows":
        import msvcrt
        while True:
            char = msvcrt.getch()
            if char in (b'\r', b'\n'):  # Enter key
                print()
                break
            elif char == b'\x08':  # Backspace
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                password += char.decode('utf-8')
                sys.stdout.write('*')
                sys.stdout.flush()
    else:  # Linux/Mac
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                char = sys.stdin.read(1)
                if char in ('\r', '\n'):  # Enter key
                    print()
                    break
                elif char == '\x7f':  # Backspace
                    if len(password) > 0:
                        password = password[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                elif char == '\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                else:
                    password += char
                    sys.stdout.write('*')
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return password

def encrypt_password(password):
    """
    Encrypts a password using SHA-256 hashing algorithm.
    Returns the encrypted (hashed) password as a hexadecimal string.
    """
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    
    # Create SHA-256 hash object
    hash_object = hashlib.sha256(password_bytes)
    
    # Get the hexadecimal representation of the hash
    encrypted_password = hash_object.hexdigest()
    
    return encrypted_password

def main():
    print("=" * 50)
    print("Password Encryption Program")
    print("=" * 50)
    
    # Get password from user (with asterisks)
    password = get_password_with_asterisks("Enter your password: ")
    
    # Encrypt the password
    encrypted = encrypt_password(password)
    
    # Display results
    print("\n" + "=" * 50)
    print("Results:")
    print("=" * 50)
    print(f"Original Password: {password}")
    print(f"Encrypted Password: {encrypted}")
    print("=" * 50)
    
    print("\nNote: This uses SHA-256 hashing, which is one-way encryption.")
    print("The original password cannot be recovered from the hash.")

if __name__ == "__main__":
    main()