import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_luomisessa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_luomisessa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_luomisessa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_raha_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_maukas_raha_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_edullinen_raha_ei_riita_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateisosto_maukas_raha_ei_riita_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_kateisosto_edulliset_lisaantyvat(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_maukkaat_lisaantyvat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_edulliset_ei_lisaanny_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukkaat_ei_lisaanny_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_kateisosto_maukas_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kortti_edullinen_raha_riittaa(self):
        kortti = Maksukortti(500)

        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_kortti_maukkaasti_raha_riittaa(self):
        kortti = Maksukortti(500)

        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_kortti_edullinen_raha_ei_riita(self):
        kortti = Maksukortti(200)

        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_kortti_maukkaasti_raha_riittaa(self):
        kortti = Maksukortti(200)

        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_kortti_edullinen_raha_riittaa_edulliset_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortti_maukas_raha_riittaa_maukkaat_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortti_edullinen_raha_riittaa_edulliset_kasvaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortti_maukas_raha_riittaa_maukkaat_kasvaa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_raha_ei_muutu_edullisella_korttiostolla(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_raha_ei_muutu_maukkaalla_korttiostolla(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataaminen_kasvattaa_kortin_saldoa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)

        self.assertEqual(kortti.saldo, 500)

    def test_kortin_lataaminen_kasvattaa_kassan_rahaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortin_lataaminen_ei_kasvata_kortin_saldoa_negatiivisella_summalla(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1000)

        self.assertEqual(kortti.saldo, 0)

    def test_kortin_lataaminen_ei_kasvata_kassan_rahaa_negatiivisella_summalla(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataaminen_negatiivisella_ei_palauta_arvoa(self):
        kortti = Maksukortti(0)
        self.assertIsNone(self.kassapaate.lataa_rahaa_kortille(kortti, -1000))
