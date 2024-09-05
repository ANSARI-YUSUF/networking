from socket import *
import string

s1=socket(AF_INET, SOCK_DGRAM)
print(s1)
s1.bind(('172.16.116.146',10005))
print(s1)

# s1.listen(3)
print('Waiting for Connection.....')

while True:

    msg,add=s1.recvfrom(1048)
    mod_msg=msg.decode()
    print("client add and messege :"+ mod_msg,add)
    u_msg=mod_msg.upper()


   
    reversed_string = u_msg[::-1]
    





    s1.sendto(reversed_string.encode(),add)
    s1.close()

