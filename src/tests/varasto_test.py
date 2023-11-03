import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(0, alku_saldo = 1)
        self.varasto3 = Varasto(10, alku_saldo = -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_tilavuus_nolla_jos_alku_tilavuus_pienempi_kuin_nolla(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_alku_saldo_pienempi_kuin_nolla(self):
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_alku_saldo_pienempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_tavaraa_varastoon_varasto_taynna(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_liikaa_tavaraa_varastoon_ei_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisataan_negatiivinen_maara_varastoon_ei_pienenna_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisataan_negatiivinen_maara_varastoon_saldo_ei_muutu(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_paljon_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(saatu_maara, 5)

    def test_liian_paljon_ottaminen_palauttaa_oikean_saldon(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_paljon_ottaminen_vapauttaa_tilaa(self):
        self.varasto.lisaa_varastoon(5)

        self.varasto.ota_varastosta(6)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_otetaan_negatiivinen_maara_varastosta_otetaan_nolla(self):
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_otetaan_negatiivinen_maara_varastosta_tilaa_ei_vapaudu(self):
        self.varasto.lisaa_varastoon(1)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 9)

    def test_otetaan_negatiivnen_maara_varastosta_saldo_ei_muutu(self):
        self.varasto.lisaa_varastoon(2)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_palauttaa_merkkijonon(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
