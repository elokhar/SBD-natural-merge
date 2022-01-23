from record import record as record
from block_rw import read_record, start_reading_from_beginning, write_record
from interface import print_file

def sort(file, show_phases=False):
    print()
    print("File before sorting:")
    start_reading_from_beginning(file)
    print_file(file)
    print("Sorting file...")
    file_sorted = False
    phase_number = 0

    start_reading_from_beginning(file)
    tape1 = open("tape1.dat", "w+b")
    tape2 = open("tape2.dat", "w+b")
    while(file_sorted==False):
        

        distribute(file, tape1, tape2)

        file_sorted = merge(tape1, tape2, file)

        start_reading_from_beginning(tape1)
        start_reading_from_beginning(tape2)

        if(file_sorted==False):
            phase_number+=1
            if(show_phases==True):
                print()          
                print("Phase "+str(phase_number)+":")
                print("Tape 1:")
                print_file(tape1)
                print("Tape 2:")
                print_file(tape2)
                print("Tape 3:")
                print_file(file)        
                start_reading_from_beginning(tape1)
                start_reading_from_beginning(tape2)
                start_reading_from_beginning(file)
            

            
        
            

        

    print()    
    print("File sorted")
    print("File after sorting:")
    start_reading_from_beginning(file)
    print_file(file)
    print("Number of phases: "+str(phase_number))
    

    tape1.close()
    tape2.close()
    start_reading_from_beginning(file)



def distribute(src_tape, dest_tape_1, dest_tape_2):
    dest_tape_1.truncate(0)
    dest_tape_1.seek(0)
    dest_tape_2.truncate(0)
    dest_tape_2.seek(0)
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

def merge(src_tape_1, src_tape_2, dest_tape):
    
    record1 = read_record(src_tape_1)
    record2 = read_record(src_tape_2)
    if(record1==None or record2==None):
        file_sorted = True
    else:
        file_sorted = False
        dest_tape.truncate(0)
        dest_tape.seek(0)
        while(record1!=None or record2!=None):
            if(record2==None):
                write_record(dest_tape, record1)
                record1 = read_record(src_tape_1)
            elif(record1==None):
                write_record(dest_tape, record2)
                record2 = read_record(src_tape_2)
            elif(record1.getKey()<record2.getKey()):
                write_record(dest_tape, record1)
                record1 = read_record(src_tape_1)
            else:
                write_record(dest_tape, record2)
                record2 = read_record(src_tape_2)
    return file_sorted

    

def check_run_end(curr_key, next_key):
    if curr_key <= next_key:
        return False
    else:
        return True

    
    
    