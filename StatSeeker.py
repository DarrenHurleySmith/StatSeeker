import argparse
import os
from batteries import ent, fips140, ais31
from utilities import dir_path, init_csv, ent_csv, fips_csv, ais_csv, sp80022_csv, file_info, csv_merge, devectorise

def main():
    opts = argparse.ArgumentParser(prog='StatSeeker', description=__doc__)

    opts.add_argument('-a', action='store_true', help="run all test batteries")
    opts.add_argument('-v', '--version', action='version', version="0.1")
    opts.add_argument("--path", type=dir_path, help="one or more files to process")
    opts.add_argument('-d', action='store_true', help="devectorise statistics files")

    args = opts.parse_args()
    print(args)

    file_names = []
    #ent_results = []
    #fips2results = []
    #fips2stats = []
    #ais31results = []

    if args.path is not '':

        if args.a == True:
            init_csv()

            for root, dir, files in os.walk(args.path):
                for file in files:
                    path = os.path.join(root, file)
                    fs = os.stat(path)

                    size = 50000  # defeault 1024000
                    num_runs = 10  # ideally >10, more is better

                    print(path)

                    if fs.st_size >= (size*num_runs)/8:
                        file_names.append(path)

                        file_info(path, fs.st_size)

                        ent_results = ent(path)
                        ent_csv(path, ent_results)
                        print('ent')

                        r, c, i = fips140(path, 2, 1000)
                        fips2results = r
                        fips2stats = c
                        fips_csv(path, fips2results, fips2stats, i)
                        print('fips2')

                        # ais31 disabled until autocorrelation test can be fixed and optimisations made
                        #ais31results = ais31(path)
                        #if 'Nan' not in ais31results:
                        #    ais_csv(path, ais31results)
                        #print('ais31')

                        if int(fs.st_size/(size/8)) < 10:
                            num_runs = int(fs.st_size/(size/8))

                        print(num_runs)

                        os.system('sudo bash ./sts_testscript.bash ' + str(path) + ' ' + str(size) + ' ' + str(num_runs) + ' > /dev/null')
                        sp80022_csv(path, 'sts-2.1.2/experiments/AlgorithmTesting/finalAnalysisReport.txt')
                        print('sp800-22')

                        #add sp800-90B - figure out if it is possible to reduce the minimum file size

            #merge csvs
            csv_merge()

        if args.d == True:
            devectorise(args.path)

if __name__ == '__main__':
    main()
