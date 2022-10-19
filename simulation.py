#IMPORTING LIBRARIES 
####################


from re import U
import streamlit as st
import pandas as pd
import pydeck as pdk

#END OF IMPORTING LIBRARIES

#Define Functions
def type_hexagon_layer_map(data):
	names_list = data['type'].to_list()		#find the different types and make a list
	set_names = set(names_list)
	names_list = list(set_names)
	st.header("Places of observation for specific types.")
	type_selectbox = st.selectbox("Specify Type", names_list)
	Scatter_LAYER_DATA = data.query("type == @type_selectbox")[['lat','lon']]
	layer = pdk.Layer(
		"HexagonLayer",
		Scatter_LAYER_DATA,
		get_position=["lon", "lat"],
		auto_highlight=True,
		elevation_scale=50,
		pickable=True,
		elevation_range=[1000, 5000],
		extruded=True,
		coverage=5,
	)
	# Set the viewport location
	view_state = pdk.ViewState(
		longitude=data['lon'].mean(), latitude=data['lat'].mean(), zoom=2, min_zoom=3, max_zoom=15, pitch=30, bearing=10,
	)
	# Render
	re = pdk.Deck(layers=[layer], initial_view_state=view_state)
	st.write(re)

def year_slider_map(data):
	st.header("Places of observation per year. Starting from 2006 for all types.")
	year_slider2 = st.slider("Year range:", 2006,2018)
	original_data = data
	data = data[data['year'] == year_slider2]
	HEXAGON_LAYER_DATA = data  
	# Define a layer to display on a map
	layer = pdk.Layer(
		"HexagonLayer",
		HEXAGON_LAYER_DATA,
		get_position=["lon", "lat"],
		auto_highlight=True,
		elevation_scale=50,
		pickable=True,
		elevation_range=[1000, 5000],
		extruded=True,
		coverage=7,
	)
	# Set the viewport location
	view_state = pdk.ViewState(
		longitude=data['lon'].mean(), latitude=data['lat'].mean(), zoom=2, min_zoom=3, max_zoom=15, pitch=30, bearing=10,
	)
	# Render
	r = pdk.Deck(layers=[layer], initial_view_state=view_state)
	st.write(r)

def load_data():
	data = pd.read_csv("new_data.csv")
	data.columns = ['id', 'type', 'cd', 'lat', 'lon', 'day', 'month', 'year']
	data.dropna(subset=['lat','lon','year','day','month','cd'],inplace=True)
	return data

def country_code(data):
	cd_set = set(data['cd'])
	countries_list = list(cd_set)
	st.header("All countries observations")
	type_selectbox = st.selectbox("Specify Country code", countries_list)
	Scatter_LAYER_DATA = data.query("cd == @type_selectbox")[['lat','lon']]
	layer = pdk.Layer(
		"ScatterplotLayer",
		Scatter_LAYER_DATA,
		get_position=["lon", "lat"],
		auto_highlight=True,
		get_radius=10000,          # Radius is given in meters
		get_fill_color=[180, 0, 200, 140],  # Set an RGBA value for fill
		pickable=True,
		elevation_range=[0, 2],
		extruded=True,
		coverage=10,
	)
	# Set the viewport location
	view_state = pdk.ViewState(
		longitude=Scatter_LAYER_DATA['lon'].mean(), latitude = Scatter_LAYER_DATA['lat'].mean(), zoom=2, min_zoom=3, max_zoom=15, pitch=30, bearing=10,
	)
	# Render
	re = pdk.Deck(layers=[layer], initial_view_state=view_state)
	st.write(re)

#end of function definiton 

def main():
	data = load_data()
	year_slider_map(data)
	type_hexagon_layer_map(data)
	country_code(data)

	if st.checkbox("Show raw data", False):
		st.subheader('Raw data')
		st.write(data)



#st.header("Yearly observations")
#year_slider = st.slider("Specify year:",2006,2018)
#st.map(data.query("year == @year_slider")[['lat','lon']])


