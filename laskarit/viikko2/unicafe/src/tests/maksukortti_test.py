import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_kortin_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 15.00 euroa")

    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 5.00 euroa")

    def test_palauttaa_true_jos_rahaa_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_palauttaa_false_jos_raha_ei_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1500))
