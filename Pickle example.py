import pickle

# Data to be pickled
data = {
    'name': 'Gunner Santana',
    'age': 31,
    'city': 'Seattle'
}

# Pickle the data
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Unpickle the data
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)