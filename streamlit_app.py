from re import I
from numpy import string_
import streamlit as st
import pandas as pd     
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium


##THE TUTORIAL I AM WORKING WITH https://www.youtube.com/watch?v=uXj76K9Lnqc&ab_channel=ZakariaChowdhury

##TITLE
APP_TITLE = "Birds of Europe Interactive Map"
APP_SUBTITLE = "Source: GBIF.org (06 October 2019) GBIF Occurrence Download https://doi.org/10.15468/dl.hbcqmv"

        
##FILTER BY SPECIES
def filter_species(df, species, metric_title):
        df = df[df['species'] == species]
        df.drop_duplicates(inplace = True)
        df.dropna(axis = 1, how = 'all', inplace = True)
        total = df.shape[0]
        st.metric(metric_title, total)

##FILTER BY COUNTRY
def filter_species_country(df, countryCode, species, metric_title_country):
        df = df[(df['countryCode'] == countryCode) & (df['species'] == species)] 
        df.drop_duplicates(inplace = True)
        df.dropna(axis = 1, how = 'all', inplace = True)
        ##DF.SHAPE IS A 2DIMENSIONAL ARRAY OF ROWS/COLUMNS. NR OF ROWS = INSTANCES 
        total = df.shape[0]
        st.metric(metric_title_country, total)

##FILTER BY YEAR
def entry_per_year(df, year, species, metric_title_year):
        df = df[(df['year'] == year) & (df['species'] == species)]
        df.drop_duplicates(inplace = True)
        df.dropna(axis = 1, how = 'all', inplace = True)
        total = df.shape[0]
        st.metric(metric_title_year, total)

##MAP
def display_map(df, species):
        df = df[df['species'] == species] 
        
        ##TAKE COORDINATES AND NAME
        loc_data = pd.DataFrame({
        'lat': df['decimalLatitude'], 
        'lon': df['decimalLongitude'],
        'name': df['species']
        })
        st.write(loc_data.head())
        st.map(loc_data)
                
        ##TODO MAP        
        ##WHAT I WANT TO DO IS I WANT TO MAKE A CHOROPLETH MAP THAT OVERLAYS THE NORMAL MAP, HIGHLIGHTING THE DATA ON CLICK
        ##I CANNOT LOAD THE NAMES, THROUGH THE COLUMNS/KEY_ON COMBO

        # map = folium.Map(location=[48, 22], zoom_start = 3.4, tiles = 'CartoDB positron')
        #choropleth = folium.Choropleth (
                #geo_data = 'data/countries.geojson',
                #data = df,
                #columns = ('countryCode', total),
                #key_on = "feature.properties.ISO_A3",
                #fill_color="BuPu",
                #fill_opacity=0.7,
                #line_opacity=0.5,
        #).add_to(map)

        #st_map = st_folium(map, width = 900, height = 650)

        #st.write('Map data') 
        #st.write(df.shape)
        #st.write(df.head())
      
def main():
        ##TITLES
        st.set_page_config(APP_TITLE)
        st.title(APP_TITLE)
        st.caption(APP_SUBTITLE)
        
        ##LOAD DATA
        @st.cache(persist = True)
        def load_data(nrows):
                df = pd.read_csv('data/birdeasterneurope.csv',sep ='\t') 
                return df   
        
        df = load_data(400000)
        
        ##SELECTBOX SPECIES
        species_list = list(df['species'].unique())
        species_list.sort()
        species = st.sidebar.selectbox('Species', species_list)
        
        ##SELECTBOX COUNTRY
        country_list = [''] + list(df['countryCode'].unique().astype(str))
        country_list.sort()
        country_Code = st.sidebar.selectbox('Country', country_list)
        
        ##SELECTBOX YEAR
        year_list = list(df['year'].unique())
        year_list.sort(reverse = True)
        year = st.sidebar.selectbox('Year', year_list)


        metric_title = f'Total Number of {species}'
        metric_title_country = f'Number of {species} in {country_Code}'
        metric_title_year = f'Number of {species} in {year}'
        
        st.subheader(f'{species} Facts:')
        
        ##PUT THEM NICELY IN THE SAME LINE
        col1, col2, col3 = st.columns(3)
        with col1:
               filter_species(df,species,metric_title)
        with col2:
                filter_species_country(df, country_Code, species, metric_title_country)
        with col3:
                entry_per_year(df, year, species, metric_title_year)
        
        display_map(df,species)
       
if __name__ == "__main__":
    main()