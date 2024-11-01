import rat
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = dict()

    def setUp(self):
        self.Usain = rat.Runner('Usain', 10)
        self.Andrey = rat.Runner('Andrey', 9)
        self.Nik = rat.Runner('Nik', 3)



    def test_Tournament_all(self):
        turnament = rat.Tournament(90, self.Usain, self.Andrey, self.Nik)
        self.all_results = turnament.start()
        self.assertTrue(self.all_results[len(self.all_results)], 'Nik')
        TournamentTest.all_results.update(self.all_results)

    def test_Tournament_Usain_and_Nik(self):
        turnament = rat.Tournament(90, self.Usain, self.Nik)
        self.all_results = turnament.start()
        self.assertTrue(self.all_results[len(self.all_results)], 'Nik')
        TournamentTest.all_results.update(self.all_results)

    def test_Tournament_Annrey_and_Nik(self):
        turnament = rat.Tournament(90, self.Andrey, self.Nik)
        self.all_results = turnament.start()
        self.assertTrue(self.all_results[len(self.all_results)], 'Nik')
        TournamentTest.all_results.update(self.all_results)


    def tearDown(self):
        print(self.all_results)


