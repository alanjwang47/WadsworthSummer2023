import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='original CSV file')
parser.add_argument('CSV_file', type=str, help='enter name of CSV file to be trimmed')
args = parser.parse_args()

raw_CSV_filename = args.CSV_file
period = raw_CSV_filename.index('.')
s1 = raw_CSV_filename[0:period]
s2 = raw_CSV_filename[period:]
trimmed_CSV_filename = s1 + "_trimmed" + s2

# raw_CSV_folder = Path("/Users/alanwang/Desktop/Wadsworth (Summer 2023)/salp20 local blasts raw CSV/")
# trimmed_CSV_folder = Path("/Users/alanwang/Desktop/Wadsworth (Summer 2023)/salp20 local blast trimmed CSV files")

# raw_CSV_folder /
with open(raw_CSV_filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # trimmed_CSV_folder /
    with open(trimmed_CSV_filename, 'w', newline="") as new_file:
        csv_writer = csv.writer(new_file)

        # Initialize dictionary where key is subject acc.ver (trinity ID) and value is string list (each line in
        # CSV file is a string list)
        id_dict = {}

        for line in csv_reader:
            # index subject acc. ver
            subject_acc_ver = line[1]

            # if id not already in dictionary, add it and its corresponding line.
            if subject_acc_ver not in id_dict:
                id_dict[subject_acc_ver] = line

            # else either keep the old line or replace with new one based on alignment length, and if needed, evalue
            else:
                old_line = id_dict[subject_acc_ver]

                old_align_len = float(old_line[3])
                new_align_len = float(line[3])

                old_evalue = float(old_line[10])
                new_evalue = float(line[10])

                if new_align_len > old_align_len:
                    id_dict[subject_acc_ver] = line

                if new_align_len == old_align_len:
                    if new_evalue < old_evalue:
                        id_dict[subject_acc_ver] = line

        line_list = list(id_dict.values())

        fieldnames = ['query acc.ver', 'subject acc.ver', '% identity', 'alignment length', 'mismatches', 'gap opens',
                      'q. start', 'q. end', 's. start', 's. end', 'evalue', 'bit score', '% query coverage per subject']

        csv_writer.writerow(fieldnames)
        csv_writer.writerows(line_list)
