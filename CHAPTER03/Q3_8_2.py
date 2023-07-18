import pickle

with open("test1.pkl", "wb") as f:
    result = pickle.load(f)
    print(result)
