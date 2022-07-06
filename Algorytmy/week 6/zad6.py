import hashlib

filename = input("wprowadz nazwe pliku: ")
md5_hash = hashlib.md5()
with open(filename, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        md5_hash.update(byte_block)
    print(md5_hash.hexdigest())


# 6dbd01b4309de2c22b027eb35a3ce18b
# e4af0ab941dc5c727acd1b2dab932deb
# 128 bitow
