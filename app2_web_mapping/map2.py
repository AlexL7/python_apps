import folium
import pandas


df=pandas.read_csv("Volcanoes-USA.txt") #dataframe object


#creates map object (takes aveage of data inputs for start location)
map=folium.Map(location=[ df['LAT'].mean(),df['LON'].mean()], zoom_start=6,tiles='Mapbox bright')

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


#create feature group
fg=folium.FeatureGroup(name='Volcano Locaitons')

# use loop to create a marker for each volacano
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color=color(elev),icon_color='green')))

#add feature group to the map
map.add_child(fg)

# add polygon data to map
map.add_child(folium.GeoJson(data=open('World_population.json'),
  name='World Population',
  style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<30000000 else 'red'}))

#adding layer control panel
map.add_child(folium.LayerControl())

#create html map file
map.save(outfile='map2.html')
