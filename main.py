from ast import For
import record as r
import block_rw as b


firstRecordsList = r.createRandomRecords(15)

file = open("file.dat", "w+b")

for record in firstRecordsList:
    file.write(bytes(record))
file.flush()
file.seek(0)

firstRecordsList.clear()

for i in range(15):
    print(b.read_record(file))
file.close()


