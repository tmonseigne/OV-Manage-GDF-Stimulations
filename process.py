"""Process to change Stimulation in GDF File"""

__author__ = "Thibaut Monseigne"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE Version 3"

import os
import os.path
from os import path

# Run Read-Stim.xml
# Quick method arrange csv file
# Good method Check if stims are bad next arrange csv file
# Run Change-Stim.xml

################################################


def search_and_replace_in_file(filename, old, new):
	with open(filename, 'r') as file:
		raw = file.read()

	raw = raw.replace(old, new)

	with open(filename, 'w') as file:
		file.write(raw)

################################################


def processWithOV(filename):
	ovFilename = filename.replace('gdf', 'ov')
	outputFilename = filename+"-output.gdf"

	# Change setting input file on OV Files
	search_and_replace_in_file('Get-OV-Stim.xml', 'file.gdf', filename)
	search_and_replace_in_file('Get-OV-Stim.xml', 'file.ov', ovFilename)
	search_and_replace_in_file('Read-Stim.xml', 'file.gdf', outputFilename)

	# "C:\OVBE-META\dist\x64\Release\openvibe-designer.cmd" "--no-pause" "--no-session-management" "--invisible" "--play-fast" "Get-OV-Stim.xml")
	# Run Get-OV-Stim.xml
	os.system("C:\\OVBE-META\\dist\\x64\\Release\\openvibe-designer.cmd \"--no-pause\" \"--no-session-management\" \"--invisible\" \"--play-fast\" \"Get-OV-Stim.xml\"")
	# Run Read-Stim.xml
	os.system("C:\\OVBE-META\\dist\\x64\\Release\\openvibe-designer.cmd \"--no-pause\" \"--no-session-management\" \"--invisible\" \"--play-fast\" \"Read-Stim.xml\"")

	# Return setting input file on OV Files
	search_and_replace_in_file('Get-OV-Stim.xml', filename, 'file.gdf')
	search_and_replace_in_file('Get-OV-Stim.xml', ovFilename, 'file.ov')
	search_and_replace_in_file('Read-Stim.xml', outputFilename, 'file.gdf')


################################################
init_path = "C:\\Git\\OV-Manage-GDF-Stimulations\\Signals"
files = [f for f in os.listdir(init_path) if f.endswith('.gdf')]
for i in range(len(files)):
	print("File "+i+"/"+len(files)+" : "+files[i])
	processWithOV(files[i])

print("Finish !! ")
