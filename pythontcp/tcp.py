import socket

target_host = "www.google.com"
target_port = 80

	#create a socket object
	#socket takes 2 params
	#AF_INET is default which indicates IPv4 or hostname
	#SOCK_STREAM indicates that it will be a TCP Client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#connect the client

client.connect((target_host, target_port))

	#send some data

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

	#receive some data

response = client.recv(4069)

print(response.decode())
client.close()