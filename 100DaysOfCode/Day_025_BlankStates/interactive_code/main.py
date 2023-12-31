# with open("weather_data.csv") as weather_data:
#     weather = weather_data.readlines()
# print(weather)

# import csv 

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
    

import pandas as pd 


# data = pd.read_csv("weather_data.csv")
# # data_list = data["temp"].to_list()

# # average = data["temp"].mean()

# max_temp = data["temp"].max()

# print(data[data.temp == max_temp])

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data['Primary Fur Color']
gray = len(data[fur_data == "Gray"])
cinnamon = len(data[fur_data == "Cinnamon"])
black = len(data[fur_data == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"], 
    "Count": [gray, cinnamon, black]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count_csv.csv")