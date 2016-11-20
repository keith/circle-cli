from src.helpers import credentials
import tempfile
import unittest

class TestCredentials(unittest.TestCase):
    def test_netrc_credentials(self):
        path = _mktempfile("machine {}\n\tlogin foo\n\tpassword bar\n"
                           .format(credentials.MACHINE))
        token = credentials.credentials(path=path)
        self.assertEqual(token, "bar")

def _mktempfile(text):
    _, name = tempfile.mkstemp()
    with open(name, "w+") as f:
        f.write(text)
    return name
