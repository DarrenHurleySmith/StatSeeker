import csv
import os

HEADER_ENT = ['File name', 'Entropy', 'Chi-score', 'Serial Correlation', 'P-val Z', 'P-val Chi', 'Monte Carlo']
HEADER_FIPS = ['File name', 'Monobit', 'Poker', 'Run', 'Long run', 'Continuous']

ENT_CSV_PATH = 'results/ent_results.csv'
FIPS_RESULTS_CSV_PATH = 'results/fips_results.csv'
FIPS_STATS_CSV_PATH = 'results/fips_stats.csv'


def raiser(ex): raise ex


def dir_path(string):
    return string if os.path.isdir(string) else raiser(NotADirectoryError(string))


# take results of ent and returns csv of results
def ent_csv(paths, results):
    with open('results/ent_results.csv', "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_ENT)
        for i in range(len(paths)):
            entropy, chi_score, serial_correlation, p_val_z, p_val_chi, monte_carlo = results[i]
            writer.writerow([paths[i], entropy, chi_score, serial_correlation, p_val_z, p_val_chi, monte_carlo])
        csvfile.close()


# take results of ais-31 (non-fips) tests and returns csv of results
def ais_csv(r):
    return c


def aggregate_lists(data, index, num):
    aggregated = []
    for i in range(num):
        aggregated.append([])
        for j in range(len(data[index])):
            aggregated[i].append(data[index][j][i])
    return aggregated


# takes results  of fips140-2 and returns results csv
def fips_csv(paths, results, stats):
    csv_results = []
    csv_stats = []

    csv_results.append(aggregate_lists(results, 0, 5))
    csv_results.append(aggregate_lists(results, 1, 5))
    csv_results.append(aggregate_lists(results, 2, 5))
    csv_results.append(aggregate_lists(results, 3, 5))

    csv_stats.append(aggregate_lists(stats, 0, 4))
    csv_stats.append(aggregate_lists(stats, 1, 4))
    csv_stats.append(aggregate_lists(stats, 2, 4))
    csv_stats.append(aggregate_lists(stats, 3, 4))

    with open(FIPS_RESULTS_CSV_PATH, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_FIPS)
        for i in range(len(paths)):
            writer.writerow([paths[i], csv_results[i][0], csv_results[i][1], csv_results[i][2], csv_results[i][3], csv_results[i][4]])

    with open(FIPS_STATS_CSV_PATH, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(HEADER_FIPS)
        for i in range(len(paths)):
            writer.writerow([paths[i], csv_stats[i][0], csv_stats[i][1], csv_stats[i][2], csv_stats[i][3]])


# merges all csvs passed in as a list of csv names (default filenames only atm)
# returns single csv with individual files joined on file names with concatenated result columns
def csv_merge(a):
    return c
