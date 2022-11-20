import os

def read_file(name):
    with open(name, 'rb') as handle:
        return handle.read().decode()

logs = os.popen('cd normal-repo && git log --oneline').readlines()
result = dict()

for log in logs[::-1]:
    commit_id = log.split()[0]
    index = log.split()[-2][:-2]
    os.popen('cd normal-repo && git checkout ' + commit_id)
    content = read_file('normal-repo/flag.txt')
    result[int(index)] = content

print(''.join(result.values()))
