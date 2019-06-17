import csv
import os

HEADER_ent = ['File name', 'Entropy', 'Chi-score', 'Serial Correlation', 'P-val Z', 'P-val Chi', 'Monte Carlo']
HEADER_fips = ['File name', 'Monobit', 'Poker', 'Run', 'Long run', 'Continuous']


def raiser(ex): raise ex


def dir_path(string):
    return string if os.path.isdir(string) else raiser(NotADirectoryError(string))


# take results of ent and returns csv of results
def ent_csv(paths, results):
    with open('results/ent_results.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_ent)
        for i in range(len(paths)):
            entropy, chi_score, serial_correlation, p_val_z, p_val_chi, monte_carlo = results[i]
            writer.writerow([paths[i], entropy, chi_score, serial_correlation, p_val_z, p_val_chi, monte_carlo])
        csvfile.close()


# take results of ais-31 (non-fips) tests and returns csv of results
def ais_csv(r):
    return c

# takes results  of fips140-2 and returns results csv
def fips_csv(paths, results, stats):
    with open('results/fips_results.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_fips)
        for i in range(len(paths)):
            print(results[i])
            monobit, poker, run, longrun, continuous = results[i]
            writer.writerow([paths[i], monobit, poker, run, longrun, continuous])
        csvfile.close()

# merges all csvs passed in as a list of csv names (default filenames only atm)
# returns single csv with individual files joined on file names with concatenated result columns
def csv_merge(a):
    return c
