import pygal
from pygal_maps_world import maps

wm = maps.World()
wm.title = 'North, Central, and South America & China'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
	'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('Asian', ['cn'])

wm.render_to_file("americas.svg")
