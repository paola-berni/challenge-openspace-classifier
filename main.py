from utils.file_utils import get_colleagues_list
from utils.openspace import Openspace
colleagues = get_colleagues_list()
#Load the list of colleagues from the configured data file
print(colleagues)

# Create an instance of the Openspace class with 6 tables and 4 seats per table
openspace1 = Openspace(6,4)
# assign a colleague randomly to a table 
openspace1.organize(colleagues)
# display assignments in the terminal
openspace1.display()