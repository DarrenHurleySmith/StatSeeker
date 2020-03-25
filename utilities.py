import csv
import os
import pandas as pd
from scipy import stats
import ast
from fractions import Fraction

HEADER_ent = ['File name', 'Entropy', 'Chi-score', 'Serial Correlation', 'P-val Chi', 'Monte Carlo']
HEADER_fips = ['File name', 'Iterations', 'Monobit', 'Poker', 'Run', 'Long run', 'Continuous']
HEADER_ais31 = ['File name', 'T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6a', 'T6b', 'T7a_1', 'T7a_2', 'T7b_1', 'T7b_2', 'T7b_3', 'T7b_4', 'T8']
HEADER_sp80022 = ['File name', 'Frequency', 'Block Frequency', 'Cumulative Sums', 'Runs', 'Longest Run', 'Rank', 'FFT',
                  'NonOverlapping Template', 'Overlapping Template', 'Universal', 'Approximate Entropy',
                  'Random Excursions', 'Random Excursions Variant', 'Serial', 'Linear Complexity']
HEADER_fileinfo = ['File name', 'size']


def init_csv():
    with open('results/fileinfo.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_fileinfo)

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


def file_info(path, size):
    with open('results/fileinfo.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([path, size])


# take results of ent and returns csv of results
def ent_csv(path, results):
    with open('results/ent_results.csv', "a") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        entropy, chi_score, serial_correlation, p_val_chi, monte_carlo = results
        writer.writerow([path, entropy, chi_score, serial_correlation, p_val_chi, monte_carlo])
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
            #print(temp)
        with open('results/sp80022_stats.csv', 'a') as out:
            writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # p-values in x[0], proportion passed in x[1]
            # * indicates a failure
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


def csv_merge():
    x = pd.read_csv('results/fileinfo.csv')
    a = pd.read_csv('results/ent_results.csv')
    b = pd.read_csv('results/fips_stats.csv')
    c = pd.read_csv('results/sp80022_stats.csv')

    a = a.dropna(axis=1)
    b = b.dropna(axis=1)
    c = c.dropna(axis=1)

    merged = x.merge(a, on='File name')
    merged = merged.merge(b, on='File name')
    merged = merged.merge(c, on='File name')

    merged.to_csv("results/statistics.csv", index=False)

#suppress scientific notation
def supNot(x):
    x = '{:.12f}'.format(float(x))
    return x

def devectorise(d):
    out = []
    header = []

    # add header
    header.append(HEADER_ent[0])
    header.append('Size')

    for item in HEADER_ent[1:-2]:
        header.append(item)

    header.append('P-val Z')

    for item in HEADER_ent[-2:]:
        header.append(item)

    for item in HEADER_fips[1:-1]:
        header.append(item)

    for item in HEADER_sp80022[1:]:
        header.append(item + '_pvalue')
        header.append(item + '_proportion')

    out.append(header)

    with open(d+'fips_results.csv', 'r') as r:
        rread = csv.reader(r, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fips_res = list(rread)

    with open(d+'statistics.csv', 'r') as s:
        sread = csv.reader(s, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        all_stats = list(sread)

    for i in range(1, len(all_stats)):
        line = []

        # add all elements which aren't already vectors
        line.append(all_stats[i][0])

        for item in all_stats[i][1:9]:
            #line.append(float(item))
            line.append(supNot(item))

        # devectorise monobits
        line.append(supNot(int(fips_res[i][2])/int(all_stats[i][8])))
        # devectorise poker
        line.append(supNot(int(fips_res[i][3]) / int(all_stats[i][8])))
        # devectorise run
        line.append(supNot(int(fips_res[i][4]) / int(all_stats[i][8])))
        # devectorise long run
        line.append(supNot(int(fips_res[i][4]) / int(all_stats[i][8])))
        # devectorise continuous - to be added later
        #line.append(int(fips_res[i][5]) / int(all_stats[i][8]))

        # split all elements which are sp800-22 results into p-value and proportion results (max 28)
        for item in all_stats[i][13:28]:
            item = ast.literal_eval(item)
            #print(item)
            #unpacked vectorised sp800-22 test results
            if type(item[0]) is list:
                # check if results exist and use fisher's method to aggregate them
                #print(item[0][0])
                if item[0][0] != '----':
                    if len(item[0]) > 1:
                        agg_elem = []
                        for elem in item[0]:
                            if float(elem) > 0:
                                agg_elem.append(float(elem))

                        #print(stats.kstest(agg_elem, 'norm'))
                        #print(len(agg_elem))
                        line.append(supNot(stats.combine_pvalues(agg_elem, method='fisher', weights=None)[1]))

                        #if stats.combine_pvalues(agg_elem, method='fisher', weights=None)[1] == 0:
                            #print(item[0])

                    #if not list of lists, just pull out the result and add to list
                    else:
                        line.append(supNot(item[0][0]))
                else:
                    line.append('')

            #perform the same checks for the proportion tests
            if type(item[1]) is list:
                if '-' not in item[1][0]:
                    for j in range(0, len(item[1])):
                        if item[1][j] == '*':
                            item[1][j] = '0/1'
                    line.append(supNot(float(sum(Fraction(s) for s in item[1]))/len(item[1])))
                #account for any test failures and show '*' where proportion tests fail
                else:
                    line.append('')

        #print(line)
        out.append(line)

    with open(d + 'statistics_devectorised.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for line in out:
            writer.writerow(line)
