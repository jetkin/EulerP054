# hands = open('p054_test.txt', 'r')

# for deal in hands:
#     cards = deal.strip().split(' ')
#     h = cards[0:5]
#     # h2 = cards[5:10]
#     print(h)
#     h1 = hd.Hand(h)
#     print(h1.harr)

# hands.close()

hands = open('p054_test.txt', 'r')

for deal in hands:
    cards = deal.strip().split(' ')
    h = cards[0:5]
    # h2 = cards[5:10]
    print(h)
    h1 = Hand(h)
    print(h1.harr)

hands.close()
# 7D 2S 5D 3S AC
# 5C AD 5D AC 9C 7C 5H 8D TD KS
# 3H 7H 6S KC JS QH TD JC 2D 8S
# TH 8H 5C QS TC 9H 4D JC KS JS
# 7C 5H KC QH JD AS KH 4C AD 4S
# 5H KS 9C 7D 9H 8D 3S 5D 5C AH
# 6H 4H 5C 3H 2H 3S QH 5S 6S AS
# TD 8C 4H 7C TC KC 4C 3H 7S KS
# 7C 9C 6D KD 3H 4C QS QC AC KH
# JC 6S 5H 2H 2D KD 9D 7C AS JS
