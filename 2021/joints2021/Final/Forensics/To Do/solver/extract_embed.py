from collections import OrderedDict
from base64 import b64decode
from binascii import unhexlify

import zlib
import json
import re
import os

def multimap(ordered_pairs):
    _dict = dict()

    for k, v in ordered_pairs:
        if k in _dict:
            if isinstance(_dict[k], dict):
                _dict[k].update(v)
            else:
                _dict[k] = [_dict[k], v]
        else:
           _dict[k] = v

    return _dict

def parse_body(body):
    data = unhexlify(
        re.sub(r':', '', body)
    ).split('&')

    return [_.split('=')[-1] for _ in data]

def parse_users(cookie):
    raw = b64decode(cookie.split('.')[0][8:])
    data = json.loads(raw)

    return data['username']

def add(user, title, desc):
    global count
    global tasks

    user_task = tasks.get(user, dict())

    if not user_task:
        tasks[user] = user_task

    task_detail = {
        count: {
            'title': title,
            'description': desc
        }
    }

    user_task.update(task_detail)
    count += 1

def edit(user, task_id, title, desc):
    global tasks

    if "'||X" in desc:
        desc = exfiltrate(desc)

    user_task = tasks[user][task_id]
    user_task['title'] = title
    user_task['description'] = desc

def delete(user, task_id):
    global tasks

    user_task = tasks.get(user)
    user_task.pop(task_id)

def make_file(user):
    global pdfs

    try:
        user_file = pdfs[user]['data']
    except:
        user_file = list()

    if not user_file:
        pdfs[user] = dict(
            data=user_file,
            publish_count=0    
        )

def save_file(user, data):
    global pdfs

    user_file = pdfs[user]['data']
    user_file.append(data) 
    extract_stream(user)

    pdfs[user]['publish_count'] += 1

def parse_filename(tasks):
    rule = re.compile(b'(\w{1,4}) rel="attachment" href="file://(.*?)"')
    a_tag = dict()
    link_tag = dict()
    
    embeds = [
        (k,v['description']) for k,v in tasks.items() \
            if rule.findall(v['description'])
    ]

    for index, embed in embeds:
        tag, refs = rule.findall(embed)[0]

        if tag == 'link':
            link_tag[index] = refs
        elif tag == 'a':
            a_tag[index] = refs

    link = OrderedDict(sorted(link_tag.items()))
    a = OrderedDict(sorted(a_tag.items()))

    result = link.values() + a.values()
    return result

def extract_stream(user):
    global pdfs
    global tasks

    id = pdfs[user]['publish_count']
    pdf = pdfs[user]['data'][id]

    if 'Embed' in pdf:
        user_task = OrderedDict(sorted(
            tasks[user].items(),
            key=lambda x: x[0]
        ))

        embedded_file = extract_embedded_file(pdf)
        embedded_name = parse_filename(user_task)

        assert (len(embedded_name) == len(embedded_file))
        dump_file(embedded_name, embedded_file)

def dump_file(path, data):
    for k,v in zip(path, data):
        basedir = 'output' + '/'.join(k.split('/')[:-1])
        target = 'output' + k

        os.popen('mkdir -p %s' % (basedir))
        with open(target, 'wb') as handle:
            handle.write(v)

def extract_embedded_file(data):
    objs = re.compile(b'\d+ \d+ obj(.*?)endobj\n', re.S)
    rule = re.compile(b'/EmbeddedFile.*stream\n(.*?)\nendstream', re.S)
    result = []

    for obj in objs.findall(data):
        for _,stream in enumerate(rule.findall(obj)):
            data = zlib.decompress(stream)
            result.append(data)

    return result

def exfiltrate(payload):
    rule = re.compile(r"X'(.*?)'")
    matches = rule.search(payload).group(1)

    return unhexlify(matches)

with open('data.json') as handle:
    content = handle.read().strip()

packets = json.loads(
    content,
    object_pairs_hook=multimap
)

count = 8
tasks = {}
pdfs = {}

for packet in packets:
    http2 = packet['_source']['layers']['http2']

    urlencoded = http2.get('urlencoded-form') 
    header = http2['http2.stream'].get('http2.header')
    data = http2['http2.stream'].get('http2.body.fragments')

    if header:
        method = header['http2.headers.method']
        action = header['http2.headers.path']
        cookies = header['http2.headers.cookie']

        current_user = parse_users(cookies)            
        print current_user, action

        if 'remove' in  action:
            task_id = int(action.split('/')[-1])
            delete(current_user, task_id)
        elif 'publish' in action:
            make_file(current_user)

    elif urlencoded:
        body = http2['http2.stream']['http2.data.data']
        title, desc = parse_body(body)

        if 'add' in action:
            add(current_user, title, desc)
        elif 'edit' in action:
            task_id = int(action.split('/')[-1])
            edit(current_user, task_id, title, desc)

    elif data:
        reassembled_data = data['http2.body.reassembled.data'].split(':')
        raw_data = unhexlify(''.join(reassembled_data))

        save_file(current_user, raw_data)