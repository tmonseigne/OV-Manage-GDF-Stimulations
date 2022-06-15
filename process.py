
"""Process to change Stimulation in GDF File"""

__author__ = "Thibaut Monseigne"
__license__ = "GNU AFFERO GENERAL PUBLIC LICENSE Version 3"


# Run Read-Stim.xml
# Quick method arrange csv file
# Good method Check if stims are bad next arrange csv file
# Run Change-Stim.xml


def search_and_replace_in_file(filename, old, new):
	with open(filename, 'r') as file:
		raw = file.read()

	raw = raw.replace(old, new)

	with open(filename, 'w') as file:
		file.write(raw)


def process():
	# Change setting input file on OV Files
	search_and_replace_in_file('Read-Stim.xml', 'file.gdf', 'A1_R3_onlineT.gdf')
	search_and_replace_in_file('Change-Stim.xml', 'file.gdf', 'A1_R3_onlineT.gdf')

	# Run Read-Stim.xml

	# Return setting input file on OV Files
	search_and_replace_in_file('Read-Stim.xml', 'A1_R3_onlineT.gdf', 'file.gdf')
	search_and_replace_in_file('Change-Stim.xml', 'A1_R3_onlineT.gdf', 'file.gdf')


process()
