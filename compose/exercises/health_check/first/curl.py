#!/usr/bin/env python

import requests
import sys
import argparse

def send_get_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        print(f"Response Status Code: {response.status_code}")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Body:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A curl-like tool for GET requests using the requests library")
    parser.add_argument('url', help="The URL to send the GET request to")
    parser.add_argument('-H', '--headers', nargs='*', help="HTTP headers (e.g., -H 'Content-Type: application/json')")

    args = parser.parse_args()

    headers = {}
    if args.headers:
        for header in args.headers:
            key, value = header.split(':', 1)
            headers[key.strip()] = value.strip()

    send_get_request(args.url, headers)
