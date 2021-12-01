#!/usr/bin/env python
"""
Plot group numbers by location

Author: Ryan Feathers jrf296
Date: 12/01/2021
"""
import argparse
import starfile
import os.path
import plotly.express as px

# def is_valid_file(parser, arg):
#     if not os.path.exists(arg):
#         parser.error("The file %s does not exist!" % arg)
#     else:
#         return open(arg, 'r')  # return an open file handle



parser = argparse.ArgumentParser()
parser.add_argument('--i', type=str, required=True, help='input particle file')
parser.add_argument('--color', type=str, required=False, help ='data value to color' )
parser.add_argument('--z', nargs='?', const=1, type=int, help = ' 3D with rlnCoordinateZ')                  
args = parser.parse_args()



df = starfile.read(args.i)
particles = df['particles']

if args.z == 1:
###3D Plot###
	if "rlnCoordinateZ" in particles.columns:
		fig = px.scatter_3d(particles, x="rlnCoordinateX", y="rlnCoordinateY", \
			z = "rlnCoordinateZ", color = args.color, size_max=1)

		fig.update_traces(marker={'size': 2})
		fig.update_layout(
			scene = dict(
				xaxis = dict(range = [0,5760],),
				yaxis = dict(range = [0,4092],),
				zaxis = dict(range = [0,3000],)),
			scene_aspectmode='manual',
	                  scene_aspectratio=dict(x=1, y=.8, z=.6))
		print("Plotting z=rlnCoordinateZ")
		fig.show()

	elif "rlnDefocusU" in particles.columns:
		fig = px.scatter_3d(particles, x="rlnCoordinateX", y="rlnCoordinateY", \
			z = "rlnDefocusU", color = args.color, size_max=1)

		fig.update_traces(marker={'size': 2})
		fig.update_layout(
			scene = dict(
				xaxis = dict(range = [0,5760],),
				yaxis = dict(range = [0,4092],),
				zaxis = dict(range = [0,20000],)),
			scene_aspectmode='manual',
	                  scene_aspectratio=dict(x=1, y=.8, z=.6))
		print("Plotting z=rlnDefocusU")
		fig.show()
	else:
		print("No Z value found")
else:
###2D plot###
	fig = px.scatter(particles, x="rlnCoordinateX", y="rlnCoordinateY", \
		 color = args.color)

	fig.update_traces(marker={'size': 5})

	print("Plotting in 2D")
	fig.show()
