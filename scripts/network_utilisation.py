import base64
import optparse
from os.path import basename

def open_file(file_name, base_64):
    decoded_file = base64.decodebytes(str.encode(base_64))
    write_to_xml(decoded_file, file_name)

def write_to_xml(decoded_file, file_name):
    file = open(file_name + ".xml", "wb")
    file.write(decoded_file)
    file.close()

def main():

    xml_encode = "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxvdXRwdXQ+DQogICAgPHByb2dyYW0+DQogICAgICAgIDxuYW1lPk5ldHdvcmsgVXRpbGlzYXRpb248L25hbWU+DQogICAgICAgIDx2ZXJzaW9uPk4vQTwvdmVyc2lvbj4NCiAgICAgICAgPGRhdGU+MDUtRmViLTIwMTggMTI6NDc6NTY8L2RhdGU+DQogICAgICAgIDxkZXNjcmlwdGlvbj48L2Rlc2NyaXB0aW9uPg0KICAgIDwvcHJvZ3JhbT4NCiAgICA8TmV0d29ya0RhdGE+DQogICAgICAgIDxob3N0bmFtZSBuYW1lPSJsZWMxIi8+DQogICAgICAgIDxEYXRlIGRhdGU9Ik1vbmRheS0wNS0wMi0xOF8xMjo0Nzo1NiIvPg0KICAgICAgICA8aW50ZXJmYWNlIG5hbWU9ImxvIj4NCiAgICAgICAgICAgIDxCeXRlc1NlbnQgbmFtZT0iQnl0ZXNTZW50Ij4xMDQzMDA5MzwvQnl0ZXNTZW50Pg0KICAgICAgICAgICAgPEJ5dGVzUmVjZWl2ZWQgbmFtZT0iQnl0ZXNSZWNlaXZlZCI+MTA0MzAwOTM8L0J5dGVzUmVjZWl2ZWQ+DQogICAgICAgICAgICA8UGFja2V0c1NlbnQgbmFtZT0iUGFja2V0c1NlbnQiPjI0MTA1PC9QYWNrZXRzU2VudD4NCiAgICAgICAgICAgIDxQYWNrZXRzUmVjZWl2ZWQgbmFtZT0iUGFja2V0c1JlY2VpdmVkIj4yNDEwNTwvUGFja2V0c1JlY2VpdmVkPg0KICAgICAgICA8L2ludGVyZmFjZT4NCiAgICAgICAgPGludGVyZmFjZSBuYW1lPSJlbnMxNjAiPg0KICAgICAgICAgICAgPEJ5dGVzU2VudCBuYW1lPSJCeXRlc1NlbnQiPjEzMjM5MzMwMTwvQnl0ZXNTZW50Pg0KICAgICAgICAgICAgPEJ5dGVzUmVjZWl2ZWQgbmFtZT0iQnl0ZXNSZWNlaXZlZCI+NDI2MTA4NDQ3PC9CeXRlc1JlY2VpdmVkPg0KICAgICAgICAgICAgPFBhY2tldHNTZW50IG5hbWU9IlBhY2tldHNTZW50Ij4yNjc2MTk8L1BhY2tldHNTZW50Pg0KICAgICAgICAgICAgPFBhY2tldHNSZWNlaXZlZCBuYW1lPSJQYWNrZXRzUmVjZWl2ZWQiPjM1MzUyMTA8L1BhY2tldHNSZWNlaXZlZD4NCiAgICAgICAgPC9pbnRlcmZhY2U+DQogICAgPC9OZXR3b3JrRGF0YT4NCjwvb3V0cHV0Pg=="
    
    parser = optparse.OptionParser("usage %prog " + \
                                   "-o output_file_name ")
    parser.add_option('-o', dest='output_file_name', type='string', \
                      help='Set the output file location')
    (options, arg) = parser.parse_args()

    output_file_name = basename(__file__).replace('.py', '') + '.xml'
    if (options.output_file_name != None):
        output_file_name = options.output_file_name

    open_file(output_file_name,xml_encode)

if __name__ == "__main__":
    main()
