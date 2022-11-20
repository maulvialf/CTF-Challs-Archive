import string
import itertools
import random
import json

char = string.lowercase + string.uppercase + string.digits + '_'
name = ["".join(x) for x in list(itertools.permutations("WeirdChamp",10))]
flag = 'W_R3vers3r_0n_g0d'
dicc = {}


def create_entry(p):
    stub = '''
[<EntryPoint>]
let main argv =
    {} (Seq.toList argv.[0])
    0
'''.format(p)
    return stub

def create_fun(p, q, r, s, t):
    stub = '''
let {} x =
    match x with
    | y :: z ->
        match y with
        | '{}' -> {} z
        | '{}' -> {} z
        | _ -> printfn "L"
    | [] -> 
        printfn "L"
'''.format(p, q, r, s, t)
    return stub

def create_end(p, q):
    stub = '''
let {} x = printfn "{}"
'''.format(p, q)
    return stub

def randchar():
    return random.choice(char)

def randname():
    return name.pop(0)

def create_dict(depth):
    if depth > 0:
        x = {}
        for i in range(2):
            x[randname() + randchar()] = create_dict(depth - 1)
        return x
    else :
        return 'L'

def program_writer(out, parent, name):
    keys = parent.keys()
    if type(parent[keys[0]]) != dict:
        out.write(create_end(keys[0][:-1], parent[keys[0]]))
        out.write(create_end(keys[1][:-1], parent[keys[1]]))
        out.write(create_fun(name[:-1],
                keys[0][-1],
                keys[0][:-1],
                keys[1][-1],
                keys[1][:-1]))

    else:
        program_writer(out, parent[keys[0]], keys[0])
        program_writer(out, parent[keys[1]], keys[1])
        out.write(create_fun(name[:-1],
                            keys[0][-1],
                            keys[0][:-1],
                            keys[1][-1],
                            keys[1][:-1]))

def create_json():
    forsen = name.pop(0)
    dicc[forsen] = create_dict(17)
    data = json.dumps(dicc)
    temp = open('temp.json', 'wb')
    temp.write(data)

def edit_json(flag):
    temp = open('temp.json').read()
    dicc = json.loads(temp)['WeirdChamp']
    arr = []
    for i in flag:
        keys = dicc.keys()
        rand = random.choice(keys)
        temp = temp.replace(rand, rand[:-1] + i)
        dicc = dicc[rand]
        arr.append(rand[:-1] + i)
    print (arr)
    out = open('withflag.json','wb')
    out.write(temp)
    out.close()

def write_program():
    temp = open('withflag.json').read()
    dicc = json.loads(temp)
    weird = dicc['WeirdChamp']
    fs = open('Program.fs', 'wb')
    program_writer(fs, weird, 'WeirdChamp?')
    fs.write(create_entry('WeirdChamp'))


# create_json()
# edit_json(flag)
# write_program()
