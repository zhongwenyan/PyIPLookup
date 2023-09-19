#!/usr/bin/env python3

import sys
import argparse
import json
import ipaddress
import urllib.parse
import http.client

def is_valid_ip(ip):
    try:
        ipaddress_object = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', metavar='Your IP2Location.io API key.')
    parser.add_argument('-p', '--ip', metavar='Specify an IP address.')
    # parser.add_argument('-l', '--lang', metavar='Translation information(ISO639-1) for continent, country, region and city name.')

    return parser

def print_usage():
    print(
"ip2location.io -p [IP ADDRESS] -k [ip2location.io API key]\n"
"\n"
"   -k, --key\n"
"       IP2Location.io API key. Free API key is available through sign up in their website.\n"
"\n"
"   -p, --ip\n"
"   Specify an IP address query (Supported IPv4 and IPv6 address).\n"
"\n"
"   -h, -?, --help\n"
"   Display the help.\n")

def ip2locationio_lookup(key, ip, language=''):
    if is_valid_ip(ip):
        parameters = urllib.parse.urlencode((("key", key), ("ip", ip), ("format", "json"), ("lang", language)))
        conn = http.client.HTTPSConnection("api.ip2location.io")
        conn.request("GET", "/?" + parameters)
        res = conn.getresponse()
        # response = json.loads(res.read())
        # return response
        print(res.read().decode('utf-8'))
    else:
        print("Invalid IP address detected.")

if __name__ == '__main__':
# def main():
    is_help = False
    # print(sys.argv)
    if len(sys.argv) >= 2:
        for index, arg in enumerate(sys.argv):
            if arg in ['--help', '-h', '-?']:
                print_usage()
                is_help = True
        if is_help is False:
            parser = create_parser()
            args = parser.parse_args(sys.argv[1:])
            # print(args)
            if args.key is not None and args.ip is not None:
                ip2locationio_lookup(args.key, args.ip)
            elif args.key is None:
                print("Missing API key.")
            elif args.ip is None:
                print("Missing IP address.")
    else:
        print("Missing parameters. Please enter 'ip2location.io -h' for more information.")