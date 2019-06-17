from ent import readdata, entropy, pearsonchisquare, correlation, poz, pochisq, monte_carlo
from fips import monobits, poker, run, longruns, contrun
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
