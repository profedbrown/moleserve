import unittest
from moleflask.molecule import Molecule

class TestMoleculeMethods(unittest.TestCase):

    def setUp(self):
        self.water = Molecule('H2O')
        self.salt = Molecule('NaCl')
        self.ammoniumdichromate = Molecule('(NH4)2Cr2O7')

    def test_mass_water(self):  
        self.assertAlmostEqual(self.water.mass(), 18.0148, msg="water mass incorrect")

    def test_mass_badsymbols(self):
        badsalt = Molecule('NalC')
        with self.assertRaises(KeyError):
                 badsalt.mass()

    def test_check_symbols(self):
        self.assertTrue( self.salt.check_symbols() )
        self.assertTrue( self.water.check_symbols() )       

    def test_clean_f(self):
        badammoniumdichromate = Molecule('(NH4)2Cr2XqO7')
        fixed = badammoniumdichromate.clean_copy()
        self.assertTrue( fixed.check_symbols() )
        self.assertEqual( str(fixed), '(NH4)2Cr2O7' )

if __name__ == '__main__':
    unittest.main()

