import dbms
import record as r
import block_rw as b
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


record = read_record(database)
while(record != None):
    print(record)
    record = read_record(database)

dbms.sort(database)

print("tape1:")
tape1 = open("tape1.dat", "a+b")
tape1.seek(0)
record = read_record(tape1)
while(record != None):
    print(record)
    record = read_record(tape1)
tape1.close()

print("tape2:")
tape2 = open("tape2.dat", "a+b")
tape2.seek(0)
record = read_record(tape2)
while(record != None):
    print(record)
    record = read_record(tape2)
tape2.close()

print("also database:")
record = read_record(database)
while(record != None):
    print(record)
    record = read_record(database)






# print("tape1:")
# print(read_record(tape1))

database.close()



