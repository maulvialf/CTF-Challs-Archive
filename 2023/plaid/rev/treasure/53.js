const b64 = `
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
0
1
2
3
4
5
6
7
8
9
+
/
=`;
export const go = async () => {
    const bti = b64.trim().split("\n").reduce((acc, x, i) => (acc.set(x, i), acc), new Map());
    const upc = window.buffer.shift();
    const moi = await fetch(import.meta.url).then((x) => x.text())
    const tg = await fetch(moi.slice(moi.lastIndexOf("=") + 1)).then((x) => x.json())
    const fl = tg.mappings.split(";").flatMap((v, l) =>v.split(",").filter((x) => !!x).map((input) => input.split("").map((x) => bti.get(x)).reduce((acc, i) => (i & 32 ? [...acc.slice(0, -1), [...acc.slice(-1)[0], (i & 31)]] : [...acc.slice(0, -1), [[...acc.slice(-1)[0], i].reverse().reduce((acc, i) => (acc << 5) + i, 0)]].map((x) => typeof x === "number" ? x : x[0] & 0x1 ? (x[0] >>> 1) === 0 ? -0x80000000 : -(x[0] >>> 1) : (x[0] >>> 1)).concat([[]])), [[]]).slice(0, -1)).map(([c, s, ol, oc, n]) => [l,c,s??0,ol??0,oc??0,n??0]).reduce((acc, e, i) => [...acc, [l, e[1] + (acc[i - 1]?.[1]??0), ...e.slice(2)]], [])).reduce((acc, e, i) => [...acc, [...e.slice(0, 2), ...e.slice(2).map((x, c) => x + (acc[i - 1]?.[c + 2] ?? 0))]], []).map(([l, c, s, ol, oc, n], i, ls) => [tg.sources[s],moi.split("\n").slice(l, ls[i+1] ? ls[i+1]?.[0] + 1 : undefined).map((x, ix, nl) => ix === 0 ? l === ls[i+1]?.[0] ? x.slice(c, ls[i+1]?.[1]) : x.slice(c) : ix === nl.length - 1 ? x.slice(0, ls[i+1]?.[1]) : x).join("\n").trim()]).filter(([_, x]) => x === upc).map(([x]) => x)?.[0] ?? tg.sources.slice(-2, -1)[0];
    import(`./${fl}`).then((x) => x.go());
}
//# sourceMappingURL=53.js.map