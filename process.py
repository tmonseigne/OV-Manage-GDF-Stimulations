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
def processReadStim(filename):
	search_and_replace_in_file('Read-Stim.xml', 'file.gdf', filename)
	os.system("C:\\OVBE-META\\dist\\x64\\Release\\openvibe-designer.cmd \"--no-pause\" \"--no-session-management\" \"--invisible\" \"--play-fast\" \"Read-Stim.xml\"")
	search_and_replace_in_file('Read-Stim.xml', filename, 'file.gdf')

################################################
def processChangeStim(filename):
	search_and_replace_in_file('Change-Stim.xml', 'file.gdf', filename)
	os.system("C:\\OVBE-META\\dist\\x64\\Release\\openvibe-designer.cmd \"--no-pause\" \"--no-session-management\" \"--invisible\" \"--play-fast\" \"Change-Stim.xml\"")
	search_and_replace_in_file('Change-Stim.xml', filename, 'file.gdf')


################################################
def processWithOV(filename):
	ovFilename = filename.replace('gdf', 'ov')
	outputFilename = filename+"-output.gdf"

	# Change setting input file on OV Files
	search_and_replace_in_file('Get-OV-Stim.xml', 'file.gdf', filename)
	search_and_replace_in_file('Get-OV-Stim.xml', 'file.ov', ovFilename)
	search_and_replace_in_file('Read-Stim.xml', 'file.gdf', outputFilename)

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
	print("File " + str(i) + "/" + str(len(files)) + " : " + files[i])
	processWithOV(files[i])

print("Finish !! ")
