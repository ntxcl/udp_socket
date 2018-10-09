# udp_socket
File transfer by sections with connection between client and server through UDP. Checksum for each section was calculated and client can request specific section with feedback of the checksum of that part from server.
Server
Implement a server in Python 3 to listen on UDP port 7037 for requests pertaining to a file specified on the command line. For example,
$ python3 SectionServer.py testfile.gz
should serve requests for sections of testfile.gz.
Requests
Clients may request:
a list of the available sections of the file by sending the string 'LIST'
the contents of a particular section by sending the string 'SECTION n', where n is the number of the section being requested.
Requests may arrive in any order, and may be repeated.
Responses
The response to a LIST request should be in the following format:
<MD5 checksum of file>
0 <size of section 0 in bytes> <MD5 checksum of section 0>
1 <size of section 1 in bytes> <MD5 checksum of section 1>
2 <size of section 2 in bytes> <MD5 checksum of section 2>
…
The second line will be repeated as many times as necessary for the file being served. For example, serving a 100,000 byte file containing all zeros would return the following:
0019d23bef56a136a1891211d7007f6f
0 32768 bb7df04e1b0a2570657527a7e108ae23
1 32768 bb7df04e1b0a2570657527a7e108ae23
2 32768 bb7df04e1b0a2570657527a7e108ae23
3 1696 ce445509b3dfc1da623ed12188f511c9
The response to a SECTION n request should be the bytes comprising section n of the file.
Limits
The maximum number of sections for a file being served is 1,024. The maximum section size is 32 KiB. Finding the maximum supported file size and UDP datagram size are left as exercises for the reader.
