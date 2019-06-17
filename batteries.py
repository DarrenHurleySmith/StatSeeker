from ent import readdata, entropy, pearsonchisquare, correlation, poz, pochisq, monte_carlo
from fips import monobits, poker, run, longruns, contrun
from ais31 import test0, test5, test6a, test7, test8

import os


# Ent (John Walker) tests called from the module developed by RSmith
def ent(path):
    data, cnts = readdata(path)
    res_entropy = entropy(cnts)
    res_chi_score = pearsonchisquare(cnts)
    res_serial_correlation = correlation(data)
    res_p_val_z = poz(res_chi_score)
    res_p_val_chi = pochisq(res_p_val_z*100-50)
    res_monte_carlo = monte_carlo(data)

    return res_entropy, res_chi_score, res_serial_correlation, res_p_val_z, res_p_val_chi, res_monte_carlo


# FIPS140 tests, called from the appropriate module
def fips140(fn, ver, params):
    res = []
    c = []

    fs = os.stat(fn)

    with open(fn, 'rb') as seq:

        if fs.st_size/(2500*params) < 1:
            params = int(fs.st_size/2500)
            print(params)

        if params == 0:
            return ['N', 'N', 'N', 'N', 'N'], [0, 0, 0, 0]

        for i in range(params):
            stat = []
            r = []

            s = seq.read(2500)

            rtmp, stattmp = monobits(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp, stattmp = poker(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp, stattmp = run(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp, stattmp = longruns(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            rtmp = contrun(s, ver)
            r.append(rtmp)

            res.append(r)
            c.append(stat)

    return res, c


# ais31 tests - borrows fips-1-140 mode tests from the fips battery for procedureA
def ais31(fn):
    c = []
    t0 = 0
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    t6 = []
    t7 = []
    t8 = []

    fs = os.stat(fn)

    if fs.st_size > 9038216:
        with open(fn, 'rb') as seq:
            a = seq.read(1038216)
            b = seq.read(8000000)
    else:
        return c


    # procedureA
    t0 = test0(a[:393216])

    for i in range(0, 257):
        x = 393216+(i*2500)
        s = a[x:x+2500]
        t1.append(monobits(s, 1))
        t2.append(poker(s, 1))
        t3.append(run(s, 1))
        t4.append(longruns(s, 1))
        t5.append(test5(s))

    # procedureB

    return c

