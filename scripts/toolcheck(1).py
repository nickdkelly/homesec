import os
import xml.etree.cElementTree as XmlTree
import datetime
import subprocess
import urllib2


def download_file(url, filename):
    attempts = 0
    while attempts < 3:
        try:
            response = urllib2.urlopen(url, timeout=5)
            content = response.read()
            f = open(filename, 'w')
            f.write(content)
            f.close()
            return True
        except urllib2.URL as e:
            attempts += 1
            print(type(e))
    return False


def pip_check():
    print("[+] Checking if PIP is installed!")
    try:
        import pip
    except ImportError:
        print("    [*] PIP not found...Please Wait while it is being installed!")
        os.system('sudo apt-get install python-pip')
        installed = False
    else:
        print("    [*] PIP found!")
        installed = True

    return installed


def psutil_check():
    print("[+] Checking if psutil is installed!")
    try:
        import psutil
    except ImportError:
        print("    [*] psutil not found...Please Wait!")
        os.system('python -m pip install psutil')
        installed = False
    else:
        print("    [*] psutil found!")
        installed = True

    return installed


def df_check():
    print("[+] Checking if df is installed...")
    retval = subprocess.call(["which", "df"])
    if retval != 0:
        print("    [*] df is not installed!")
        print("PLEASE CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] df is installed!")
        installed = True

    return installed


def rk_check():
    print("[+] Checking if rkhunter is installed...")
    retval = subprocess.call(["which", "rkhunter"])
    if retval != 0:
        print("    [*] rkhunter is not installed!")
        installed = False
    else:
        print("    [*] rkhunter is installed!")
        installed = True

    return installed


def apt_check():
    print("[+] Checking if apt is installed...")
    retval = subprocess.call(["which", "apt"])
    if retval != 0:
        print("    [*] apt is not installed!")
        print("PLEASE CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] apt is installed!")
        installed = True

    return installed


def lastlog_tool_check():
    print("[+] Checking if apt is installed...")
    retval = subprocess.call(["which", "lastlog"])
    if retval != 0:
        print("    [*] lastlog is not installed!")
        print("PLEASE CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] lastlog is installed!")
        installed = True

    return installed


def nmap_check():
    print("[+] Checking if nmap is installed...")
    retval = subprocess.call(["which", "nmap"])
    if retval != 0:
        print("    [*] nmap is not installed!")
        os.system('sudo apt-get install nmap')
        installed = False
    else:
        print("    [*] nmap is installed!")
        installed = True

    return installed


def network_utilisation_check():
    print("[+] Checking if network_utilisation.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/network_utilisation.py", "network_utilisation.py")
    retval = os.path.exists("./network_utilisation.py")
    print(retval)
    if retval == False:
        print("    [*] network_utilisation.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] network_utilisation.py is present!")
        installed = True

    return installed


def nikto_check():
    print("[+] Checking if nikto.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/nikto.py", "nikto.py")
    retval = os.path.exists("./nikto.py")
    if retval == False:
        print("    [*] nikto.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] nikto.py is present!")
        installed = True

    return installed


def df_python_check():
    print("[+] Checking if df.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/df.py", "df.py")
    retval = os.path.exists("./df.py")
    if retval == False:
        print("    [*] df.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] df.py is present!")
        installed = True

    return installed


def lastlog_check():
    print("[+] Checking if lastlog.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/lastlog.py", "lastlog.py")
    retval = os.path.exists("./lastlog.py")
    if retval == False:
        print("    [*] lastlog.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] lastlog.py is present!")
        installed = True

    return installed


def nmap_ping_check():
    print("[+] Checking if nmap_ping.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/nmap_ping.py", "nmap_ping.py")
    retval = os.path.exists("./nmap_ping.py")
    if retval == False:
        print("    [*] nmap_ping.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] nmap_ping.py is present!")
        installed = True

    return installed


def apt_history_check():
    print("[+] Checking if apt_history.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/apt_history.py", "apt_history.py")
    retval = os.path.exists("./apt_history.py")
    if retval == False:
        print("    [*] apt_history.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] apt_history.py is present!")
        installed = True

    return installed


def nmap_scan_check():
    print("[+] Checking if nmap_scan.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/nmap_scan.py", "nmap_scan.py")
    retval = os.path.exists("./nmap_scan.py")
    if retval == False:
        print("    [*] nmap_scan.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] nmap_scan.py is present!")
        installed = True

    return installed


def rkhunter_python_check():
    print("[+] Checking if rkhunter.py is present...")
    download_file("http://lec1.cyber.comp.southwales.ac.uk/CW2/tools/rkhunter.py", "rkhunter.py")
    retval = os.path.exists("./rkhunter.py")
    if retval == False:
        print("    [*] rkhunter.py not found!")
        print("PLEASE DOUBLE CHECK YOU HAVE DOWNLOADED THE PYTHON SCRIPTS IF SO CONTACT JACK OR ROSS!")
        installed = False
    else:
        print("    [*] rkhunter.py is present!")
        installed = True

    return installed


def check():
    current_time = get_time()
    version = "1.0.1"
    program_name = "Tool Check"

    root = XmlTree.Element("Output")

    program = XmlTree.Element("Program")
    XmlTree.SubElement(program, "name").text = program_name
    XmlTree.SubElement(program, "version").text = version
    XmlTree.SubElement(program, "date").text = current_time

    root.append(program)
    record = XmlTree.Element("record")
    error = XmlTree.Element("Errors")
    xml(record, error, "apt", apt_check())
    xml(record, error, "pip", pip_check())
    xml(record, error, "psutil", psutil_check())
    xml(record, error, "df", df_check())
    xml(record, error, "rkhunter", rk_check())
    xml(record, error, "lastlog", lastlog_tool_check())
    xml(record, error, "nmap", nmap_check())
    xml(record, error, "networkusage.py", network_utilisation_check())
    xml(record, error, "nikto.py", nikto_check())
    xml(record, error, "df.py", df_python_check())
    xml(record, error, "lastlog.py", lastlog_check())
    xml(record, error, "nmap_ping.py", nmap_ping_check())
    xml(record, error, "nmap_scan.py", nmap_scan_check())
    xml(record, error, "rkhunter.py", rkhunter_python_check())
    xml(record, error, "apt_history.py", apt_history_check())

    root.append(record)
    root.append(error)
    tree = XmlTree.ElementTree(root)

    with open("toolcheck.xml", "ab") as fh:
        tree.write(fh, xml_declaration=True, encoding='utf-8', method="xml")


def xml(record, error, tool_name, installed):
    if installed == True:
        XmlTree.SubElement(record, "installed", name=tool_name).text = str(installed)
    else:
        XmlTree.SubElement(error, "installed", name=tool_name).text = str(installed)

    return XmlTree


def get_time():
    time_stamp = datetime.datetime.utcnow().strftime("%d-%B-%m-%Y %H:%M:%S")
    return time_stamp


def main():
    check()


if __name__ == '__main__':
    main()
