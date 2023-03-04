import hashlib
# Rtrams

email = "scd@gmail.com"
pwd = "abcxyz"

pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd)
print(pwd_hash)

your_email = "scd@gmail.com"
your_password = "abcxyz"

hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()

if email == your_email and pwd_hash == hashed_your_password:
    print("Right user")
else:
    print("Wrong password")

hacker_pass = "70fb874a43097a25234382390c0baeb3"