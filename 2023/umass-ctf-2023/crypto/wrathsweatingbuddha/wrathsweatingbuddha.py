#!/usr/bin/env python3
#
# Polymero
#

# Imports
from Crypto.Util.number import getPrime, GCD, inverse
from secrets import randbelow

# Local imports
with open("flag.txt","rb") as f:
	FLAG = f.read()[::-1]
	f.close()


HDR_1 = r"""|
|
|                    (\         ._._._._._._._._.         /)
|                     \'--.___,'================='.___,--'/
|                      \'--._.__                 __._,--'/
|                        \  ,. |'~~~~~~~~~~~~~~~'| ,.  /
|           (\             \||(_)!_!_!_.-._!_!_!(_)||/             /)
|            \\'-.__        ||_|____!!_|;|_!!____|_||        __,-'//
|             \\    '==---='-----------'='-----------'=---=='    //
|             | '--.      Shrine of the Sweating Buddha      ,--' |
|              \  ,.'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',.  /
|                \||  ____,-------._,-------._,-------.____  ||/
|                 ||\|___|"======="|"======="|"======="|___|/||
|                 || |---||--------||-| | |-||--------||---| ||
|       __O_____O_ll_lO__ll_O_____O|| |'|'| ||O_____O_ll__Ol_ll_O_____O__
|       o | o o | o o | o o | o o |-----------| o o | o o | o o | o o | o
|      ___|_____|_____|_____|____O =========== O____|_____|_____|_____|___
|                               /|=============|\
|     ()______()______()______() '==== +-+ ====' ()______()______()______()
|     ||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||
|     ||      ||      ||     / |==== s(   )s ====| \     ||      ||      ||
|    =======================()  =================  ()=======================
|"""

MENU_1 = r"""|
|
|    +---------------------------------------------------------------------+
|    |  [E]xamine               [A]pproach              [L]eave            |
|    +---------------------------------------------------------------------+
|"""


HDR_2 = r"""|
|           .                                                      .
|         .n                   .                 .                  n.
|   .   .dP                  dP                   9b                 9b.    .
|  4    qXb         .       dX                     Xb       .        dXp     t
| dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
| 9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
|  9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
|   '9XXXXXXXXXXXXXXXXXXXXX'~   ~'OOO8b   d8OOO'~   ~'XXXXXXXXXXXXXXXXXXXXXP'
|     '9XXXXXXXXXXXP' '9XX'  hello   '98v8P'   again  'XXP' '9XXXXXXXXXXXP'
|         ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
|                         )b.  .dbo.dP''v''9b.odb.  .dX(
|                       ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.           _..
|                 ,-'" `-._XXXXXXXXP'   .   '9XXXXXXXXXXXb,--------".  \
|                .         `-XXXXXXb   d|b   dXXXXXXXXXXX:           \  \
|                '           `".XXXXb.dX|Xb.dXXXXX'   'dX:            \  `.
|           (\   |         .   'XXXXXX(   )XXXXXXP      ''.   |.-"`.   \  |
|            \\'-.   /\    ''  |XXXX X.'v'.X XXXX         |   `.. //\   |_'
|             \\ '  /==\   |.   .P^X''b   d''X^XX ---'=---`.._   ./ '  ,'
|             | '   \  '   .'   ;. 9  '   '  P )X uddha      , `"'   `.'
|              \ \  '~~\   `...''b  '       '  d' ~~~~~~~~~~',.  /
|                \`"" __`,'----- '             ' -----.____  ||/
|                 ||\|___|"======="|"======="|"======="|___|/||
|                 || |---||--------||-| | |-||--------||---| ||
|       __O_____O_ll_lO__ll_O_____O|| |'|'| ||O_____O_ll__Ol_ll_O_____O__
|       o | o o | o o | o o | o o |-----------| o o | o o | o o | o o | o
|      ___|_____|_____|_____|____O =========== O____|_____|_____|_____|___
|                               /|=============|\
|     ()______()______()______() '==== +-+ ====' ()______()______()______()
|     ||{_}{_}||{_}{_}||{_}{_}/| ===== |_| ===== |\{_}{_}||{_}{_}||{_}{_}||
|     ||      ||      ||     / |==== s(   )s ====| \     ||      ||      ||
|    =======================()  =================  ()=======================
|"""

