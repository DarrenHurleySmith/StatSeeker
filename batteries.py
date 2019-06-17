from ent import readdata, entropy, pearsonchisquare, correlation, poz, pochisq, monte_carlo
from fips import monobits, poker, run, longruns, contrun


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
    with open(fn, 'rb') as seq:
        if seq.tell()/(2500*params) < 1:
            params = int(seq.tell()/2500)

        for i in range(params):
            r = []
            stat = []
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

            rtmp, stattmp = contrun(s, ver)
            r.append(rtmp)
            stat.append(stattmp)

            res.append(r)
            c.append(stat)

    print(res)
    return res, c
