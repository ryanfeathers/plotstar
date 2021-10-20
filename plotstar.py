#!/usr/bin/env python
"""
Plot group numbers by location

Author: Ryan Feathers jrf296
Date: 10/19/2021
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
	fig = px.scatter_3d(particles, x="rlnCoordinateX", y="rlnCoordinateY", \
		z = "rlnCoordinateZ", color = args.color, size_max=1)

	fig.update_traces(marker={'size': 2})

	fig.show()
else:
###2D plot###
	fig = px.scatter(particles, x="rlnCoordinateX", y="rlnCoordinateY", \
		 color = args.color)

	fig.update_traces(marker={'size': 5})

	fig.show()














