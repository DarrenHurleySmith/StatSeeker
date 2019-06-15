import argparse
import sys
import glob, os
from batteries import ent
from utilities import dir_path, ent_csv


def main(argv):
    opts = argparse.ArgumentParser(prog='StatSeeker', description=__doc__)

    opts.add_argument('-a', action='store_true', help="run all test batteries")
    opts.add_argument('-v', '--version', action='version', version="0.1")
    opts.add_argument("--path", type=dir_path, help="one or more files to process")

    args = opts.parse_args()

    os.chdir(args.path)

    ent_results = []
    files = []

    for file in glob.glob("*.*"):
        fs = os.stat(file)
        if fs.st_size >= 1024:
            files.append(file)
            ent_results.append(ent(file))

    e_csv = ent_csv(ent_results)

    print(files)
    print(ent_results)


if __name__ == '__main__':
    main(sys.argv[1:])