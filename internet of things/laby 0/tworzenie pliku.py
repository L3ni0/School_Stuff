import random



def random_bytes(size):
    bytes = []
    for _ in range(size):
        bytes.append(random.randrange(0, 255))
    return bytes


bytes = random_bytes(30)

with open('binary file.txt', 'wb') as file:
    for i in bytes:
        file.write(i.to_bytes(1, byteorder='big'))
