#!/usr/bin/env python

from flask import Flask, request
from subprocess import Popen
import json
import sys
import argparse

app = Flask(__name__)

@app.route('/humbug', methods=['POST'])
def humbug():
    data = json.JSONDecoder().decode(request.data)

    for d in data:
        sys.stdout.flush()
        if d['stream']:
            header = "%s : %s" % (d['stream'][0].upper(), d['subject'][0])
            header=header.encode("UTF-8")
            print '='*len(header)
            print header
            print '='*len(header)
            print
            if args.say:
                run('say "' + header + '"')

        if d['name']:
            name = "%s @%s" % (d['name'][0], d['time'][0])
            name=name.encode("UTF-8")
            print name
            print "-" * len(name)
            if args.say:
                run('say "' + name + '"')

        if d['message']:
            message = d['message'][0].encode("UTF-8")
            print message
            if args.say:
                run('say "' + message + '"')
    sys.stdout.flush()
    return "Thanks!"

def run(str):
    sys.stdout.flush()
    Popen([str]).communicate()
    sys.stdout.flush()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Scrape Humbug messages.')

    parser.add_argument('-v','--verbose', action='store_true', help="Show STDERR")
    parser.add_argument('-s', '--say', action='store_true', help='Pipe to OSX say command')
    parser.add_argument('-w', dest='outfile', help='Write to JSON file')

    args = parser.parse_args()

    if not args.verbose:
        sys.stderr = open('/dev/null')

    print "Welcome to Terminal Humbug!"
    sys.stdout.flush()

    app.run()

