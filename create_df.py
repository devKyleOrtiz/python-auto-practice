import pandas as pd 
#this is the import for pandas library and giving the alias of pd for less code

#creating a list of values for the dataframe, which is a 2 dimensional representation of data. A table, bassically
col_1 = ["red","blue","brown","black","yellow","green","orange","purple"]

#calling the data frame method from the pd(pandas) library and passing it col_1, created var to store this df
data_frame = pd.DataFrame(col_1)

#printing the new data frame
print(data_frame)