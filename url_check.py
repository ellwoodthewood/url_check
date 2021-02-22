#!/usr/bin/python3
# Usage: url_check.py -u http://google.com 
# I just learned about rich, and saw this twitter post: 
# https://twitter.com/TimMedin/status/1363956188975661056
# so I decided to write a simple script for commandline,
# because that's where I'm most comfortable.
### To do: Add -i, --input to use readlines() for a text file containing multiple URLs
### To do: Add error control (if you type ./url.py http:blah, it doesn't check that you forgot the -u 


from rich import inspect
import requests
import sys, getopt

argumentList = sys.argv[1:]

# Options
options = "hu:"

# Long options
long_options = ["help", "url"]

try:
    # Parsing args
    arguments, values = getopt.getopt(argumentList, options, long_options)
    
    # checking args
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print ("Usage: ", sys.argv[0], " -u | --url https://something")
        elif currentArgument in ("-u", "--url"):
            url = currentValue
            r = requests.get(url, verify=False)
            # I set this to verify=False because I tend to check a lot of self-signed cert websites
            print (inspect(r))
except getopt.error as err:
    # output error and return
    print (str(err))