from record import record
from block_rw import read_record

def print_file(file):
    record = read_record(file)
    while(record != None):
        print(record)
        record = read_record(file)