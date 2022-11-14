from functions import names_only, random_name_generator

file = "surnames.csv"
# file = "first_names.csv"
new_file = "surnames.txt"
index = 0
gender = "none"

# Use only to create the txt name lists
# names_only(file, new_file, index, gender)

boy_names = "boy_names.txt"
girl_names = "girl_names.txt"
last_name = "surnames.txt"

random_name_generator([boy_names, girl_names, last_name])