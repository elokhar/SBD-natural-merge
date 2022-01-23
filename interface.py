import sys
import os
from block_rw import read_record, write_record
from dbms import sort
import record as r


def run_interface(database, input_file=None):
    command=""
    test_file = None
    if(input_file==None):
        input_stream = sys.stdin
    else:
        input_stream = input_file
    while command!="quit":
        command = input_stream.readline().strip()
        match command:
            case "random":
                print("Enter number of random records to add:")
                number = int(input_stream.readline().strip())
                add_random_records(database, number)
                print("Added "+str(number)+" random records to database")
            case "add":
                print("Type records to add in a form: \"c m dT\", type \"end\" to end adding records:")
                record_str = input_stream.readline().strip()
                while(record_str!="end"):
                    record = record_from_string(record_str)
                    if(record!=None):
                        write_record(database, record)
                        print("Record added")
                    else:
                        print("Cannot add record, too few valid parameters")
                    record_str=input_stream.readline().strip()
                print("Exiting adding mode")
            case "test_file":
                print("Enter test file name with extension, leave empty to use test.txt:")
                filename = input_stream.readline().strip()
                if(filename==""):
                    filename="test.txt"
                if(os.path.isfile(filename)):
                    test_file = open(filename)
                    run_interface(database, test_file)
                    test_file.close()
                else:
                    print("No such file exists!")
    
            case "sort":
                sort(database)
            case "sort -p":
                sort(database, True)
            case "quit":
                if(input_file!=None):
                    print("End of test file parsing")
                else:
                    print("Exiting")
            case _:
                print("Invalid command used")
    
            
            
def record_from_string(record_str):
    parameters = []
    curr_parameter_str = ""
    record_str+=' '
    for character in record_str:
        if(character!=' '):
            curr_parameter_str+=character
        else:
            if(curr_parameter_str.isdigit()):
                parameters.append(int(curr_parameter_str))
                if(len(parameters)>=3):
                    break
            curr_parameter_str=""
    if(len(parameters)>=3):
        return r.record(parameters[0], parameters[1], parameters[2])      
    else:
        return None  

            

def add_random_records(file, records_number):
    records = r.createRandomRecords(records_number)
    for record in records:
        write_record(file, record)
