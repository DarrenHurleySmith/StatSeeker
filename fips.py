from numpy import *
from bitstring import BitArray

def fips1401(fn):
	res = []
	monores = []
	pokerres = []
	runres = []
	longrunres = []
    contrunres = []


#monobits test as defined in FIPS140-1
def monobits(s):
    res = True
	b = BitArray(s)
	c = b.count(True)

    if x<9654 or x>10346:
        res = False

	return c, res


# poker test as defined in FIPS140-1
def poker(s):
    res = [0] * 16
    h = ''.join(format(x, '02x') for x in s)
    for i in h:
        res[int(i, 16)] = res[int(i, 16)] + 1

    sres = [x ** 2 for x in res]
    tres = sum(sres)
    fres = (16 / 5000) * tres - 5000
    return fres


# runs test as defined in FIPS140-1
def run(s):
    b = BitArray(s)
    c = [0] * 6
    cnt = 0

    for i in range(0, len(b) - 1):
        if b[i] == b[i + 1]:
            cnt = cnt + 1
        else:
            if cnt < 6 and cnt > 0:
                c[cnt - 1] = c[cnt - 1] + 1
            elif cnt >= 6:
                c[5] = c[5] + 1
            cnt = 0
    return c


# long run test as defined in FIPS140-1	- self evaluates
def test4(s):
    res = True
    b = BitArray(s)
    c = [0, 0]

    for i in b:
        if i == '0':
            c[1] = 0
            c[0] = c[0] + 1
            if c[0] > 34:
                res = False
                break
        elif i == '1':
            c[0] = 0
            c[1] = c[1] + 1
            if c[1] > 34:
                res = False
                break

    return c, res


# continuous run test - checks for any repeated 16 byte sequence in the input sequence - repetition == failure
def contrun(s):
    res = True
    check = s[:128]
    comp = s[128:]

    for i in range(len(comp)/128):
        chunk = comp[i*128:(i*256)]
        if chunk == comp:
            res = False

    return res