#!/usr/bin/env python

import netrc
import sys

MACHINE = "circleci.com"


def credentials(path=None):
    auth = netrc.netrc(path).authenticators(MACHINE)
    if auth is None:
        sys.exit("Add %s to your ~/.netrc" % MACHINE)

    return auth[2]
