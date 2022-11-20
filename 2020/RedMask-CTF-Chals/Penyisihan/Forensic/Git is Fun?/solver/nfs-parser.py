from anytree import *

import re
import os
import sys

BASE = 'git'
iters = 0
tree = Node(None)
alias = dict()
folder = dict()

def init(filename):
    f1 = ['nfs.procedure_v2 != 6','nfs.procedure_v2 != 4','nfs', 'nfs.procedure_v2 != 1 || frame.number <=2']
    f2 = ['nfs.data']
    c1 = ['tshark -r', filename, '-Y', '"{}"'.format(' && '.join(f1)), '-w clean.pcap']
    c2 = ['tshark -r clean.pcap | grep -o "V2 .*" > log']
    c3 = ['tshark -r clean.pcap -Y', '"{}"'.format(' && '.join(f2)), '-Tfields -e frame.number -e', f2[0], '> data']
 
    os.popen(' '.join(c1))
    os.popen(' '.join(c2))
    os.popen(' '.join(c3))

def lookup(c,r):
    pass

def get_procedure(command):
    rule = re.compile('(V2 )?(\w*) [(Call,)|(Reply)]')
    matches = rule.findall(command)

    return matches[0][1].lower()

def get_original_path(elements, dicts=folder):
    path = []
    for e in elements.path:
        name = dicts[e.name][0]
        path.append(name)
    return os.path.join(*path)

def get_path(path):
    return str(path)[7:-2]

def is_ok(command):
    return 'Call In' in command

def file_handle(command):
    rule = re.compile('FH: (.*)')
    matches = rule.findall(command)
    return matches[0]

def dir_handle(command):
    rule = re.compile('DH: (.*)')
    matches = rule.findall(command)[0]
    return matches.split('/')

def walk(base):
    global tree

    root = tree
    base = base if isinstance(base, list) else [base] 
    for node in base:
        try:
            root = search.find_by_attr(tree, node)
        except Exception:
            root = search.findall_by_attr(tree, node)[0]

    return root

def read(call, reply):
    pass

def write(call, reply, mode='wb'):
    target_id = file_handle(call).split()[0]
    seek_node = walk(target_id)
    pathname = get_original_path(seek_node)
    content = data[iters + 1]

    print '[v] Writing', pathname
    with open(pathname, mode) as f:
        f.write(content.decode('hex'))
        f.close()


def getattr(call, reply):
    global tree, alias
    if is_ok(reply):

        fh = file_handle(call)
        if tree.name is None:
            tree = Node(fh)
            alias[BASE] = fh
            folder[fh] = [BASE]

            print '[+] Initialize', BASE, 'directory'
            try:
                os.makedirs(BASE)
            except OSError:
                pass

def setattr(call, reply):
    pass

def link(call, reply):
    col, target = dir_handle(call)
    source = col.split()[0]
    base = col.split()[-1]

    current_node = walk(source)
    target_node = walk(base)

    # rename
    if current_node.parent != target_node:
        new_node = Node(source, target_node)
    
    source_name = get_original_path(current_node)
    target_name = get_original_path(target_node) + '/' + target

    alias[target] = source
    folder[source].append(target)

    print '[C] Hard-linking', source_name, 'to', target_name
    os.popen('cp %s %s' % (source_name, target_name))
    
def remove(call, reply):
    try:
        base, target = dir_handle(call)
        current_node = walk([base, alias[target]])
        target_name  = get_original_path(current_node)
   
        # current_node.parent = None
        del alias[target]
        del folder[current_node.name][0]

        if not 'git/objects/pack' in target_name:
            print '[D] Deleting', target_name
            os.popen('rm -rf %s' % (target_name))
    except Exception as e:
        print(str(e) + ' No such file or directory')


def mkdir(call, reply):
    base, target = dir_handle(call)
    target_id = file_handle(reply)

    alias[target] = target_id
    elements = folder.get(target_id, list())
    
    if not elements:
        folder[target_id] = elements
    elements.append(target)  

    current_node = walk(base)
    new_node = Node(target_id, current_node)
    pathname = get_original_path(new_node)

    print '[+] Creating', target, 'directory'
    try:
        os.makedirs(pathname)
    except OSError:
        pass

def rmdir(call, reply):
    base, target = dir_handle(call)
    seek_node = walk([base, alias[target]])
    target_name = get_original_path(seek_node)

    # seek_node.parent = None
    del alias[target]
    del folder[seek_node.name][0]

    if 'git/objects/incoming' in target_name :
        print '[-] Removing', target_name, 'Directory'
        os.popen('rm -rf %s' %(target_name))

def create(call, reply):
    base, target = dir_handle(call)
    target_id = file_handle(reply)

    alias[target] = target_id
    elements = folder.get(target_id, list())
    
    if not elements:
        folder[target_id] = elements
    elements.append(target)

    current_node = walk(base)
    new_node = Node(target_id, current_node)
    pathname = get_original_path(new_node)

    print '[~] Creating File', pathname
    os.popen('touch %s' % (pathname))

def rename(call, reply):
    base, col, target = dir_handle(call)
    source = col.split()[0]
    target_id = col.split()[-1]

    assert (base==target_id)
    
    current_node = walk([base, alias[source]])
    source_name = get_original_path(current_node)
    target_name = source_name.replace(source, target)
    
    del alias[source]
    alias[target] = current_node.name
    folder[current_node.name].append(target)

    print '[!] Renaming', source_name, 'to', target_name
    os.rename(source_name, target_name)

def symlink(call, reply):
    pass

def readdir(call, reply):
    pass


if __name__ == "__main__":
    init(sys.argv[1])
    logs = open('log','rb').read().split('\n')[:-1]
    data = dict()

    for _ in open('data','rb').read().split('\n')[:-1]:
        index, content = _.split()
        data[int(index)] = content

    calls = logs[::2]
    replies = logs[1::2]

    for call, reply in zip(calls, replies):
        p1,p2 = map(get_procedure, (call, reply))
        assert (p1==p2), "Procedure must be same, ({} != {})".format(p1,p2)
        assert ('Call' in call), call
        assert ('Reply' in reply), reply

        func = eval(p1)
        func(call, reply)

        iters += 2
