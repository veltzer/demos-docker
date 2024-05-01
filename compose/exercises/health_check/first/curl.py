#!/usr/bin/env python

"""
Curl like tool in python
"""

import sys
import argparse
import requests


def send_get_request(url, headers=None):
    """ this function does most of the heavy lifting """
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        print(f"Response Status Code: {response.status_code}")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Body:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """ main entry point """
    parser = argparse.ArgumentParser(
            description="curl-like tool for GET requests"
    )
    parser.add_argument(
        "url",
        help="The URL to send the GET request to",
    )
    parser.add_argument(
        "-H",
        "--headers",
        nargs="*",
        help="HTTP headers (e.g., -H \"Content-Type: application/json\")",
    )

    args = parser.parse_args()

    headers = {}
    if args.headers:
        for header in args.headers:
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()

    send_get_request(args.url, headers=headers)


if __name__ == "__main__":
    main()
