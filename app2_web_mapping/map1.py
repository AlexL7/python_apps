import folium
import pandas


df=pandas.read_csv("Volcanoes-USA.txt") #dataframe object


#creates map object (takes aveage of data inputs for start location)
map = folium.Map(location=[ df['LAT'].mean(),df['LON'].mean()], zoom_start =6,tiles='Stamen Terrain')

#function to give color based on elevation

def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/4)

    if elev in range (minimum,minimum+step):
      col='blue'
    elif elev in range (minimum+step,minimum+step*2):
      col='green'
    elif elev in range(minimum+step*2,minimum+step*3):
      col='orange'
    else:
      col='red'
    return col


# use loop to create a marker for each volacano
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color=color(elev),icon_color='green')))


#manual add markers on the map
  #map.simple_marker(location=[45.3288,-121.6625],popup='Mt.Hood Meadows', marker_color='red')
  #map.simple_marker(location=[45.3211,-121.7311],popup='Timberlake Lodge', marker_color='green')

#create html map
map.save(outfile='map1.html')
