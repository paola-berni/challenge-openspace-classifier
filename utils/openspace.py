import random
import pandas as pd

from utils.table import Table
# import Table from utils.table:
# This import statement allows you to use the Table class defined in the utils.table module
# in your current code. By importing Table, you can create instances of the Table class and
# call its methods to manage seating arrangements in the Openspace class.

class Openspace:
# 1) __init__(self, number_of_tables, table_capacity) method:
# This is the constructor for the Openspace class, which gets called when you create a new 
# Openspace object.
# number_of_tables: This parameter specifies how many tables the openspace will have.
# table_capacity: This parameter specifies how many seats each table can accommodate.
# self.tables: This creates a list of Table objects, where each Table is initialized with
# the specified table_capacity. The number of tables is equal to number_of_tables.

    def __init__(self, number_of_tables, table_capacity):
        self.number_of_tables = number_of_tables
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
  # 2) organize(self, names) method:  
# This method takes a list of names and randomly assigns them to tables in the openspace.
# random.shuffle(names): This function randomly shuffles the order of the names in the list
# to ensure that the seating arrangement is different each time you run the code.
# The method then iterates through each name and tries to assign it to a seat
# at one of the tables. If a table has a free seat, it assigns the name to that seat 
# and breaks out of the loop to move on to the next name.
# SUMMARY: 
# So, the organize method ensures that each person from the shuffled list is seated at 
# a table. It tries to assign people to tables until there are no more free seats left.
    def organize(self, names):
        random.shuffle(names)  # Shuffle the names to randomly assign people to tables
        for name in names:
            for table in self.tables:
                if table.assign_seat(name):
                    break
   #3) display(self) method:
# This method displays the current seating arrangement in the openspace.
# It iterates through each table and prints out the status of each seat, indicating
# whether it is occupied and by whom, or if it is empty.
    def display(self):
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                print(f"  Seat: {'Occupied by ' + seat.occupant if not seat.free else 'Empty'}")
    #4) store(self, filename) method:
# This method saves the current seating arrangement to an Excel file.
# It prepares the data in a format suitable for Excel, where each row contains the table
# number, seat number, and occupant name.
# It uses the pandas library to create a DataFrame from the data and then saves it to an
# Excel file.

#store(self, filename) is a method to save the seating arrangement to an Excel file.
# Inside the store method:
# data = []: #Creates an empty list to store the data for each seat.
# for i, table in enumerate(self.tables, 1)::
#Loops through each table, using enumerate to get a 1-based index i.
#for idx, seat in enumerate(table.seats, 1)::
#Loops through each seat in the current table's seats.
# data.append({...}):
# For each seat, we create a dictionary with:
# 'Table': The table number.
# 'Seat': The seat number.
#'Occupant': The name of the person occupying the seat, or 'Empty' if the seat is free.
# df = pd.DataFrame(data):
# Converts the data list (which is a list of dictionaries) into a Pandas DataFrame.
# Pandas DataFrames are like tables in Python, making it easier to handle and save tabular
# data.
# df.to_excel(filename, index=False):
# This saves the DataFrame to an Excel file with the name specified by filename.
# The index=False argument ensures that row indices are not included in the Excel file.
    def store(self, filename):
        # Prepare data for Excel
        data = []
        for i, table in enumerate(self.tables, 1):
            for idx, seat in enumerate(table.seats, 1):
                data.append({
                    'Table': i,
                    'Seat': idx,
                    'Occupant': seat.occupant if not seat.free else 'Empty'
                })
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

#SUMMARY: Openspace Class Methods:
# __init__: Initializes the Openspace with a specified number of tables and seats.
# organize: Randomly assigns people to available seats at the tables.
# display: Prints the seating arrangement to the console.
# store: Saves the seating arrangement in an Excel file.
