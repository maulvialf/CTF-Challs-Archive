# Extract MFT records
vol.py -f memory.dmp --profile=Win7SP1x86_23418 mftparser > mft-records

# Extract files inside of MFT hexdump
python3 parse.py

# List & Recover deleted files
trashparse trash --sort time -w files

# Concate SECRET files
ls files/SECRET* | sort -t'(' -k2 -n | xargs -Iz cat z | base32 -d

# Download confidential.zip from confide.txt
gdown --id 1vz_G1Pyy3O6hy0En8hNLA8mYIVAY_o-P -O confidential.zip

# Unzip confidential.zip using password from SECRET files
7z x -so -p'U945#RCgDb1lLMJotdmH9^J%Qhoc9&L8c2$' confidential.zip