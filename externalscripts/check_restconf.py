#! /usr/bin/env python
"""
A script to test to see if RESTCONF is reachable on a host.

Author: Hank Preston 
"""

from nso_tests import test_restconf


# Script entry point
if __name__ == "__main__":
    import argparse

    # Use argparse to determine the host to check : https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description="Test RESTCONF Functional")
    parser.add_argument("--host", type=str, help="Network host to test")
    parser.add_argument(
        "--port", type=int, help="The port RESTCONF runs on. Default 443", default=443
    )
    parser.add_argument(
        "--path",
        type=str,
        help="The resource path to check. Default ",
        default="/.well-known/host-meta",
    )
    args = parser.parse_args()

    if args.host is None:
        print(f"Missing required parameters for test. host={args.host}")
        exit(1)

    result = test_restconf(args.host, args.port, args.path)

    if result == 200:
        print(f"RESTCONF running on host {args.host}")
    else:
        print(f"ERROR: RESTCONF unreachable.")
