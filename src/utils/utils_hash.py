import hashlib


def generate_hash(string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(string.encode('utf-8'))
    hash_value = sha256_hash.hexdigest()
    return hash_value
