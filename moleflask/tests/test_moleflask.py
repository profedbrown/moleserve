import os
from moleflask import mflask
import unittest

class MoleFlaskTestCase(unittest.TestCase):

    def setUp(self):
        mflask.app.testing = True
        self.app = mflask.app.test_client()

    def test_salt(self):
       rv = self.app.post('/givemass', data=dict(
           whatmolecule='NaCl',
       ), follow_redirects=True)
       assert b'NaCl' in rv.data
       assert b'58.44' in rv.data

if __name__ == '__main__':
    unittest.main()
