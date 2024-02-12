from Bio import SeqIO
import csv
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='original CSV file')
parser.add_argument('CSV_file', type=str, help='enter name of trimmed CSV file containing sequences to look for')
parser.add_argument('trinity_db', type=str, help="enter name of trinity database fasta file" )
parser.add_argument('final_fasta_file', type=str, help="enter name of output fasta file")
args = parser.parse_args()

trimmed_CSV_filename = args.CSV_file
trinity_db_name = args.trinity_db
final_fasta_filename = args.final_fasta_file

# trimmed_CSV_folder = Path("/Users/alanwang/Desktop/Wadsworth (Summer 2023)/salp20 local blast trimmed CSV files")
# trinity_databases_folder = Path("/Users/alanwang/Desktop/Wadsworth (Summer 2023)/salp20 trinity databases")
# final_fasta_folder = Path("/Users/alanwang/Desktop/Wadsworth (Summer 2023)/salp20 final fasta")

# trimmed_CSV_folder /
with open(trimmed_CSV_filename, 'r') as trim_file:
    csv_reader = csv.reader(trim_file)

    seq = []
    for line in csv_reader:
        # get the trinity id from CSV file
        trinity_id = str(line[1])

# trinity_databases_folder /
        for seq_record in SeqIO.parse(trinity_db_name, "fasta"):
            if trinity_id in seq_record.id:
                seq.append(seq_record)

# final_fasta_folder /
    SeqIO.write(seq, final_fasta_filename, "fasta")


