#!/usr/env/python2
import signal
from proxy import Inspector
from snipper import urlsnip
from sender import repeater

if __name__ == "__main__":
    filename = "test.urls"


    def stop(signum, frame):
        if urlsnip(filename):
            repeater()


    signal.signal(signal.SIGINT, stop)
    sniff = Inspector()
    sniff.run()
