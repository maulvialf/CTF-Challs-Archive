#!/usr/bin/env python2

import os, sys
import subprocess
from random import randint

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def writelines(self, datas):
    self.stream.writelines(datas)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

secret = randint(0, 999999)
blacklist = [" ", "|", "&", "$", "' ", '"']

try:
	key = input("[>] Insert key to use our service: ")

	if key == secret:
		text = raw_input("[>] Plaintext: ")
		for i in blacklist:
			if i in text or len(text) > 9:
				print "[!] Not allowed!"
				exit()

		enc = "echo '{0}' | base64 | rev".format(text)
		procc = subprocess.Popen(enc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		secc = procc.communicate()[0]
		print "[*] Ciphertext :", secc
		exit()
	else:
		print "[!] Wrong!"
except:
	print "[!] Wrong!"
