import folium

#creates html file with a map
map = folium.Map(location=[45.372,-121.697], zoom_start =12,tiles='Stamen Terrain')

#markers on the map
map.simple_marker(location=[45.3288,-121.6625],popup='Mt.Hood Meadows', marker_color='red')
map.simple_marker(location=[45.3211,-121.7311],popup='Timberlake Lodge', marker_color='green')

map.create_map(path='test_map.html')
