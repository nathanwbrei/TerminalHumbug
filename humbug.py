from flask import Flask, request
import json
import sys

app = Flask(__name__)

@app.route('/humbug', methods=['POST'])
def humbug():
    data = json.JSONDecoder().decode(request.data)

    for d in data:
        sys.stdout.flush()
        if d['stream']:
            header = "%s ==> %s" % (d['stream'][0], d['subject'][0])
            header=header.encode("UTF-8")
            print '='*len(header)
            print header
            print '='*len(header)
            print
        if d['name']:
            name = "%s @%s" % (d['name'][0], d['time'][0])
            name=name.encode("UTF-8")
            print name
            print "-" * len(name)
        if d['message']:
            print d['message'][0].encode("UTF-8")
        sys.stdout.flush()

    return "Thanks!"

if __name__ == "__main__":
    sys.stderr = open('/dev/null')
    print "Welcome to Terminal Humbug!"
    sys.stdout.flush()

    app.run()



