import pandas as pd

df = pd.read_csv("FastFoodRestaurants.csv")

<<<<<<< HEAD
print(df)
=======
# print out the entire data
print(df)

>>>>>>> 8462ba2ae3213ca7f10ca2e27955b6e809f6ab01
# prints out the header of the data set
#print(df.keys())

# outputs first 5 in the data
#df.head(5)

# outputs last 10 in the data
#df.tail(10)

# sorts the data by state
#df.sort_values('province')

# outputs all the Subways in New York City, NY
#df[df['city'] == "New York"][df['name'] == "Subway"][df['province'] == "NY"]

# outputs all the Mcdonald's in the US
#df[df['name'] == "McDonald's"]
