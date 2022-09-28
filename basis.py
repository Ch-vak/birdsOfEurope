#url : https://www.gbif.org/occurrence/download/0011211-190918142434337

#IMPORTING LIBRARIES 
####################

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


#END OF IMPORTING LIBRARIES
#############################


DATA_URL = ( "birdeasterneurope.csv" )

data = pd.read_csv('birdeasterneurope.csv', sep='\t')
#WE NEED TO ADD DELIMITER BECAUSE THEY ARE \T SEPARATED VALUES

print("-------------Our data in rowsxcollumns------------- \n")
print(data.shape)
print("\n")

print("-------------Our collumns names------------- \n")
print(data.info())
print("\n")

print("-------------Our values for the year------------- \n")
print(data['year'].describe())
#YOU CAN CHANGE YEAR FOR ANY OTHER COLLUMN AND SEE THE MEAN VALUES
#WE OBSERVE THAT WE HAVE 12 YEARS IN TOTAL 2006-2018
print("\n")

print("-------------Our vallue counts for IDs------------- \n")
print(data["gbifID"].value_counts())
print("\n")

#EVERYTHING IS REGISTERED AS SOMETHING NEW

print("-------------Our vallue counts for KINGDOM------------- \n")
print(data["kingdom"].value_counts())
print("\n")
#EVERYTHING IS IN ANIMALIA

infodata = data.apply(lambda x: x.isnull().value_counts())

print(infodata)

for c in data.columns:
    print ("---- %s ---" % c)
    print (data[c].value_counts())

#INTRESTING COUNTRY CODE AND SCIENTIFIC NAME FOR OCCURANCES IN COUNTRIES AS A START

print(data['year'].plot(kind='hist', figsize=(16,4)))


dataframe = data['year'].value_counts()
dataframe
st.write('This is a line_chart.')
st.line_chart(dataframe)

#st.write('Map data')
#d = {data['decimalLatitude'], data['decimalLongitude']}
#df = pd.DataFrame(data=d)

df = pd.DataFrame({'lat':data['decimalLatitude'], 'lon':data['decimalLongitude'] })

st.map(df)

plt.scatter(x=data['decimalLatitude'], y=data['decimalLongitude'])
plt.rcParams["figure.figsize"] = [50,35]
plt.show()
