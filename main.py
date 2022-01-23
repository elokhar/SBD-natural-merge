import dbms
import record as r
import block_rw as b
import interface as i
from block_rw import read_record, write_record

database = open("database.dat", "w+b")

RANDOM_RECORDS_NUMBER = 22

i.add_random_records(database, RANDOM_RECORDS_NUMBER)

# write_record(tape1, r.record(4,5,6))

# record = read_record(database)

# write_record(database,r.record(1,2,3))



dbms.sort(database)








# print("tape1:")
# print(read_record(tape1))

database.close()



