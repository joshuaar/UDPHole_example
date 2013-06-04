from socket import *
import sys
import select

address = ('', 6004)

serverAddr = ('smaugshideout.com',6004)

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.bind(address)
num_retransmits = 0
while(num_retransmits < 60):
    num_retransmits = num_retransmits + 1
    data = "Request 1"
    client_socket.sendto(data, serverAddr)
    print "Sending request 1"

    recv_data, addr = client_socket.recvfrom(2048)

    print recv_data, "!!"