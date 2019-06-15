from ent import readdata, entropy, pearsonchisquare, correlation, poz, pochisq, monte_carlo


# Ent (John Walker) tests called from the module developed by RSmith
def ent(f):
    data, cnts = readdata(f)
    e = entropy(cnts)
    p = pearsonchisquare(cnts)
    c = correlation(data)
    po = poz(p)
    pchi = pochisq(po*100-50)
    m = monte_carlo(data)

    return e, p, c, po, pchi, m


# FIPS140-1 tests, called from the appropriate module
def fips1(f, t):
    return a, b, c, d, e


# FIPS140-2 tests, called from the appropriate module
def fips1(f, t):
    return a, b, c, d, e