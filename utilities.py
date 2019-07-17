import csv
import os

HEADER_ent = ['File name', 'Entropy', 'Chi-score', 'Serial Correlation', 'P-val Z', 'P-val Chi', 'Monte Carlo']
HEADER_fips = ['File name', 'Iterations', 'Monobit', 'Poker', 'Run', 'Long run', 'Continuous']
HEADER_ais31 = ['File name', 'T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6a', 'T6b', 'T7a_1', 'T7a_2', 'T7b_1', 'T7b_2', 'T7b_3', 'T7b_4', 'T8']
HEADER_sp80022 = ['File name', 'Frequency', 'Block Frequency', 'Cumulative Sums', 'Runs', 'Longest Run', 'Rank', 'FFT',
                  'NonOverlapping Template', 'Overlapping Template', 'Universal', 'Approximate Entropy',
                  'Random Excursions', 'Random Excursions Variant', 'Serial', 'Linear Complexity']


def init_csv():
    with open('results/ent_results.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_ent)

    with open('results/ais31_stats.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_ais31)

    with open('results/fips_results.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_fips)

    with open('results/fips_stats.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_fips)

    with open('results/sp80022_stats.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_sp80022)

def dir_path(string):
    return string if os.path.isdir(string) else raiser(NotADirectoryError(string))


# take results of ent and returns csv of results
def ent_csv(path, results):
    with open('results/ent_results.csv', "a") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        entropy, chi_score, serial_correlation, p_val_z, p_val_chi, monte_carlo = results
        writer.writerow([path, entropy, chi_score, serial_correlation, p_val_z, p_val_chi, monte_carlo])
        csvfile.close()


# take results of ais-31 (non-fips) tests and returns csv of results
def ais_csv(path, r):
    with open('results/ais31_stats.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([path, r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]])


def aggregate_lists(data, index, num):
    aggregated = []
    for i in range(num):
        aggregated.append([])
        for j in range(len(data[index])):
            aggregated[i].append(data[index][j][i])
    return aggregated


def fips_csv(path, results, stats, it):
    with open('results/fips_results.csv', 'a') as csvfile:
        monobits = []
        pokers = []
        runs = []
        longruns = []
        continuous = []
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(results)):
            monobits.append(results[i][0])
            pokers.append(results[i][1])
            runs.append(results[i][2])
            longruns.append(results[i][3])
            continuous.append(results[i][4])

        writer.writerow([path, it, monobits.count(True), pokers.count(True), runs.count(True), longruns.count(True), continuous.count(True)])
        csvfile.close()

    with open('results/fips_stats.csv', "a") as csvfile:
        monobits = []
        pokers = []
        runs = []
        longruns = []
        #cont = []
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(stats)):
            monobits.append(stats[i][0])
            pokers.append(stats[i][1])
            runs.append(stats[i][2])
            longruns.append(stats[i][3])
            #cont.append(results[i][4])

        writer.writerow([path, it, monobits, pokers, runs, longruns])
        csvfile.close()

def sp80022_csv(path, res):
    temp = []
    with open(res, 'r') as results:
        readfile = results.readlines()[7:]
        for line in readfile:
            temp.append(line.split()[10:])
        with open('results/sp80022_stats.csv', 'a') as out:
            writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([path, [[x[0] for x in temp if 'Frequency' in x],
                             [x[1] for x in temp if 'Frequency' in x]],
                             [[x[0] for x in temp if 'BlockFrequency' in x],
                             [x[1] for x in temp if 'BlockFrequency' in x]],
                             [[x[0] for x in temp if 'CumulativeSums' in x],
                             [x[1] for x in temp if 'CumulativeSums' in x]],
                             [[x[0] for x in temp if 'Runs' in x],
                             [x[1] for x in temp if 'Runs' in x]],
                             [[x[0] for x in temp if 'LongestRun' in x],
                             [x[1] for x in temp if 'LongestRun' in x]],
                             [[x[0] for x in temp if 'Rank' in x],
                             [x[1] for x in temp if 'Rank' in x]],
                             [[x[0] for x in temp if 'FFT' in x],
                             [x[1] for x in temp if 'FFT' in x]],
                             [[x[0] for x in temp if 'NonOverlappingTemplate' in x],
                             [x[1] for x in temp if 'NonOverlappingTemplate' in x]],
                             [[x[0] for x in temp if 'OverlappingTemplate' in x],
                             [x[1] for x in temp if 'OverlappingTemplate' in x]],
                             [[x[0] for x in temp if 'Universal' in x],
                             [x[1] for x in temp if 'Universal' in x]],
                             [[x[0] for x in temp if 'ApproximateEntropy' in x],
                             [x[1] for x in temp if 'ApproximateEntropy' in x]],
                             [[x[0] for x in temp if 'RandomExcursions' in x],
                             [x[1] for x in temp if 'RandomExcursions' in x]],
                             [[x[0] for x in temp if 'RandomExcursionsVariant' in x],
                             [x[1] for x in temp if 'RandomExcursionsVariant' in x]],
                             [[x[0] for x in temp if 'Serial' in x],
                             [x[1] for x in temp if 'Serial' in x]],
                             [[x[0] for x in temp if 'LinearComplexity' in x],
                             [x[1] for x in temp if 'LinearComplexity' in x]]])

# merges all csvs passed in as a list of csv names (default filenames only atm)
# returns single csv with individual files joined on file names with concatenated result columns


def csv_merge(a):
    return c
