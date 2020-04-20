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

def create_error_element(description, value):
	error_element = ET.Element('error');
	error_element.set('description', description)
	error_element.set('value', value)
	return error_element

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

	command = 'nmap -oX - ' + get_hostname()

	header_element = create_header_element(command, nmap_version, now, 'nmap local scan')
	errors_element = ET.Element('errors')

	uput = os.popen(command).read()
	nmap_xml = ET.fromstring(uput)

	ports = nmap_xml.findall('host/ports/port');
	for port in ports:
		name = port.find('service').get('name')
		port_id = int(port.get('portid'))
		state = port.find('state').get('state')
		#Write a list of ports that we would want to check
		if (port_id == 3306 and state == 'open'):
			error_element = create_error_element(name + ' status ' + state + ' db should never be exposed', str(port_id))
			errors_element.append(error_element)
		elif (port_id == 22 and state == 'open'):
			error_element = create_error_element(name + ' status ' + state + ' SSH port exposure', str(port_id))
			errors_element.append(error_element)

	#Group all the elements together into their final output
	output_element = ET.Element('output')
	output_element.append(header_element)
	output_element.append(nmap_xml)
	output_element.append(errors_element)
	return output_element


def main():
	output_path = get_output_path()
	output_element = run_df()

	#convert the element into a file
	output_xml_element_to_file(output_path, output_element)

if __name__ == "__main__":
    main()
