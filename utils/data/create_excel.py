import pandas as pd

# Define the data
new_colleagues = ["Aleksei", "Amine", "Anna", "Astha", "Brigitta",
                  "Bryan", "Ena", "Esra", "Faranges", "Frédéric",
                  "Hamideh", "Héloïse", "Imran", "Intan K.",
                  "Jens", "Kristin", "Michiel", "Nancy", "Pierrick",
                  "Sandrine", "Tim", "Viktor", "Welederufeal", "Živile"]

# Create a list of dictionaries to represent the data
colleague_list = [{"name": name} for name in new_colleagues]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(colleague_list)
# pd pandas
# df dataframe

# Ensure the 'data' folder exists
df.to_excel("colleagues.xlsx", index=False)

print("Excel file created successfully in 'data/' folder!")
