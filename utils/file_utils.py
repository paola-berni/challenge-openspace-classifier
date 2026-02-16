import csv
def get_colleagues_list():

    with open (r"C:\Users\Defree\Documents\Project\challenge-openspace-classifier\utils\data\new_colleagues.csv", mode="r") as file:
        csv_file = csv.reader(file)
        colleagues = [row[0] for row in csv_file]
        return colleagues

 
 
