import os
import optparse
from os.path import basename
import xml.etree.ElementTree as ET

def get_formatted_date():
	import datetime
	return datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')

def create_header_element(name, version, date, description):
	program_element = ET.Element('program')
	name_element = ET.SubElement(program_element, 'name')
	name_element.text = name
	version_element = ET.SubElement(program_element, 'version')
	version_element.text = version
	date_element = ET.SubElement(program_element, 'date')
	date_element.text = date
	desc_element = ET.SubElement(program_element, 'description')
	desc_element.text = description
	return program_element


def output_xml_element_to_file(file_path, output_element):
	contents = ET.tostring(output_element)

	with open(file_path, 'w') as output_file:
		output_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>')
		output_file.write(contents)

def get_output_path():
	parser = optparse.OptionParser("usage %prog -o output_file_name ")
	parser.add_option('-o', dest='output_file_name', type='string', help='Set the output file location')
	(options, arg) = parser.parse_args()

	output_file_name = basename(__file__).replace('.py', '') + '.xml'
	if (options.output_file_name != None):
        	output_file_name = options.output_file_name

	return output_file_name


#program specific code
def create_xml_element(line):
	file_system = line[0]
	blocks = line[1]
	used = line[2]
	availiable = line[3]
	use = line[4]
	mount = line[5]
	file_element =	ET.Element('file')
	file_element.set('FileSystem', file_system)
	file_element.set('Blocks', blocks)
	file_element.set('Used', used)
	file_element.set('Availiable', availiable)
	file_element.set('Use', use)
	file_element.set('Mount', mount)
	return file_element

def create_xml_error_element(line, threshold):
	file_system = line[0]
	use = int(line[4][:-1])
	if (use >= threshold):
		error_element = ET.Element('error')
		desc_text = file_system + ' is above ' + str(threshold)  + ' percent'
		error_element.set('description', desc_text)
		error_element.set('value', str(use))
		return error_element
	return False

def run_df():
	#Create the header element that describes the program
	now = get_formatted_date()
	header_element = create_header_element('apt history', os.popen('apt --version').read(), now, 'apt log /var/log/apt/history.log')

	#Gather the output from the command and split the lines and strings

	history_element = ET.Element('history')
	with open("/var/log/apt/history.log", "r") as f:
		data = f.read()
		data = data.split('\n\n')
		for history in data:
			record_element = ET.Element('record')
			temp = [s.split(':',1) for s in history.splitlines()]
			for s in temp:
				if (len(s) > 1):
					record_element.set(s[0], s[1].strip())
			history_element.append(record_element)

	#Group all the elements together into their final output
	output_element = ET.Element('output')
	output_element.append(header_element)
	output_element.append(history_element)
	return output_element


def main():
	output_path = get_output_path()
	output_element = run_df()

	#convert the element into a file
	output_xml_element_to_file(output_path, output_element)

if __name__ == "__main__":
    main()
