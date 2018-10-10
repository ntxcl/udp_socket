
import sys
import socket
import hashlib
import os

#
#ISSUES:
#1. connection was estabilished but needs to receive string requests from clients
#2. usage function with sys.agrv module accessed in terms of this proj instructions
#3. corner cases to handle incorrect input or sth like that
#4. more tests 
#

PORT = 7037
#local ip
serverName = ''

MAX_UDP_PAYLOAD = 65507
CHUNK_SIZE = 32768
FILE = '/Users/banana/Desktop/cpsc471_proj1/zeros'

# def usage(program):
#     sys.exit(f'Usage: python3 {program} [FILE] ')

def checksum(filepath):
    with open(filepath, 'rb') as servedFile:
        hash_md5 = hashlib.md5()
        hash_md5.update(servedFile.read())
        return hash_md5.hexdigest()

def main():

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverName, PORT))

    print("The sever is read to receive data...", serverName, PORT)

    print(checksum(FILE))

    #replying client's requests "SECTION {n} and send file by chunks"
    list_chunkfile = list()
    #string of info from sever that needs to be sent to the client
    listChunks = ""
    #counter for sections 
    i = 0
    with open(FILE, 'rb') as servedFile:
        for chunk_file in iter(lambda: servedFile.read(CHUNK_SIZE), b""):
            hash_md5 = hashlib.md5()
            hash_md5.update(chunk_file)
            list_chunkfile.append(chunk_file)
            listChunks = str(i) + " "+ str(len(chunk_file)) +" "+ str(hash_md5.hexdigest())
            print (listChunks)
            i += 1


if __name__ == '__main__':
    main()








