from secrets import randbelow
import random
from functools import reduce
from operator import and_, or_
from time import time
import signal
from tqdm import tqdm

def random_formula(num_vars, num_clauses):
    formula = []
    for _ in range(num_clauses):
        clause = set()
        for _ in range(random.randint(1,num_vars)):
            clause.add(random.randint(1,num_vars))
        formula.append(tuple(random.choice([-1,1])*j for j in clause))
    return tuple(formula)

def eval_formula(clause,vars):
    return reduce(or_, (reduce(and_,(vars[c-1] if c>0 else not(vars[-c-1]) for c in cl)) for cl in clause))

def get_balanced(num_vars, num_clauses, num_trials=512, thresh=0.05):
    while True:
        balance = 0
        dnf = random_formula(num_vars,num_clauses)
        for _ in range(num_trials):
            x = [random.randint(0,1) for _ in range(num_vars)]
            if eval_formula(dnf, x):
                balance += 1
            else:
                balance -= 1
        if -num_trials*thresh < balance < num_trials*thresh:
            return dnf

class PrivateHash:
    def __init__(self, N_in, N_out, n_clauses=9, verif_lvl=512):
        self.N_in = N_in
        self.N_out = N_out
        self.functions = [get_balanced(N_in, n_clauses, verif_lvl) for _ in tqdm(range(N_out))]

    def hash(self, numb):
        assert numb.bit_length()<=self.N_in
        numb_bits = list(map(int,bin(numb)[2:].zfill(self.N_in)))
        res = 0
        for i in range(self.N_out):
            res *= 2
            res += eval_formula(self.functions[i], numb_bits)
        return res


class BlokeChain:
    def __init__(self,N,O,n_cl=9,verif_lvl=512):
        self.mining_rate = 1 # 1 bloke per second
        self.num_new = self.mining_rate*60 # number of new blokes per second
        self.N = N
        self.O = O
        self.H = PrivateHash(N, O, n_cl, verif_lvl)
        self.B = 0

    def get_pending_blocks(self):
        self.start_time = time()
        self.blokes = [(randbelow(2**self.N), randbelow(100_000)) for _ in range(self.num_new)]

    def verify_chain(self, hashes):
        num_unmined = int(time()-self.start_time)//self.mining_rate
        total_payout = 0
        for i in range(num_unmined, len(self.blokes)):
            bloke_hash = self.H.hash(self.blokes[i][0])
            if bloke_hash == hashes[i]:
                total_payout += self.blokes[i][1]
            print(f"expected hash {hex(bloke_hash)[2:].zfill(self.O//4)} for {self.blokes[i][0]} got {hex(hashes[i])[2:].zfill(self.O//4)}")
        return total_payout


if __name__ == "__main__":
    B = BlokeChain(50, 100, 10, 500)
    PROMPT =  ("Choose an option\n"
              "1. Get unmined blocks\n"
              "2. Submit mined blocks\n"
              "3. Destroy vessels\n")
    signal.alarm(2000)
    while True:
        try:
            option = int(input(PROMPT))
            match option:
                case 1:
                    print("Retriving new blokes in the pool")
                    B.get_pending_blocks()
                case 2:
                    hashes = []
                    for i in range(B.num_new):
                        hashes.append(int(input(f"enter hash for {B.blokes[i][0]}: ")))
                    B.B += B.verify_chain(hashes)
                    print("Balance:",B.B)
                case 3:
                    if B.B > 100_000_000:
                        print("FLAG")
                    else:
                        print("Attack blocked!")
                    exit(0)
        except Exception as e:
            print(e)
            print("Enabling self defend system in: 1...")
            exit(1)
