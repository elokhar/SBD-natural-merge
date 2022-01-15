import record as r
import block_rw as b


firstRecordsList = r.createRandomRecords(15)


file = open("file.dat", "wb")

for record in firstRecordsList:
    file.write(bytes(record))
file.close()

firstRecordsList.clear()

print(b.read_record("file.dat"))
print(b.read_record("file.dat"))
print(b.read_record("file.dat"))
print(b.read_record("file.dat"))
print(b.read_record("file.dat"))

print(b.read_record("file.dat"))


