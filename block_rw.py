import record as r

# def block_read(filename):
#     records_list = []
#     file = open(filename, "rb")
#     record_bytes = file.read(rec.INT_SIZE*3)
#     while record_bytes:
#         records_list.append(rec.record.from_bytes(record_bytes))
#         record_bytes = file.read(rec.INT_SIZE*3)
#     file.close()
#     return records_list

BLOCK_SIZE = r.RECORD_SIZE*5

records_list = []

def read_block(data_file):
    file = data_file
    record_bytes = file.read(r.RECORD_SIZE)
    records_list.append(r.record.from_bytes(record_bytes))
    if(record_bytes==0): #if there is no more data to read, return False
        file.close()
        return False
    for i in range(r.RECORD_SIZE,BLOCK_SIZE,r.RECORD_SIZE):
        record_bytes = file.read(r.RECORD_SIZE)
        if(record_bytes==0):
            break
        records_list.append(r.record.from_bytes(record_bytes))
    return True

def write_block(data_file, record):
    file = data_file
    

def read_record(data_file):
    if records_list:
        return records_list.pop(0)
    else:
        if(read_block(data_file)):
            return read_record(data_file)
        else:
            return False

def write_record(data_file, record):
    if len(records_list) < BLOCK_SIZE:
        records_list.append(record)
    else:
        write_block(data_file, record)


        
        


    

