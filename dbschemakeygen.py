import hashlib
import random
import string
import sys

def random_num(min_val, max_val):
    return random.randint(min_val, max_val)

def get_salt():
    r = random_num(10000, 30000)
    return str(r)

def generate_key(name):
    salt = get_salt()
    print("salt:", salt)
    encrypt_source = "ax5" + name + "b52w" + salt + "vb3"
    print("encrypt:", encrypt_source)
    hash_obj = hashlib.md5(encrypt_source.encode())
    hash_str = hash_obj.hexdigest()
    print("md5:", hash_str)
    return hash_str[:4] + salt + hash_str[4:]

def main():
    print("DbSchema Key Generator")
    print("Usage: keygen <username>")
    if len(sys.argv) < 2:
        return 0
    username = sys.argv[1]
    key = generate_key(username)
    print("Key:")
    print(key)
    return 1

if __name__ == "__main__":
    random.seed()  # seeding the random number generator
    sys.exit(main())
