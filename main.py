from ast import For
import record as r
import block_rw as b

RECORDS_NUMBER = 13

firstRecordsList = r.createRandomRecords(RECORDS_NUMBER)

file = open("file.dat", "w+b")

for record in firstRecordsList:
    b.write_record(file, record)
file.flush()
file.seek(0)

firstRecordsList.clear()

for i in range(RECORDS_NUMBER):
    print(b.read_record(file))
file.close()


