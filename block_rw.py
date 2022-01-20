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

records_list = []   #the buffer for reading and writing

def read_block(data_file):
    file = data_file
    record_bytes = file.read(r.RECORD_SIZE)
    
    if(record_bytes==0): #if there is no more data to read, the function returns reads nothing and returns False
        return False
    else:
        records_list.append(r.record.from_bytes(record_bytes))
        for i in range(r.RECORD_SIZE,BLOCK_SIZE,r.RECORD_SIZE):
            record_bytes = file.read(r.RECORD_SIZE)
            if(record_bytes==0): 
                break               #stop reading if end of file has been reached
            records_list.append(r.record.from_bytes(record_bytes))
        return True

def write_block(data_file):
    file = data_file
    for record in records_list:
        file.write(bytes(record))
    

def read_record(data_file):
    if records_list:
        return records_list.pop(0)
    else:                                   # if buffer is empty, place next block from file into it
        if(read_block(data_file)):          # if read_block placed at least one record into the buffer
            return read_record(data_file)   # read the first record from the buffer
        else:                               # if read_block didn't read antything, return false
            return False

def write_record(data_file, record):
    if len(records_list) < BLOCK_SIZE:
        records_list.append(record)
    else:
        write_block(data_file)
        write_record(data_file, record)



        
        


    

