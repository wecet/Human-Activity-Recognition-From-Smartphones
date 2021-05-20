#%%
import pandas as pd
import csv

#%%
file = pd.read_csv("test.csv")
duplicates = file[file.duplicated()]
print("Size of File with Duplicates: \n", len(file))
#print("\nDuplicate Rows: \n {}".format(duplicates))

##REMOVED IS THE VARIABLE THAT STORES THE DATA SET WITHOUT DUPLICATES
removed = file.drop_duplicates(keep='last')
print("Size of File after Removal of Duplicates: \n", len(removed))

#print("\nResult after Removal :\n", removed.head(n=5))
