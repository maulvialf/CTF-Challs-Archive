import time
import os
import re

def exfiltrate(query, records):
    rule = re.compile(
        r'(%s)(\n.*){2,8}\$DATA((\n\d{10}:.*){0,1000})' \
      % (query)
    )

    return rule.findall(records)

mft_records = open('mft-records').read()
mft_files = exfiltrate('confide.txt', mft_records)
mft_files += exfiltrate('\$[R|I][A-Z0-9]{6}\.?.*', mft_records)

for matches in mft_files:
    filename = matches[0]
    contents = matches[2]

    if contents:
        with open('temp', 'wb') as f:
            f.write(contents.encode('utf-8'))

        try:
            os.makedirs('trash')
        except OSError:
            pass
        finally:
            os.system("xxd -r temp > 'trash/%s'" % (filename))
            os.remove('temp')