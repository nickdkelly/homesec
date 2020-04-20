import base64
import optparse

def open_file(file_name, base_64):
    decoded_file = base64.decodebytes(str.encode(base_64))
    write_to_xml(decoded_file, file_name)

def write_to_xml(decoded_file, file_name):
    file = open(file_name + ".xml", "wb")
    file.write(decoded_file)
    file.close()

def main():
    parser = optparse.OptionParser("usage %prog " + \
                                   "-o output_file_name ")
    parser.add_option('-o', dest='output_file_name', type='string', \
                      help='Set the output file location')
    (options, arg) = parser.parse_args()
    output_file_name = 'rkhunter_out.xml'
    if (options.output_file_name != None):
        output_file_name = options.output_file_name

    open_file(output_file_name, "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjxvdXRwdXQ+DQogICAgPHByb2dyYW0+DQogICAgICAgIDxuYW1lPlJLSHVudGVyPC9uYW1lPg0KICAgICAgICA8dmVyc2lvbj4xLjQ0PC92ZXJzaW9uPg0KICAgICAgICA8ZGF0ZT4xMC1KYW4tMjAxOCAxMDoxMjowMTwvZGF0ZT4NCiAgICAgICAgPGRlc2NyaXB0aW9uPlJlaW50ZXJwcmV0ZWQgaW5wdXQgZnJvbSBSS0h1bnRlcjwvZGVzY3JpcHRpb24+DQogICAgPC9wcm9ncmFtPg0KICAgIDxyZWNvcmRzPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSJDaGVja2luZyAnc3RyaW5ncycgY29tbWFuZCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSJDaGVja2luZyBmb3IgcHJlbG9hZGluZyB2YXJpYWJsZXMiIHN0YXR1cz0iTm9uZSBmb3VuZCIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSJDaGVja2luZyBmb3IgcHJlbG9hZGVkIGxpYnJhcmllcyIgc3RhdHVzPSJOb25lIGZvdW5kIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9IkNoZWNraW5nIExEX0xJQlJBUllfUEFUSCB2YXJpYWJsZSIgc3RhdHVzPSJOb3QgZm91bmQiLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iQ2hlY2tpbmcgZm9yIHByZXJlcXVpc2l0ZXMiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL2FkZHVzZXIiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL2Nocm9vdCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL3NiaW4vY3JvbiIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL3NiaW4vZ3JvdXBhZGQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL2dyb3VwZGVsIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi9ncm91cG1vZCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL3NiaW4vZ3JwY2siIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL25vbG9naW4iIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL3B3Y2siIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL3JzeXNsb2dkIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi90Y3BkIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi91c2VyYWRkIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi91c2VyZGVsIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi91c2VybW9kIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi92aXB3IiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi91bmhpZGUiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9zYmluL3VuaGlkZS1saW51eCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL3NiaW4vdW5oaWRlLXBvc2l4IiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3Ivc2Jpbi91bmhpZGUtdGNwIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2F3ayIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9iYXNlbmFtZSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9jaGF0dHIiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vY3V0IiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2RpZmYiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vZGlybmFtZSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9kdSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9lbnYiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vZmlsZSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9maW5kIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2dyb3VwcyIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9oZWFkIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2lkIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2tpbGxhbGwiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vbGFzdCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9sYXN0bG9nIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2xlc3MiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vbG9jYXRlIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2xvZ2dlciIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9sc2F0dHIiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vbHNvZiIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9tYWlsIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL21kNXN1bSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9tbG9jYXRlIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL25ld2dycCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9wYXNzd2QiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vcGdyZXAiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vcGtpbGwiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vcHN0cmVlIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3JraHVudGVyIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3J1bmNvbiIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9zaGExc3VtIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3NoYTIyNHN1bSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9zaGEyNTZzdW0iIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vc2hhMzg0c3VtIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3NoYTUxMnN1bSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi9zb3J0IiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3N0YXQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vc3RyYWNlIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3N1ZG8iIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdGFpbCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi90ZWxuZXQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdGVzdCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi90b3AiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdG91Y2giIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdHIiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdW5pcSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi91c2VycyIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi92bXN0YXQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdyIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi93YXRjaCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi93YyIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi93aGF0aXMiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vd2hlcmVpcyIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi93aGljaCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvdXNyL2Jpbi93aG8iIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vd2hvYW1pIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL2dhd2siIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vYnNkLW1haWx4IiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii91c3IvYmluL3RlbG5ldC5uZXRraXQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3Vzci9iaW4vdy5wcm9jcHMiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vZGVwbW9kIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9zYmluL2ZzY2siIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vaWZjb25maWciIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vaWZkb3duIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9zYmluL2lmdXAiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vaW5zbW9kIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9zYmluL2xzbW9kIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9zYmluL21vZGluZm8iIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vbW9kcHJvYmUiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vcm1tb2QiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vcm91dGUiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL3NiaW4vc3Vsb2dpbiIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvc2Jpbi9zeXNjdGwiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9iYXNoIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vY2F0IiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vY2htb2QiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9jaG93biIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL2NwIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vZGF0ZSIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL2RmIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vZG1lc2ciIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9lY2hvIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vZWQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9lZ3JlcCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL2ZncmVwIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vZnVzZXIiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9ncmVwIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4va2lsbCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL2xlc3MiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9sb2dpbiIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL2xzIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vbHNtb2QiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9ta3RlbXAiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9tb3JlIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vbW91bnQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9tdiIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL25ldHN0YXQiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9waW5nIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vcHMiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9wd2QiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9yZWFkbGluayIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL3NlZCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL3NoIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vc3UiIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi90b3VjaCIgc3RhdHVzPSJPSyIvPg0KICAgICAgICA8cmVjb3JkIHZhbHVlPSIvYmluL3VuYW1lIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vd2hpY2giIHN0YXR1cz0iT0siLz4NCiAgICAgICAgPHJlY29yZCB2YWx1ZT0iL2Jpbi9rbW9kIiBzdGF0dXM9Ik9LIi8+DQogICAgICAgIDxyZWNvcmQgdmFsdWU9Ii9iaW4vZGFzaCIgc3RhdHVzPSJPSyIvPg0KICAgIDwvcmVjb3Jkcz4NCiAgICA8ZXJyb3JzPg0KICAgICAgICA8ZXJyb3IgZGVzY3JpcHRpb249Ii91c3Ivc2Jpbi9zc2hkIiB2YWx1ZT0iV2FybmluZyIvPg0KICAgICAgICA8ZXJyb3IgZGVzY3JpcHRpb249Ii91c3IvYmluL2N1cmwiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL3Vzci9iaW4vZHBrZyIgdmFsdWU9Ildhcm5pbmciLz4NCiAgICAgICAgPGVycm9yIGRlc2NyaXB0aW9uPSIvdXNyL2Jpbi9kcGtnLXF1ZXJ5IiB2YWx1ZT0iV2FybmluZyIvPg0KICAgICAgICA8ZXJyb3IgZGVzY3JpcHRpb249Ii91c3IvYmluL2xkZCIgdmFsdWU9Ildhcm5pbmciLz4NCiAgICAgICAgPGVycm9yIGRlc2NyaXB0aW9uPSIvdXNyL2Jpbi9wZXJsIiB2YWx1ZT0iV2FybmluZyIvPg0KICAgICAgICA8ZXJyb3IgZGVzY3JpcHRpb249Ii91c3IvYmluL3NpemUiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL3Vzci9iaW4vc3NoIiB2YWx1ZT0iV2FybmluZyIvPg0KICAgICAgICA8ZXJyb3IgZGVzY3JpcHRpb249Ii91c3IvYmluL3N0cmluZ3MiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL3Vzci9iaW4vd2dldCIgdmFsdWU9Ildhcm5pbmciLz4NCiAgICAgICAgPGVycm9yIGRlc2NyaXB0aW9uPSIvdXNyL2Jpbi94ODZfNjQtbGludXgtZ251LXNpemUiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL3Vzci9iaW4veDg2XzY0LWxpbnV4LWdudS1zdHJpbmdzIiB2YWx1ZT0iV2FybmluZyIvPg0KICAgICAgICA8ZXJyb3IgZGVzY3JpcHRpb249Ii9zYmluL2luaXQiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL3NiaW4vaXAiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL3NiaW4vcnVubGV2ZWwiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL2Jpbi9pcCIgdmFsdWU9Ildhcm5pbmciLz4NCiAgICAgICAgPGVycm9yIGRlc2NyaXB0aW9uPSIvYmluL3N5c3RlbWQiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL2Jpbi9zeXN0ZW1jdGwiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgICAgIDxlcnJvciBkZXNjcmlwdGlvbj0iL2xpYi9zeXN0ZW1kL3N5c3RlbWQiIHZhbHVlPSJXYXJuaW5nIi8+DQogICAgPC9lcnJvcnM+DQo8L291dHB1dD4=")

if __name__ == "__main__":
    main()
