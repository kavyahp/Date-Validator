
from datetime import datetime #database that is used to validate input

while(True):
    try:
        Date = input("Enter Date yyyymmdd: ")
        datetime = datetime.strptime(Date, '%Y%m%d')   # it converts the input into the format used by dataset
        if len(Date) != 8: # checks if there are 8 characters as input should have 8 characters
            raise Exception
        else:
            break    # To end loop
    except:
        print("INVALID Date: ",Date)

print("Valid Date Has Been Entered: ",Date)