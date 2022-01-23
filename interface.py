from block_rw import read_record, write_record
import record as r

def print_file(file):
    record = read_record(file)
    while(record != None):
        print(record)
        record = read_record(file)

def add_random_records(file, records_number):
    records = r.createRandomRecords(records_number)
    for record in records:
        write_record(file, record)
