import unittest
import logging
import sys
import Hand as hd


class TestHandSetup(unittest.TestCase):

    def test_shape(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        # log = logging.getLogger('TestHandSetup')
        # log.debug(hand.seq)
        self.assertEqual(hand.df.shape, (13, 5))

    def test_isStraight(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['STRAIGHT'])

        hstr = '7C 6S 5C 8H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['STRAIGHT'])

    def test_isFlush(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['FLUSH'])

        hstr = '7C 6C KC 8C 4C'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['FLUSH'])

    def test_isStraightFlush(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['STRAIGHT_FLUSH'])

        hstr = '7C 6C 5C 8C 4C'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['STRAIGHT_FLUSH'])

    def test_is4Kind(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['4_KIND'])

        hstr = '7C 7S 7H 8H 7D'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['4_KIND'])

    def test_is3Kind(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['3_KIND'])

        hstr = '7C 7S 7H 8H 2D'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['3_KIND'])

    def test_is2Pair(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['2_PAIR'])

        hstr = '7C 7S 8C 8H 6D'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['2_PAIR'])

    def test_is1Pair(self):
        hstr = '8C TS KC 9H 4S'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertNotEqual(hv, hd.Hand.HAND_TYPE_VALS['1_PAIR'])

        hstr = '5C 4S 7H 3H 7D'.split(' ')
        hand = hd.Hand(hstr)
        hv = hand.hand_type()
        self.assertEqual(hv, hd.Hand.HAND_TYPE_VALS['1_PAIR'])


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger('TestHandSetup').setLevel(logging.DEBUG)
    unittest.main()
