from ent import readdata, entropy, pearsonchisquare, correlation, poz, pochisq, monte_carlo


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


# FIPS140-1 tests, called from the appropriate module
def fips1(f, t):
    return a, b, c, d, e


# FIPS140-2 tests, called from the appropriate module
def fips1(f, t):
    return a, b, c, d, e