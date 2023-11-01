#if you want to test within class, import unittest and inheritance from it
import unittest

#pytest test with function start from head of test
import pytest_cov

import hw4

#unittest
# with basic concepts of input and output
#use expected output compare with output from tested function
#assert if is wrong
#########################  Quetion1 ##################################
class TestPatient(unittest.TestCase):

    #class method setUpClass$tearDownClass
    #classmethod represents the state of the class:begin->...->end
    #print for each time creating TestClass at the beginning of object and ending of object
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    #in order to decrease duplicate
    #we use setUp default method before each test_method to start test
    #setup contains the instantiate of tested class members
    def setUp(self):
        print("setup")
        self.patient_Bruce = hw4.Patient("Bruce", 'fluid')
        self.patient_Smith = hw4.Patient("Smith",['neck stiffness','irritability'])
        self.patient_John = hw4.Patient("John", ['fever', 'cough', 'anosmia'])
        self.patient_Saly = hw4.Patient("Saly",['fever', 'cough', 'anosmia','fever', 'cough', 'anosmia'])
        #['fever', 'cough', 'anosmia']
    #in order to decrease duplicate
    #we use tearDown default method after each test_method to start test
    #setup contains the instantiate of tested class members
    def tearDown(self):
        print("teardown\n")
        #refresh test variable
        self.patient_Bruce = hw4.Patient("Bruce", 'fluid')
        self.patient_Smith = hw4.Patient("Smith",['neck stiffness','irritability'])
        self.patient_John = hw4.Patient("John", ['allergies'])
        self.patient_Saly = hw4.Patient("Saly",['fever', 'cough', 'anosmia','fever', 'cough', 'anosmia'])

    #test with no input of Patient instantiate
    def test_Patient_wiht_string_and_Array_instantiate(self):
        #Bruce,'fluid'
        self.assertEqual(self.patient_Bruce.name,"Bruce")
        self.assertEqual(self.patient_Bruce._symptoms,['fluid'])

        #Bruce,'fluid'
        self.assertEqual(self.patient_Smith.name,"Smith")
        self.assertEqual(self.patient_Smith._symptoms,['neck stiffness','irritability'])

        #assertRaises()
        #(Error we expected, funtion we desired to test, arguments to pass)
        #self.assertRaises(ValueError, self.patient_test1.add_test,["fever"])
    
    #test with no input of Patient instantiate
    def test_Patient_Add_test(self):
        test_sets = ['x_ray','covid','covid'] 
        result_sets = [True, False,True]

        #add_test
        for t,r in zip(test_sets,result_sets):
            self.patient_Bruce.add_test(t,r)

        #assert check add
        n = len(test_sets)
        for i in range(n):
            self.assertEqual(self.patient_Bruce._test[i],test_sets[i])
            self.assertEqual(self.patient_Bruce._result[i],result_sets[i])

    def test_has_covid_with_covid_other_test_and_symptos_situations(self):
        test_sets = ['x_ray','covid']
        result_sets = [True,True]
        #add_test
        for t,r in zip(test_sets,result_sets):
            self.patient_Bruce.add_test(t,r)

        test_sets2 = ['x_ray','covid']
        result_sets2 = [True, False]
        #add_test
        for t,r in zip(test_sets2,result_sets2):
            self.patient_Smith.add_test(t,r)

        test_sets3 = ['x_ray']
        result_sets3 = [True]
        #add_test
        for t,r in zip(test_sets3,result_sets3):
            self.patient_John.add_test(t,r)

        test_sets4 = ['x_ray']
        result_sets4 = [True]
        #add_test
        for t,r in zip(test_sets4,result_sets4):
            self.patient_Saly.add_test(t,r)

         #assert check
            #covid 
            #covid with covid true test
            self.assertEqual(self.patient_Bruce.has_covid(),0.99)
            #covid with covid false test
            self.assertEqual(self.patient_Smith.has_covid(),0.01)
            #Smith take another covid test and result is True
            self.patient_Smith.add_test('covid',True)
            self.assertEqual(self.patient_Smith.has_covid(),0.99)

            #three covid synptomss
            self.assertEqual(self.patient_John.has_covid(),0.35)
            #three covid synptoms, check with repeatbility
            self.assertEqual(self.patient_Saly.has_covid(),0.35)
