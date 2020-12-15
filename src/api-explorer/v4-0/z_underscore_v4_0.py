from unipath import Path
import os

# CircleCI will run this script 5th

# This will add an "_" to all the fresh .md files in v4-0


# All markdown files in the 'includes' folder in Slate portion of the Dev Center repo
os.chdir(r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\api-explorer\v4-0")

#Add "_" to the beginning of every markdown file that does not have it
for markdown in os.listdir():
    if "_" not in markdown:
        new_name = "_" + markdown        
        os.rename(markdown, new_name)
        print("Adding '_' to file...Filename has just been updated to: ", new_name)
print("All filenames already have correct formatting")
    