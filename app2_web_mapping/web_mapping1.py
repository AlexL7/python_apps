import folium
import pandas


df=pandas.read_csv("Volcanoes-USA.txt") #dataframe object


#creates map object
map = folium.Map(location=[45.372,-121.697], zoom_start =6,tiles='Stamen Terrain')

#function to give color based on elevation
def color(elev):
    if elev in range (0,1000):
      col='blue'
    elif elev in range (1000,2000):
      col='green'
    elif elev in range(2000,3000):
      col='orange'
    else:
      col='red'
    return col


# use loop to create a marker for each volacano
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon],popup=name, marker_color=color(elev))


#manual add markers on the map
  #map.simple_marker(location=[45.3288,-121.6625],popup='Mt.Hood Meadows', marker_color='red')
  #map.simple_marker(location=[45.3211,-121.7311],popup='Timberlake Lodge', marker_color='green')

#create html map
map.create_map(path='test_map.html')
