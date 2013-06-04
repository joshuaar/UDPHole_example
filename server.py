from socket import *
import sys
import select
address = ('', 6004)

clientAddr = ('serverHostNameorIP',6004) # Get this from STUN server

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

print "Trying to punch a hole"
server_socket.sendto("Hole Punch",clientAddr)
while(1):
    print "Listening"
    recv_data, addr = server_socket.recvfrom(2048)
    print recv_data
    print "Address: ",addr
    if recv_data == "Request 1" :
        print "Received request 1"
        server_socket.sendto("Response 1", addr)
    elif recv_data == "Request 2" :
        print "Received request 2"
        data = "Response 2"
        server_socket.sendto(data, addr)
        
        
