import dbms
import record as r
import block_rw as b
import util as u
from block_rw import read_record, write_record

RECORDS_NUMBER = 7

firstRecordsList = r.createRandomRecords(RECORDS_NUMBER)

database = open("database.dat", "w+b")


for record in firstRecordsList:
    write_record(database, record)
database.flush()
firstRecordsList.clear()

# write_record(tape1, r.record(4,5,6))

# record = read_record(database)

# write_record(database,r.record(1,2,3))

u.print_file(database)

dbms.sort(database)







# print("tape1:")
# print(read_record(tape1))

database.close()



