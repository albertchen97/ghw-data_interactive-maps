import pandas as pd
import streamlit as st
import folium
import streamlit.components.v1 as components

PATH_TO_DATA = "aa_flights_paths_data.csv"


def aa_flight_paths():
  # add a subtitle
  st.subheader("AA Flight Paths")
  
  # load data from CSV into dataframe
  flight_paths = pd.read_csv(PATH_TO_DATA)
  
  # add a column called row_id at the beginning
  flight_paths.insert(0, 'row_id', range(1, 1 + len(flight_paths)))
  st.dataframe(flight_paths, hide_index=True)
  map = folium.Map(location=(45.5236, -122.6750))
  
  # Iterate over the dataframe rows
  for index, row in flight_paths.iterrows():
    start_coords = (row['start_lat'], row['start_lon'])
    end_coords = (row['end_lat'], row['end_lon'])
    line = folium.PolyLine(locations=[start_coords, end_coords])
    map.add_child(line)
    
  map.save("light_paths.html")
  
  # Open the HTML file and read
  HtmlFile = open("flight_paths.html", "r", encoding="utf-8")
  my_map = HtmlFile.read()
  components.html(my_map, height=700)

