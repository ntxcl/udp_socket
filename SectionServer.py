
import sys
import socket
import hashlib
import os

PORT = 7037
#local ip
serverName = ''

MAX_UDP_PAYLOAD = 65507
CHUNK_SIZE = 32768
FILE = '/Users/banana/Desktop/cpsc471_proj1/zeros'

# def usage(program):
#     sys.exit(f'Usage: python3 {program} [FILE] '

#checksum for the file
def checksum(filepath):
    print("checksum")
    with open(filepath, 'rb') as servedFile:
        hash_md5 = hashlib.md5()
        hash_md5.update(servedFile.read())
        return hash_md5.hexdigest()

# def checksumbychunk(filepath, chunksize):
#     print("checksumbychunk")
    # hash_md5_chunk = hashlib.md5()
    # filesize = os.path.getsize(filepath)
    # print(filesize)
    # with open(filepath, 'rb') as servedFile:
    #     for i in range (0, filesize, chunksize):
    #         print(i+chunksize)
            # data = servedFile[i].read()
            # hash_md5_chunk.update(data)
            # print(hash_md5_chunk.hexdigest())
            # print(len(servedFile[i]))


def main():
    print("im main starts")
    
    print(checksum(FILE))

    #connction with client
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverName, PORT))

    print("The sever is read to receive data...", serverName, PORT)

    #replying client's requests "SECTION {n} and send file by chunks"
    list_chunkfile = list()
    listChunks = ""
    i = 0
    with open(FILE, 'rb') as servedFile:
        for chunk_file in iter(lambda: servedFile.read(CHUNK_SIZE), b""):
            hash_md5 = hashlib.md5()
            hash_md5.update(chunk_file)
            list_chunkfile.append(chunk_file)
            print(len(list_chunkfile))
            print(len(chunk_file))
            print (hash_md5.hexdigest())
            listChunks += str(i) + " "+ str(len(chunk_file)) +" "+ str(hash_md5.hexdigest())+"\n"
            print (listChunks)
            i += 1

	
    # while True:
    #     message, clientAddress = serverSocket.recvfrom(MAX_UDP_PAYLOAD)
    #     data = message.decode()
    #     if data == 'LIST':
    #         serverSocket.sendto(listChunks.encode(), clientAddress)
        # else if data == 'SECTION':
        # else

if __name__ == '__main__':
    print("im main")
    main()