#########################  Quetion2 ##################################
class TestCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    #instantiate mock object
    def setUp(self):
        print("setup")
        self.card = hw4.Card('Heart','A')
        
    def tearDown(self):
        print("teardown\n")
        #refresh test variable
        self.card = hw4.Card('Heart','A')

    #test Card
    def test_Card_instantiate(self):
        self.assertEqual(self.card._suit,'Heart')
        self.assertEqual(self.card._value,'A')
    #test Card
    def test_Card_instantiate(self):
        self.assertEqual(self.card._suit,'Heart')
        self.assertEqual(self.card._value,'A')
    #getter
    def test_Card_gettr(self):
        self.assertEqual(self.card.accessSuit(),'Heart')
        self.assertEqual(self.card.accessValue(),'A')
    

class TestEnglishDeck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    
    #append four suits type of cards by input Value
    def _appendCards(self, suitValue):
        HeartsCard = hw4.Card("Hearts",suitValue)
        DiamondsCard = hw4.Card("Diamonds",suitValue)
        ClubsCard = hw4.Card("Clubs",suitValue)
        SpadesCard = hw4.Card("Spades",suitValue)

        self._cards.append(HeartsCard)
        self._cards.append(DiamondsCard)
        self._cards.append(ClubsCard)
        self._cards.append(SpadesCard)

    #create Deck
    def createDeck(self):
        #cards: 4 suits* 13 values
        #create card and append by 13 times loops.
        #each append 4 suits
        for i in range(1,14):
            #after we append Card, A,J,Q,K, we append card by numeric value
            if i == 1:
                self._appendCards("A")
            elif i == 11:
                self._appendCards("J")
            elif i == 12:
                self._appendCards("Q")
            elif i == 13:
                self._appendCards("K")
            else:
                #in Card class, we can access card Value by public function
                #and it only return string of value
                self._appendCards(i)
            
    #instantiate mock object
    def setUp(self):
        print("setup")
        self._cards = []
        self.createDeck()
        self.englishdeck = hw4.EnglishDeck()
        
    def tearDown(self):
        print("teardown\n")
        #refresh test variable
        self._cards = []
        self.createDeck()
        self.englishdeck = hw4.EnglishDeck()

    #test EnglishDeck instantiate
    def test_EnglishDeck_instantiate(self):
        engdeck = hw4.EnglishDeck()
        
        for i in range(len(self._cards)):
            self.assertEqual(engdeck._cards[i].accessSuit(),self._cards[i].accessSuit())
            self.assertEqual(engdeck._cards[i].accessValue(),self._cards[i].accessValue())
    
   
    #test EnglishDeck shuffle
    def test_EnglishDeck_shuffle(self):
        engdeck = hw4.EnglishDeck()
        engdeck.shuffle()
        
        self.assertNotEqual([engdeck._cards[0].accessSuit(),engdeck._cards[0].accessValue()],
                            [self._cards[0].accessSuit(),self._cards[0].accessValue()])

    #test EnglishDeck draw
    def test_EnglishDeck_draw(self):
        engdeck = hw4.EnglishDeck()
        for i in range(10):
            engdeck.draw()
            self._cards.pop(0)
        
        for i in range(len(self._cards)):
            self.assertEqual(engdeck._cards[i].accessSuit(),self._cards[i].accessSuit())
            self.assertEqual(engdeck._cards[i].accessValue(),self._cards[i].accessValue())
#several files---make sure its our file
if __name__ == '__main__':
    unittest.main()