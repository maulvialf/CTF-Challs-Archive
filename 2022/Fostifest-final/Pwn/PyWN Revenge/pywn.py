#!/usr/bin/env python3

import os, sys
import subprocess

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

blacklist = [" ", "|", "&", "$", "' ", '"', ';', 's', 'h']

text = input("[>] Plaintext: ")

for i in blacklist:
  if i in text.lower() or len(text) > 10:
    print("[!] Not allowed!")
    exit()

enc = "echo '{0}' | base64 | rev".format(text)
procc = subprocess.Popen(enc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
secc = procc.communicate()[0]
print(f"[*] Ciphertext: {secc}")
exit()