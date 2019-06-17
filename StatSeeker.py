import argparse
import os
from batteries import ent
from utilities import dir_path, ent_csv


def main():
    opts = argparse.ArgumentParser(prog='StatSeeker', description=__doc__)

    opts.add_argument('-a', action='store_true', help="run all test batteries")
    opts.add_argument('-v', '--version', action='version', version="0.1")
    opts.add_argument("--path", type=dir_path, help="one or more files to process")

    args = opts.parse_args()

    file_names = []
    ent_results = []
    for root, dir, files in os.walk(args.path):
        for file in files:
            path = os.path.join(root, file)
            fs = os.stat(path)
            if fs.st_size >= 1024:
                file_names.append(path)
                ent_results.append(ent(path))

    # print(file_names)
    # print(ent_results)
    ent_csv(file_names, ent_results)


if __name__ == '__main__':
    main()
