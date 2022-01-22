from record import record as record
from block_rw import read_record, write_record, set_buffer_mode

def sort(file):
    set_buffer_mode(0, "write", file)
    set_buffer_mode(0, "read", file)
    tape1 = open("tape1.dat", "w+b")
    tape2 = open("tape2.dat", "w+b")
    tape3 = open("tape3.dat", "w+b")
    distribute(file, tape1, tape2)
    tape1.close()
    tape2.close()
    tape3.close()
    set_buffer_mode(0, "write", file)
    set_buffer_mode(0, "read", file)



def distribute(src_tape, dest_tape_1, dest_tape_2):
    curr_record = read_record(src_tape)
    next_record = read_record(src_tape)
    dest_tapes = [dest_tape_1, dest_tape_2]
    dest_tape_number = 0
    if(curr_record!=None and next_record!=None):

        dest_tape = dest_tapes[dest_tape_number]
        write_record(dest_tape, curr_record)
        while(next_record!=None):            
            curr_key = curr_record.getKey()
            next_key = next_record.getKey()
            run_end = check_run_end(curr_key, next_key)
            if(run_end):
                #alternate destination tape
                dest_tape_number = (dest_tape_number+1)%2
                dest_tape = dest_tapes[dest_tape_number]
            curr_record = next_record
            next_record = read_record(src_tape)
            write_record(dest_tape, curr_record)
    pass

def check_run_end(curr_key, next_key):
    if curr_key <= next_key:
        return False
    else:
        return True

    
    
    