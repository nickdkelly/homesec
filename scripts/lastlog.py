from datetime import datetime
import os
import re
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


# program specific code
def create_xml_element(line):
    file_system = line[0]
    file_element = ET.Element('user')
    file_element.set('username', file_system)

    if len(line) > 1:
        blocks = line[1]
        used = line[2]
        availiable = line[3]
        file_element.set('port', blocks)
        file_element.set('from', used)
        file_element.set('latest', availiable)
    return file_element


def create_xml_error_element(username, duration):
    error_element = ET.Element('error')
    error_element.set('description', username)
    error_element.set('value', str(duration))
    return error_element


def run_df():
    # Create the header element that describes the program
    now = get_formatted_date()
    header_element = create_header_element('lastlog', '1.0', now, 'desc')

    # Gather the output from the command and split the lines and strings

    lastlog = os.popen("lastlog").read()
    lastlog = re.sub(' +', ' ', lastlog).splitlines()
    lastlog = [s.split(' ', 3) for s in lastlog]
    # remove the first item
    lastlog = lastlog[1:]
    # Filter out any values that have not been logged into
    logged = []
    for s in lastlog:
        if s[1] == '**Never':
            logged.append([s[0]])
        else:
            s[3] = re.sub(' \+\d{4}', '', s[3])

            s[3] = datetime.strptime(s[3], '%a %b %d %H:%M:%S %Y')
            if (datetime.now() - s[3]).total_seconds() < 3600:
                s.append(datetime.now() - s[3])

            s[3] = s[3].strftime('%d-%b-%y %H:%M:%S')
            logged.append(s)

    files_element = ET.Element('users')
    errors_element = ET.Element('errors')
    for line in logged:
        file_element = create_xml_element(line)
        files_element.append(file_element);
        # check if there are any errors in this line
        if len(line) == 5:
            error_element = create_xml_error_element(line[0], line[4])
            errors_element.append(error_element)

    # Group all the elements together into their final output
    output_element = ET.Element('output')
    output_element.append(header_element)
    output_element.append(files_element)
    output_element.append(errors_element)
    return output_element


def main():
    output_path = get_output_path()
    output_element = run_df()

    # convert the element into a file
    output_xml_element_to_file(output_path, output_element)


if __name__ == "__main__":
    main()
