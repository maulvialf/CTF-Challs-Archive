from textwrap import *
from string import *
from random import *

import re

c = wrap(ascii_lowercase + ascii_uppercase  + digits + '#$', 8)
shuffle(c)
c = ''.join(c)

def encode(data):
    s = re.findall('.{1,3}', data, flags=re.S)
    p = len(data) % 3
    r = ''

    for _ in s:
        x, y, z = _.ljust(3, '\x00')

        _ = ord(x) << 16 | ord(y) << 8 | ord(z)
        r += c[_ >> 18] + c[(_ >> 12) & 0x3f]
        r += c[(_ >> 6) & 0x3f] + c[_ & 0x3f]
    r = r.lower()
    
    return r[:-p] if p else r

flag = open('flag.txt').read()
text = """
While the argument seems to be different the truth is it's always the same.
Yes, the topic may be different or the circumstances, but when all said and done, it all came back to the same thing.
They both knew it, but neither has the courage or strength to address the underlying issue. So they continue to argue.
There wasn't a bird in the sky, but that was not what caught her attention.
It was the clouds. The deep green that isn't the color of clouds, but came with these.
She knew what was coming and she hoped she was prepared.
There was a time when he would have embraced the change that was coming.
In his youth, he sought adventure and the unknown, but that had been years ago.
He wished he could go back and learn to find the excitement that came with change but it was useless.
That curiosity had long left him to where he had come to loathe anything that put him out of his comfort zone.
Anyway the flag is %s...
""" % (flag)

with open('result.txt', 'w') as f:
    f.write(encode(text))