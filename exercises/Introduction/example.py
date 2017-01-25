import datetime

r"""
This script creats an example file.
"""

filename = datetime.datetime.now()

#Create empty file
def create_file():
    """This function creates an empty file"""
    with open(filename.strftime("%Y-%m-%d")+".txt","w") as file:
        file.write("") #Writing empty string

create_file()