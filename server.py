import ipfshttpclient
from constants import DEFAULT_LOG_MODE, LOG_DIR

def upload_file():
	# Share TCP connections using a context manager
	client = ipfshttpclient.connect('127.0.0.1', 5001)
	res = client.add('./log/*')
	print(LOG_DIR)
	print(res)

# # Share TCP connections until the client session is closed
# class SomeObject:
# 	def __init__(self):
# 		self._client = ipfshttpclient.connect(session=True)

# 	def do_something(self):
# 		hash = self._client.add(LOG_DIR+filename)['Hash']
# 		print(self._client.stat(hash))

# 	def close(self):  # Call this when your done
# 		self._client.close()

"""
import socket
import os
import uuid
import re
import hashlib

class Server:
	def __init__(self):
		global conn, addr
		self.sfile = None

		s = socket.socket()
		# host = socket.gethostname()
		# print(f"host: {host}")
		host = '127.0.0.1'
		port = 65308
		s.bind((host,port))
		s.listen(1) #only one connection

		conn, addr = s.accept()
		print('[+] Client has connected')

		self.sfile = self.get_file()

		self.send_file()

		self.send_smac()

		self.send_sfhash()


	def get_file(self):
		file = input(str("[+] Input the name of the file you would like to send: ")) #holds path to files
		return file

	def send_file(self):
		cwd = os.getcwd()
		f = open(f"{cwd}/uploads/{self.sfile}", 'rb')
		file_data = f.read(1024)
		conn.send(file_data) #file sent in utf-8 bytes

"""