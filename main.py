import record as r
import block_rw as b
from block_rw import read_record, write_record

RECORDS_NUMBER = 3

firstRecordsList = r.createRandomRecords(RECORDS_NUMBER)

database = open("database.dat", "a+b")
test1 = open("test1.dat", "a+b")
database.truncate(0)
test1.truncate(0)

for record in firstRecordsList:
    write_record(database, record)
database.flush()
firstRecordsList.clear()

write_record(test1, r.record(4,5,6), 1)

record = read_record(database)

write_record(database,r.record(1,2,3))

record = read_record(database)
while(record.getKey() != 0):
    print(record)
    record = read_record(database)

print("test1:")
print(read_record(test1, 1))

database.close()
test1.close()


