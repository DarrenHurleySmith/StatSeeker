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
    with open('results/fips_results.csv', 'w') as csvfile:
        monobits = []
        pokers = []
        runs = []
        longruns = []
        continuouss = []
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_fips)
        for i in range(len(results)):
            monobits.append([])
            pokers.append([])
            runs.append([])
            longruns.append([])
            continuouss.append([])
            for j in range(len(results[i])):
                monobits[i].append(results[i][j][0])
                pokers[i].append(results[i][j][1])
                runs[i].append(results[i][j][2])
                longruns[i].append(results[i][j][3])
                continuouss[i].append(results[i][j][4])

        for i in range(len(results)):
            writer.writerow([paths[i], monobits[i], pokers[i], runs[i], longruns[i], continuouss[i]])
        csvfile.close()

    with open('results/fips_stats.csv', "w") as csvfile:
        monobits = []
        pokers = []
        runs = []
        longruns = []
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_fips)
        for i in range(len(stats)):
            monobits.append([])
            pokers.append([])
            runs.append([])
            longruns.append([])
            for j in range(len(stats[i])):
                try:
                    monobits[i].append(stats[i][j][0])
                    pokers[i].append(stats[i][j][1])
                    runs[i].append(stats[i][j][2])
                    longruns[i].append(stats[i][j][3])
                except TypeError:
                    pass

        for i in range(len(results)):
            writer.writerow([paths[i], monobits[i], pokers[i], runs[i], longruns[i]])
        csvfile.close()

# merges all csvs passed in as a list of csv names (default filenames only atm)
# returns single csv with individual files joined on file names with concatenated result columns
def csv_merge(a):
    return c
