import numpy as np
import pandas as pd


class Hand:

    CARD_VALS = ['23456789TJQKA'[i] for i in range(13)]
    SUIT_VALS = ['CDHS'[i] for i in range(4)]

    HAND_TYPE_VALS = {'STRAIGHT_FLUSH': 1 << 11,
                      '4_KIND': 1 << 10,
                      'FULL_HOUSE': 1 << 9,
                      'FLUSH': 1 << 8,
                      'STRAIGHT': 1 << 7,
                      '3_KIND': 1 << 6,
                      '2_PAIR': 1 << 5,
                      '1_PAIR': 1 << 4,
                      'HIGH_CARD': 1 << 3}

    def __init__(self, hstr):
        self.hstr = hstr
        harr = np.zeros((13, 4), dtype=np.int)
        for card in hstr:
            harr[Hand.CARD_VALS.index(card[0]),
                 Hand.SUIT_VALS.index(card[1])] = 1
        self.harr = harr

        df = pd.DataFrame(harr, columns=Hand.SUIT_VALS)
        df = df.transpose()
        df.columns = Hand.CARD_VALS
        df = df.transpose()
        df['TOT'] = df.sum(axis=1)
        self.seq = ''.join(['{}'.format(x) for x in df['TOT']])
        self.df = df

    def hand_type(self):
        hv = 0

        suits = self.df.drop('TOT', axis=1).sum()
        if suits.max() == 5:
            hv = Hand.HAND_TYPE_VALS['FLUSH']
        if '11111' in self.seq:
            hv = Hand.HAND_TYPE_VALS['STRAIGHT']
        if '11111' in self.seq and suits.max() == 5:
            hv = Hand.HAND_TYPE_VALS['STRAIGHT_FLUSH']
        if hv > 0:
            return hv

        sig = self.seq.replace('0', '').replace('1', '')
        if sig == '4':
            hv = Hand.HAND_TYPE_VALS['4_KIND']
        elif sig == '3':
            hv = Hand.HAND_TYPE_VALS['3_KIND']
        elif sig == '2':
            hv = Hand.HAND_TYPE_VALS['1_PAIR']
        elif sig == '22':
            hv = Hand.HAND_TYPE_VALS['2_PAIR']
        elif sig == '23' or sig == '32':
            hv = Hand.HAND_TYPE_VALS['FULL_HOUSE']
        return hv


def main():
    h = '8C TS KC 9H 4S'.split(' ')
    h1 = Hand(h)
    print(h1.df)
    print(h1.hand_type())


if __name__ == "__main__":
    main()
