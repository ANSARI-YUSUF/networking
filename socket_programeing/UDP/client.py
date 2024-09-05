from socket import *

client_socket=socket(AF_INET,SOCK_DGRAM)

msg=input('Input message in lower case:')
client_socket.sendto(msg.encode(),('172.16.116.146',10005))
mod_msg,server_addr=client_socket.recvfrom(1048)
print(mod_msg.decode())
client_socket.close()