from FLAG import flag
import random
import math
import time

ITERATIONS = 47
SIDE_LENGTH = 2 * 10 ** 9
ATTEMPTS = 300

HI = SIDE_LENGTH // 2
LO = -SIDE_LENGTH // 2

def banner():
    banner = """
┌──────────────────────────────────────────────────────────────────────┐
│┼───────────────────┼────────────────────────┼┼──────────────────────┼│
││ XenoCal 2000      │     .                  ││                      ││
│┼───────────────────┤              ┌─┐      x││      .        .      ││
││ Iteration: 42     │    x     ►   └─┘       ││          x           ││
│┼─────────┬─────────┤                        ││                      ││
││ X:1337  │ Y:65189 │      .   x         ┌───┼┼───┐                  ││
│┼─────────┴─────────┘  x               ┌─┘   ││   └─┐     x          ││
││   .                                ┌─┘     ││     └─┐              ││
││    ┌─┐          x              ▼  ┌┘   .   ││       └┐      x      ││
││    └─┘                   .       ┌┘        ││        └┐            ││
││           .                      │         ││      .  │            ││
│┼──────────────────────────────────┼─────────┼┼─────────┼────────────┼│
││                        x         │   x     ││         │      ▼     ││
││  x      ──►x                     └┐        ││        ┌┘            ││
││                   .        ▼      └┐       ││       ┌┘    .        ││
││          .                         └─┐     ││     ┌─┘              ││
││     ┌─┐              x               └─┐   ││   ┌─┘           x    ││
││     └─┘      ┌─┐             ┌─┐       └───┼┼───┘                  ││
││              └─┘             └─┘           ││                      ││
││         x         .          .             ││          .           ││
││    .                             x         ││              x       ││
││   x             ▼   x                   .  ││      x               ││
││                                            ││                      ││
│┼────────────────────────────────────────────┼┼──────────────────────┼│
└──────────────────────────────────────────────────────────────────────┘    ┌─
                                                                            │
        ┌─┬───────────────────────────┬─┐             ┌──────┐          ┌───┼┐
        │ │┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼│ │             │[=()=]│          ├────┤
        │ │┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼│ │          ┌──┼──────┼──┐       │    │
        │ │┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼│ │          │◄├┼┼┼┼┼┼┼┼┤►│       │    │
        │ │┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼│ │          └──┼──────┼──┘       ├────┤
        └─┴───────────────────────────┴─┘             │[=()=]│          └────┘
                                                      └──────┘
"""
    print(banner)


def load():
    boot_messages = \
    """
[\033[92mOK\033[0m] Memory check      
[\033[92mOK\033[0m] Syncing filesystem
[\033[92mOK\033[0m] Detecting sensors
[\033[92mOK\033[0m] Module loader
[\033[92mOK\033[0m] Reading configurations

Inititing calibration process ...
    """.split('\n')
    for m in boot_messages:
        print(m)
        time.sleep(random.random())


# Calibrator's error acceptance threshold
e = 2
if __name__ == '__main__':
    load()
    banner()

    for i in range(ITERATIONS):
        print(f"Iteration {i}:")
        R = random.randint(SIDE_LENGTH // 4, SIDE_LENGTH // 2)
        X = random.randint(LO + R, HI - R)
        Y = random.randint(LO + R, HI - R)

        for a in range(ATTEMPTS):
            line = input("> ")
            x, y = [int(n) for n in line.split(' ')]
            D = math.sqrt((X - x) ** 2 + (Y - y) ** 2)
            if D <= e:
                print("\033[94mREFERENCE", end="\n\033[0m")
                break
            elif D <= R:
                print("\033[92mDETECTED", end="\n\033[0m")
            else:
                print("\033[91mUNDETECTED", end="\n\033[0m")
        else:
            exit(0)

    print(flag)
