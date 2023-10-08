

# importing os module 

# a creating a directory using its functions 

import os

if(not os.path.exists("Data")):

       os.mkdir("Data")


# creating 100 files in the data directory using os module 

for i in range (0,100):

       os.mkdir(f"Data/Day{i+1}")