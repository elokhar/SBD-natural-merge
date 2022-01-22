import record as r

BLOCK_LENGTH = 1    #number of records in one block
BLOCK_SIZE = r.RECORD_SIZE*BLOCK_LENGTH     #block size in bytes
NUMBER_OF_BUFFERS = 4

#records_list = []   #the buffer for reading and writing
buffers = [ [] for _ in range(NUMBER_OF_BUFFERS) ]
buffers_modes = [ "read" for _ in range(NUMBER_OF_BUFFERS) ]

def read_record(data_file):
    buffer_number = select_buffer_number(data_file)
    set_buffer_mode(buffer_number, "read", data_file)
    records_list = buffers[buffer_number]
    if records_list:                                         #if buffer is not empty, pop the first record from it
        return records_list.pop(0)
    else:                                                    # if buffer is empty, place next block from file into it
        if(read_block_to_buffer(data_file, buffer_number)):  # if read_block_to_buffer placed at least one record into the buffer
            return read_record(data_file)     # read the first record from the buffer
        else:                                                # if read_block_to_buffer didn't read antything, return False
            return None

def write_record(data_file, record):
    buffer_number = select_buffer_number(data_file)
    set_buffer_mode(buffer_number, "write", data_file)
    records_list = buffers[buffer_number]
    if len(records_list) < BLOCK_LENGTH:
        records_list.append(record)
    else:
        write_buffer_to_file(data_file, buffer_number)
        write_record(data_file, record)

def read_block_to_buffer(data_file, buffer_number):
    records_list = buffers[buffer_number]
    file = data_file
    record_bytes = file.read(r.RECORD_SIZE)
    
    if(record_bytes==b''): #if there is no more data to read, the function returns reads nothing and returns False
        return False
    else:
        records_list.append(r.record.from_bytes(record_bytes))
        for i in range(r.RECORD_SIZE,BLOCK_SIZE,r.RECORD_SIZE):
            record_bytes = file.read(r.RECORD_SIZE)
            if(record_bytes==b''): 
                break               #stop reading if end of file has been reached
            records_list.append(r.record.from_bytes(record_bytes))
        return True

def write_buffer_to_file(data_file, buffer_number):
    records_list = buffers[buffer_number]
    file = data_file
    for record in records_list:
        file.write(bytes(record))
    file.flush()
    records_list.clear()

def set_buffer_mode(buffer_number, mode, file):
    if(buffers_modes[buffer_number]==mode):
        pass
    else:
        if(mode=="read"):   #if mode changed to "read"
            write_buffer_to_file(file, buffer_number)
            file.seek(0)        #move file cursor to the beginning of the file
            buffers[buffer_number].clear()
            buffers_modes[buffer_number] = mode
        elif(mode=="write"):  #if mode changed to "write"
            file.seek(0,2)      #move file cursor to the end of the file
            buffers[buffer_number].clear()
            buffers_modes[buffer_number] = mode
        else:
            print("Incorrect buffer mode")

def select_buffer_number(file):
    file_name_no_ext = file.name[:-4]
    match file_name_no_ext:
        case "database":
            buffer_number=0
        case "tape1":
            buffer_number=1
        case "tape2":
            buffer_number=2
        case "tape3":
            buffer_number=3
        case _:
            buffer_number=-1

    assert buffer_number!=-1, "Wrong filename used, cannot assign buffer!"

    return buffer_number





        
        


    

