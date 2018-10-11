
import sys
from socket import *
import hashlib
import os

#
#ISSUES:
#3. corner cases to handle incorrect input or sth like that
#4. more tests 
#

PORT = 7037
#local ip
serverName = ''
MAX_UDP_PAYLOAD = 65507
CHUNK_SIZE = 32768

def usage(program):
    sys.exit(f'Usage: python3 {program} [FILE] ')

def checksum(filepath):
    with open(filepath, 'rb') as servedFile:
        hash_md5 = hashlib.md5()
        hash_md5.update(servedFile.read())
        return hash_md5.hexdigest()

def main(FILE):
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind((serverName, PORT))
    print("The sever is read to receive data...", serverName, PORT)

    #replying client's requests "SECTION {n} and send file by chunks"
    list_chunkfile = list()
    #string of info from sever that needs to be sent to the client
    listChunks = str(checksum(FILE))
    #counter for sections 
    i = 0
    with open(FILE, 'rb') as servedFile:
        for chunk_file in iter(lambda: servedFile.read(CHUNK_SIZE), b""):
            hash_md5 = hashlib.md5()
            hash_md5.update(chunk_file)
            list_chunkfile.append(chunk_file)
            listChunks += "\n" + str(i) + " "+ str(len(chunk_file)) +" "+ str(hash_md5.hexdigest())
            #number of sections, needed to be limited to 1024
            i += 1
            if(i > 1024):
                raise ValueError ("File is too large...")

    #error message
    error = "not valid command"
    #reveiving and replying to client         
    while True:
        message, clientAddress = serverSocket.recvfrom(MAX_UDP_PAYLOAD)
        data = message.decode()

        if (data == 'LIST'):
            serverSocket.sendto(listChunks.encode(), clientAddress)
        elif (data.split()[0] == 'SECTION'):
            message = list_chunkfile[int(data.split(maxsplit = 2)[1])]
            serverSocket.sendto(message, clientAddress)
        else:
            serverSocket.sendto(error.encode(), clientAddress)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage(sys.argv[0])

    sys.exit(main(*sys.argv[1:]))








