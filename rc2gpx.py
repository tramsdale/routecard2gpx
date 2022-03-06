import osgb
import gpxpy
import argparse
from math import *
from tabulate import *

parser = argparse.ArgumentParser(description='Process a route-card into a gpx file')
parser.add_argument('gridrefs', metavar='GR', type=str, nargs='*',
	help='Grid references in 6-digit OS Map format')
parser.add_argument('-o', type=str, dest='outfile', action='store', help='Output file name', 
	default='output.gpx')
parser.add_argument('-v', dest='verbose', action='store_true', help='Select verbose mode', default=False)
parser.add_argument('--map', type=str, nargs=1, default='TL', action='store',
	help='map square, such as TL, SV, NX etc')
parser.add_argument('--name', type=str, dest='name', default='Autogen', action='store',
	help='Name to use in gpx file')
parser.add_argument('--desc', type=str, dest='description', default='Autogen', action='store',
	help='Name to use in gpx file')
parser.add_argument('-q', dest='nquiet', action='store_false', default=True)
parser.add_argument('--speed', dest='speed', action='store', type=float, default=3.0)

a = parser.parse_args()

routemap = [['Type', 'Grid ref', 'Bearing', 'Distance/km', 'Est leg time', 'Total time']]
ttotal = 0
way = 0
last_gridref = f''

def add_start(routemap, gridref):
	global ttotal, way, last_gridref
	last_gridref = gridref
	# routemap.append(['START', grid_ref, bearing, distance, tleg, ttotal])

def add_point(routemap, gridref, bearing, distance):
	global ttotal, way, last_gridref
	waytype = f'START' if way==0 else f'WAY{way}'
	tleg = distance/a.speed
	ttotal += tleg
	routemap.append([waytype, last_gridref, f'{bearing:03.0f}', f'{distance:.1f}', conv_time(tleg), conv_time(ttotal)])
	way+=1
	last_gridref = gridref


def add_finish(routemap):
	global ttotal, way, last_gridref
	waytype = f'FINISH'
	routemap.append([waytype, last_gridref, '', '', '', ''])

def conv_time(hours):
	ihrs = floor(hours)
	mins = (hours-ihrs)*60
	if ihrs>0:
		return f'{ihrs}h{mins:02.0f}'
	else:
		return f'{mins:02.0f}m'

def main():
	if a.nquiet:
		print(f'Using map square: {a.map}')
		print(f'Writing gpx to file: {a.outfile}')

	# Create a new file:
	gpx = gpxpy.gpx.GPX()
	gpx.name=a.name
	gpx.description = a.description
	# Create first track in our GPX:
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx.tracks.append(gpx_track)
	# Create first segment in our GPX track:
	gpx_segment = gpxpy.gpx.GPXTrackSegment()
	gpx_track.segments.append(gpx_segment)

	i=0
	distance = 0
	direction = 0
	x=y=0 

	for j in a.gridrefs:
		gref = f'{a.map} {j}'
		if i>0:
			(last_e, last_n) = (e, n)
		(e,n) = osgb.parse_grid(gref)
		(lat, lon) = osgb.grid_to_ll(e,n)
		if i>0:
			x = e - last_e
			y = n - last_n
			distance = sqrt(x**2 + y**2)/1000
			if x==0:
				direction = 0 if (y>0) else 180
			elif y==0:
				direction = 90 if x>0 else 270
			elif x>0 and y>0:
				direction  = 90-degrees(atan(y/x))
			elif x<0 and y>0:
				direction  = 270+degrees(atan(-y/x))
			elif x>0 and y<0:
				direction = 90+degrees(atan(-y/x))
			elif x<0 and y<0:
				direction = 270-degrees(atan(y/x))

			if direction < 0:
				direction += 360


		# Create points:
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon))
		if i==0:
			add_start(routemap, gref)
		else:
			add_point(routemap, gref, direction, distance)
		i+=1
		if a.nquiet:
			print(f'Processing coordinate {gref} ...lat:{lat:.3f}, lon:{lon:.3f}  delta = {x:.2f}, {y:.2f},  ... {distance:.2f}km, {direction:.1f}deg')

	add_finish(routemap)
	gpx=gpx.to_xml()
	if a.verbose: 
		print('Created GPX:', gpx)
	f=open(a.outfile, 'w')
	f.write(gpx)
	f.close()

	print(tabulate(routemap, headers='firstrow', tablefmt='fancy_grid'))








if __name__ == '__main__':
	main()

