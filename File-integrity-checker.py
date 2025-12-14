import hashlib

data = b"test"

hash_sha256 = hashlib.sha256(data).hexdigest()

print(hash_sha256)
