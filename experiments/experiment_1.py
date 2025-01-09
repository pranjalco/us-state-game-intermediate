import pandas

data = pandas.read_csv("../50_states.csv")
print(data)

data_dict = data.to_dict()
print("")
print(data_dict)






