# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Gunner Santana ,08/19/2023,Created Script
# ------------------------------------------------- #
import pickle

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, data):
    objFile = open(file_name, "ab")
    pickle.dump(data, objFile)  # Swap the arguments: data first, then file object
    objFile.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    data = pickle.load(file)
    file.close()
    return data

# Presentation ------------------------------------ #
intId = int(input("Enter an Id: "))
strName = input("Enter a Name: ")
lstCustomer = [intId, strName]

# Save the list object into a binary file
save_data_to_file(strFileName, lstCustomer)

# Read the data from the file into a new list object and display the contents
loaded_data = read_data_from_file(strFileName)
print("Loaded Data:", loaded_data)