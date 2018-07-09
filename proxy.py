#!/usr/bin/python
# Install with `sudo pip install scapy` and `sudo pip install scapy-http`

import re
from scapy.all import IP
from scapy.packet import Raw
from scapy.all import sniff
from scapy_http import http
import datetime


# Make sure device under router mode - sys.ipv4_forward = 1
# Only sniffer all url with params
# Emulate all requests after all records (with sulley)

class Inspector(object):
    """
    Make sure your gateway settings in correct!
    """

    def __init__(self):
        self.enc_alert = 0
        self.http_layer = None
        self.ip_layer = None
        self.tmpfile = open('test.urls', 'w', 0)  # No buffer, write to file immediately
        self.urls = []

    def dispatch_url(self, packet):
        """
        Dispatch URLs from packet. (Use SSLStrip for decrypt HTTPs sessions in manual)
        :param packet: <Object> L3 packets
        :return: None
        """
        try:
            if packet[IP].dport == 443 and self.enc_alert == 0:
                print "{0} - Encrypted - {1}".format(datetime.datetime.now(), packet[IP].dst)
                self.enc_alert = 1
        except IndexError:
            pass

        if packet.haslayer(http.HTTPRequest):
            # print http_layer.fields
            http_layer = packet.getlayer(http.HTTPRequest)
            raw_data = packet.getlayer(Raw)
            # print packet
            if http_layer.fields["Method"] == "GET" and re.findall(r'[=,&]', http_layer.fields["Path"]):
                # Store JSON (http fields and URL)
                print '{0} - {1[Method]} - http://{1[Host]}{1[Path]}'.format(datetime.datetime.now(),
                                                                             http_layer.fields)
                self.tmpfile.write('{0} - {1[Method]} - http://{1[Host]}{1[Path]}\n'.format(datetime.datetime.now(),
                                                                                            http_layer.fields))
                self.tmpfile.write(str(http_layer.fields))

            if http_layer.fields["Method"] == "POST":
                # Store JSON and raw_data
                print '{0} - {1[Method]} - http://{1[Host]}{1[Path]}'.format(datetime.datetime.now(),
                                                                             http_layer.fields)
                if re.findall(r'[=,&]', str(raw_data)+'\n'):
                    print raw_data

                self.tmpfile.write(
                    '{0} - {1[Method]} - http://{1[Host]}{1[Path]} - {2}\n'.format(datetime.datetime.now(),
                                                                                   http_layer.fields, raw_data))
                self.tmpfile.write(str(http_layer.fields)+'\n')

        # HTTPS not only working on 443
        if packet.haslayer(http.HTTPResponse):
            # Audit response data in the future!
            try:
                print '{0} - Got Response! - {1}'.format(datetime.datetime.now(), packet[IP].src)
            except IndexError:
                pass

    def run(self, ipdst=None, dstport=None):
        # Compile BPF
        if ipdst == None and dstport == None:
            _BPF = 'tcp'
        else:
            pass  # Refer to wireshark
        sniff(filter=_BPF, prn=self.dispatch_url)

    def __del__(self):
        self.tmpfile.close()


if __name__ == "__main__":
    proxy = Inspector()
    proxy.run()
