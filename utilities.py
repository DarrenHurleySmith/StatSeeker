import csv
import os


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


# take results of ent and returns csv of results
def ent_csv(r):
    return c


# take results of ais-31 (non-fips) tests and returns csv of results
def ais_csv(r):
    return c


# take results of fips140-1 and returns csv of results
def fips1_csv(r):
    return c


# takes results  of fips140-2 and returns results csv
def fips2_csv(r):
    return c


# merges all csvs passed in as a list of csv names (default filenames only atm)
# returns single csv with individual files joined on file names with concatenated result columns
def csv_merge(a):
    return c