from ent import readdata, entropy, pearsonchisquare, correlation, poz, pochisq, monte_carlo


def ent(f):
    data, cnts = readdata(f)
    e = entropy(cnts)
    p = pearsonchisquare(cnts)
    c = correlation(data)
    po = poz(p)
    pchi = pochisq(po*100-50)
    m = monte_carlo(data)

    return e, p, c, po, pchi, m