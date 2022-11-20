#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from libnum import b2s, s2b
import struct
import sys

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

class Cyclic:
    def __init__(self):
        self.mask = 0xFFFFFFFF
        self.poly = 0xEDB88320
        self.table = []
        for byte in range(256):
            tmp = 0
            for _ in range(8):
                if (byte ^ tmp) & 1:
                    tmp = (tmp >> 1) ^ self.poly
                else:
                    tmp >>= 1
                byte >>= 1
            self.table.append(tmp)
    def calc(self, string):
        value = self.mask
        for c in string:
            value = self.table[(ord(c) ^ value) & 0xFF] ^ (value >> 8)
        return struct.pack('>I', (-1 - value) & self.mask)

sys.stdout = Unbuffered(sys.stdout)
FLAG = open('flag.txt').read().strip()
KEY = AES.get_random_bytes(16)
CC = Cyclic()

def intro():
    print '''
````````````````````````````````````````````````````````````````
`````````````````````...----::::::::::---..`````````````````````
`````````````-/+syhdddmmmmmmddddddddmmmmmmddhhyyso+:````````````
````````````.yhhhhdddmmmmmmddddddddddmmmmmdddddhhhhh+```````````
````````````-yhhhhdddmmmmmddddddddddddddmmmddddhhhhhs```````````
````````````:yhhhhhhhddddmdddddddddddddddddhhhhhhhhhy```````````
````````````/yyo------:/+shdddddddddddhso++::--:+yyyy```````````
````````````/yyoyyyyys+:.``:ohdddddho-``-/osyhyyo+yyy.``````````
````````````/syyyhhhhhhhys/-`-hdddy.`-+syhhhhhhhyyyyy.``````````
````````````/ssyyyyyyyyyyyssosddddhoosyyyyyyyyyyyyyss```````````
````````````/ysooo+////::::/oyhmmmhyso+//////++ooosss```````````
````````````/ssyyyysoo+++osyhhhmmdhhys+//:://+syhyyso```````````
````````````-yyhhddmmddddddddhhdmdhhhddddddddddddhhy+```````````
````````````.ssyyhddddddddddhhhdmdhhhdddddddddhhhyys:```````````
```````  ````oosyyhhddddddhhhhhdmdhhhhhddddhhhyyssso.```````````
````` ` `    -soosyyyyyyyyhhhhhddmhhhhhsssyyyyysooo+``````   ```
````` `   ` ``:sos::syyhddhssyyhhhyyssyhhhyso/:/+os-````      ` 
`````     `````/sss--shhhhhhy:://:-/yyhhhhhh+`/syy+```` `       
`````         ``+ssyo..://+/..`-+.``.+oo+/:`-osyyo-````         
`````         ```+sssyy+:-..``-sss-`````.:+yysyys/`````         
`````         ````+sysssyyyhhhyyyyyyhhhhyssssyss+``````         
`````        ``````/syyyyyssss+oooooossssssyyss/```````         
```````       ``````-oyhyyhhhhy` `:hhhyyssysso-````````         
````           ``   ``/syyyhhds```-hhhyyyyso:`                  
                       .+yyyhhs` `-hhhyyso:`                    
                         .+syyh. `ohyys+-`                      
                           `:+o/ -so/-`                         
       ````````                ````` `               ````````   
  ________   ````         __         __         ```````````  
  \______ \____________  |  | __    |__| ____   ____   ____  
   |    |  \_  __ \__  \ |  |/ /    |  |/  _ \ / ___\_/ __ \ 
   |    `   \  | \// __ \|    <     |  (  <_> ) /_/  >  ___/ 
  /_______  /__|  (____  /__|_ \/\__|  |\____/\___  / \___  >
          \/   ````    \/     \/\______|     /_____/      \/ v1.0
'''

def main():
    while True:
        try:
            inp = b2s(raw_input('Kamu: ').strip())
            chs = CC.calc(inp + FLAG)
            ptx = pad(inp + chs + FLAG, 16)
            cip = AES.new(KEY, AES.MODE_ECB)
            ctx = cip.encrypt(ptx)
            print 'Bang Haxor: %s\n' % (s2b(ctx))
        except:
            break

if __name__ == "__main__":
    intro()
    main()
