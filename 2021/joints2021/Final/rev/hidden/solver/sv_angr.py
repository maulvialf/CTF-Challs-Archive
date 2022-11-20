import angr
import claripy
import binascii

flag=claripy.BVS("flag",8*100)
fi=open('./res.txt').readlines()
shellcodes=[]
for x in fi:
    shellcodes.append(binascii.unhexlify(x.strip()))
ctr=0
w=None
fl=""
for x in shellcodes:
    p=angr.project.load_shellcode(x,arch="amd64")
    s=p.factory.call_state(addr=0)
    s.memory.store(2000,flag)
    s.regs.rdi=2000
    pg = p.factory.simulation_manager(s)
    r=str(p.factory.block(0).capstone)
    wow= int(r.split('je\t')[1],16)
    pg.explore(find=wow,avoid=wow-7)
    print(pg)
    if pg.found:
        fl+=chr(pg.found[0].solver.eval(flag,cast_to=bytes)[ctr])
        print(fl,ctr)
    else:
        raise Exception('Could not find the solution')
    ctr+=1

