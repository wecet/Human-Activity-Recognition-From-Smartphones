#%%
import pandas as pd

#%%
file = pd.read_csv("test.csv")
#print("\nResult before Removal :\n", file.head(n=5))
duplicates = file[file.duplicated()]
print("Size of File with Duplicates: \n", len(file))
#print("\nDuplicate Rows: \n {}".format(duplicates))

##REMOVED IS THE VARIABLE THAT STORES THE DATA SET WITHOUT DUPLICATES
removed = file.drop_duplicates(keep='last')
removed.to_csv("output.csv")
print("Size of File after Removal of Duplicates: \n", len(removed))
#print(type(removed))
#print("\nResult after Removal :\n", removed.head(n=5))
