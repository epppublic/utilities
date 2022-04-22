import os
from os import listdir
import pandas as pd
import io

file_list = listdir('/Volumes/Elements/Films 1 2 3 4')
print(file_list)
# Create dataframe out of file list
df_names = pd.DataFrame(file_list)
# Create CSV file
df_names.to_csv('/Users/epalma/Documents/all_films.csv')


# First approach below only print the name but does not create the list of folder names
# os.chdir('/Volumes/Elements/Films 1 2 3 4')

# all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
# for dirs in all_subdirs:
#     dir = os.path.join('/Volumes/Elements/Films 1 2 3 4', dirs)
#     os.chdir(dir)
#     current = os.getcwd()
#     new = str(current).split("/")[4]
#     newdf = pd.read_csv(io.StringIO(new), sep=";")
#     newdf.to_csv('/Users/epalma/Documents/all_films.csv')
#     print(new)