MENU_2 = r"""|
|
|    +---------------------------------------------------------------------+
|    |  [R]equest               [B]arter                [L]eave            |
|    +---------------------------------------------------------------------+
|"""


class Buddhier:    
    def __init__(self):
        P, Q = [getPrime(512) for _ in range(2)]
        self.N = P * Q
        self.G = randbelow(self.N * self.N)
        self.L = (P - 1) * (Q - 1) // GCD(P - 1, Q - 1)
        self.U = inverse((pow(self.G, self.L, self.N * self.N) - 1) // self.N, self.N)
        
    def encrypt(self, msg: int) -> int:
        g_m = pow(self.G, msg, self.N * self.N)
        r_n = pow(randbelow(self.N), self.N, self.N * self.N)
        return (g_m * r_n) % (self.N * self.N)
    
    def decrypt(self, cip: int) -> int:
        msg = ((pow(cip, self.L, self.N * self.N) - 1) // self.N * self.U) % self.N
        return msg
    
    def barter(self, cip: int) -> int:
        k = self.decrypt(cip) & 1
        r = randbelow(self.N)
        rG = pow(r, randbelow(self.N), self.N * self.N)
        g_m = pow(rG, k + 1, self.N * self.N)
        r_n = pow(r, self.N, self.N * self.N)
        return (g_m * r_n) % (self.N * self.N)


bud = Buddhier()

STAGE_1, STAGE_2 = True, False


print("|\n|")

print(HDR_1)

print("|\n|")


while STAGE_1:

	try:

		print(MENU_1)

		choice = input("|  > ").lower()

		if choice == 'e':
			print("|\n|\n|  The inscriptions on the front side of the temple state "+'"Shrine of the Sweating Buddha".')
			print("|  The place seems familiar to you... Have you been here before?")
			print("|\n|  On a nearby sign, some public info is displayed:")
			print("|\n|   N:", hex(bud.N))
			print("|   G:", hex(bud.G))

		elif choice == 'a':
			print("|\n|  A piece of paper, carried by the wind, lands in front of your feet.")
			print("|  You pick it up. It reads:")
			print("|\n|  '''")
			print("|   I managed to find HIS flag!... although it appears to be encrypted still.")
			print("|\n|   FLAG: =", hex(bud.encrypt(int.from_bytes(FLAG,'big'))))
			print("|  '''")

			print("|\n|  Before you wrap your head around the message, a darkness suddenly surrounds you.")
			print("|  You look up and see HIM. You have been here before for sure...")

			print(HDR_2)

			print('|\n|  "I am so glad to meet with you again, my child ~~~ It has been too long."')
			print('|  "I see your predecessor has left you something, no? Want ME to help you with that?"')

			STAGE_2 = True
			break

		elif choice == 'l':
			print("|\n|\n|  ~ A soft whisper in the wind bids you farewell.\n|")
			break

		else:
			print("|\n|  As you blink, you suddenly find yourself back where you started...")


	except KeyboardInterrupt:
		print("\n|\n|  ~ A soft whisper in the wind bids you farewell.\n|")
		break

	except:
		print("|\n|  As you blink, you suddenly find yourself back where you started...")


FIRST_TIME = True

while STAGE_2:

	try:

		print(MENU_2)

		choice = input("|  > ").lower()

		if choice == 'r':
			print('|\n|  HE bellows a laugh, then says "You are in no position to make requests, my child ~~~"')

		elif choice == 'b':
			if FIRST_TIME:
				print('|\n|  HE thinks for a while... "As the keeper of this shrine I will respect your offerings..."')
				print('|  "Offer ME a ciphertext and I will return its LSB ~~"')

			offer = int(input("|\n|   OFFER(int): "))

			print('|\n|  "Here you go, my child ~~~"')
			print("|   LSB: {}".format(hex(bud.barter(offer))))

			if FIRST_TIME:
				print('|\n|  "You look surprised... Did you really think I would just give it to you straight up ~ ?"')
				FIRST_TIME = False

		elif choice == 'l':
			print("|\n|\n|  ~ As you walk away, HE bellows after you "+'"See you again, my child."\n|')
			break

		else:
			print("|\n|  As you blink, you suddenly find yourself back where you started...")

	except KeyboardInterrupt:
		print("\n|\n|  ~ As you walk away, HE bellows after you "+'"See you again, my child."\n|')
		break

	except:
		print("|\n|  As you blink, you suddenly find yourself back where you started...")
