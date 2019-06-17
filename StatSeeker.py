import argparse
import sys
import glob
import os
from batteries import ent
from utilities import dir_path, ent_csv


def main(argv):
    opts = argparse.ArgumentParser(prog='StatSeeker', description=__doc__)

    opts.add_argument('-a', action='store_true', help="run all test batteries")
    opts.add_argument('-v', '--version', action='version', version="0.1")
    opts.add_argument("--path", type=dir_path, help="one or more files to process")

    args = opts.parse_args()
    f = []
    e = []

    for root, dir, files in os.walk(args.path):
        for file in files:
            fs = os.stat(root+file)
            if fs.st_size >= 1024:
                f.append(root+file)
                e.append(ent(root+file))


    # print(f)
    # print(e)
    ent_csv(f, e)


if __name__ == '__main__':
    main(sys.argv[1:])