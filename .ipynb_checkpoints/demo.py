# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '.ipynb_checkpoints'))
	print(os.getcwd())
except:
	pass
#%%
from IPython import get_ipython


#%%
import pandas as pd


#%%
# Read the csv file in
filename      = "cities.csv"
df            = pd.read_csv(filename).reset_index(None)[['City','Cloudiness','Country','Date','Humidity','Lat','Lng','Max Temp','Wind Speed']]
df.head()


#%%
# Assign to string
df.to_html('cities_data.html',classes='utf8',index=False)
#df.reset_index(drop=True)


#%%
# Save to file
df.to_html('cities_data.html')


#%%
# Open the file
get_ipython().system('explorer cities_data.html')


#%%



