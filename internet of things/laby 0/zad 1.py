def read_byte_file(name):
    with open(name,'rb') as file:
        while byte := file.read(1):
            print(int.from_bytes(byte, byteorder='big'))


def write_byte_file(name, number : int):
    with open(name, 'ab') as file:
        file.write(number.to_bytes(3, byteorder='big'))

read_byte_file('binary file.txt')