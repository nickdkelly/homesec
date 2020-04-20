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

def get_hostname():
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	return ip

#program specific code
def run_df():
	#Create the header element that describes the program
	now = get_formatted_date()

	nmap_version = os.popen("nmap --version").read()

	header_element = create_header_element('nmap -oX - -sP', nmap_version, now, 'nmap ping scan')

	uput = os.popen("nmap -oX - -sP 192.168.171.0/24").read()
	nmap_xml = ET.fromstring(uput)

	#Group all the elements together into their final output
	output_element = ET.Element('output')
	output_element.append(header_element)
	output_element.append(nmap_xml)
	return output_element


def main():
	output_path = get_output_path()
	output_element = run_df()

	#convert the element into a file
	output_xml_element_to_file(output_path, output_element)

if __name__ == "__main__":
    main()
