# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple example of pickling and structured error handling
# ChangeLog: (Who, When, What)
# Gunner Santana ,08/19/2023,Created Script
# ------------------------------------------------- #

import pickle

# Define a sample data structure
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'Seattle'
}

# Pickling: Writing data to a file using pickle
def save_data_to_file(filename, data):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
            print(f"Data saved to '{filename}' successfully.")
    except IOError as e:
        print(f"Error saving data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Unpickling: Reading data from a file using pickle
def load_data_from_file(filename):
    try:
        with open(filename, 'rb') as file: # reads binary file
            loaded_data = pickle.load(file)
            print("Loaded data:", loaded_data)
    except FileNotFoundError:
        print(f"'{filename}' not found.")
    except pickle.PickleError as pe:
        print(f"Error loading data: {pe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Demonstrate pickling and structured error handling
if __name__ == "__main__":
    filename = "data.pkl"

    # Saving data to a file
    save_data_to_file(filename, data)

    # Loading data from a file
    load_data_from_file(filename)
(input("Want a pickle?"))






