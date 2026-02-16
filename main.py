from utils.file_utils import get_colleagues_list
from utils.openspace import Openspace
colleagues = get_colleagues_list()
#Load the list of colleagues from the configured data file
print(colleagues)

openspace1 = Openspace(6,4)
openspace1.organize(colleagues)
openspace1.display()