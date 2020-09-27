#!/usr/bin/env python

# Author: Steve Wolfman
# License: CC-By-Sa 3.0 https://creativecommons.org/licenses/by-sa/3.0/
# You are free to use, modify, and distribute this code as long as (roughly) you
# include a CC-By-Sa license and acknowledge the author(s)' contributions.
#
# Description: Some code to support the card trick at
# http://www.cs.ubc.ca/~wolf/teaching/card-trick-notes.html

import math
import unittest
import random

SUITS = {"C" : 0, "D" : 1, "H" : 2, "S" : 3}
REV_SUITS = dict([(value, key) for (key, value) in SUITS.items()])
RANKS = {"A" : 0, "2" : 4, "3" : 8, "4" : 12, "5" : 16, "6" : 20, \
         "7" : 24, "8" : 28, "9" : 32, "T" : 36, "J" : 40, "Q" : 44, "K" : 48}
REV_RANKS = dict([(value, key) for (key, value) in RANKS.items()])



# RS string -> [0,51]
#
# Given a rank/suit string like AC, 2H, TD, or KS (A, 2-9, T, J, Q, K
# and C, D, H, S), returns our chosen canonical card number for that
# card.
def card_to_number(card):
    assert len(card) == 2 and card[0] in RANKS and card[1] in SUITS, \
           "{0} is not a string of the form RS, where R is a rank A, 2-9, T, J, Q, or K and S is a suit C, D, H, or S".format(card)

    return RANKS[card[0]] + SUITS[card[1]]

class CardToNumberTests(unittest.TestCase):
    def testAces(self):
        self.assertEqual(card_to_number("AC"), 0)
        self.assertEqual(card_to_number("AD"), 1)
        self.assertEqual(card_to_number("AH"), 2)
        self.assertEqual(card_to_number("AS"), 3)

    def testSevens(self):
        self.assertEqual(card_to_number("7C"), 24)
        self.assertEqual(card_to_number("7D"), 25)
        self.assertEqual(card_to_number("7H"), 26)
        self.assertEqual(card_to_number("7S"), 27)

    def testRanks(self):
        for i in range(2,10):
            self.assertEqual(card_to_number("{0}C".format(i)), (i-1)*4)
        self.assertEqual(card_to_number("TC"), 36)
        self.assertEqual(card_to_number("JC"), 40)
        self.assertEqual(card_to_number("QC"), 44)
        self.assertEqual(card_to_number("KC"), 48)



def number_to_card(num):
    assert 0 <= num and num < 52
    suit = num % 4
    rank = num - suit
    return REV_RANKS[rank] + REV_SUITS[suit]



class NumberToCardTests(unittest.TestCase):
    def testAces(self):
        self.assertEqual(number_to_card(0), "AC")
        self.assertEqual(number_to_card(1), "AD")
        self.assertEqual(number_to_card(2), "AH")
        self.assertEqual(number_to_card(3), "AS")

    def testSevens(self):
        self.assertEqual(number_to_card(24), "7C")
        self.assertEqual(number_to_card(25), "7D")
        self.assertEqual(number_to_card(26), "7H")
        self.assertEqual(number_to_card(27), "7S")

    def testRanks(self):
        for i in range(2,10):
            self.assertEqual(number_to_card((i-1)*4), "{0}C".format(i))
        self.assertEqual(number_to_card(36), "TC")
        self.assertEqual(number_to_card(40), "JC")
        self.assertEqual(number_to_card(44), "QC")
        self.assertEqual(number_to_card(48), "KC")


# seq(number) number -> number
#
# Given a set of numbers, returns the highest number in the set if
# it's no more than limit higher than the second highest number; else
# chooses the lowest
def choose_high_low(set, limit):
    assert len(set) > 1
    highest = max(set)
    second_highest = max([x for x in set if x != highest])
    if highest - second_highest > limit:
        return min(set)
    else:
        return highest


class ChooseHighLowTests(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(choose_high_low([0, 1], 1), 1)
        self.assertEqual(choose_high_low([0, 1], 0), 0)
        self.assertEqual(choose_high_low([1, 0], 1), 1)
        self.assertEqual(choose_high_low([1, 0], 0), 0)

    def testHands(self):
        self.assertEqual(choose_high_low([card_to_number("AC"),
                                          card_to_number("AD"),
                                          card_to_number("AH"),
                                          card_to_number("AS"),
                                          card_to_number("2C")],
                                         24), card_to_number("2C"))
        self.assertEqual(choose_high_low([card_to_number("AC"),
                                          card_to_number("AD"),
                                          card_to_number("AH"),
                                          card_to_number("AS"),
                                          card_to_number("KC")],
                                         24), card_to_number("AC"))
        self.assertEqual(choose_high_low([card_to_number("AC"),
                                          card_to_number("AD"),
                                          card_to_number("AH"),
                                          card_to_number("AS"),
                                          card_to_number("7S")],
                                         24), card_to_number("7S"))
        self.assertEqual(choose_high_low([card_to_number("AC"),
                                          card_to_number("AD"),
                                          card_to_number("AH"),
                                          card_to_number("AS"),
                                          card_to_number("8C")],
                                         24), card_to_number("AC"))


# seq(number) number -> seq(number)
#
# Given a set of numbers and a target offset, produces the canonical
# permutation representing that offset.  The target must be in
# range(1, math.factorial(len(set))+1).
def choose_permutation(set, target):
    assert target in range(1, math.factorial(len(set)) + 1)

    mutable_set = set[:]
    mutable_set.sort()
    result = []
    target = target - 1  # 0-based numbering
    while len(mutable_set) > 0:
        step_size = math.factorial(len(mutable_set)-1)
        result.append(mutable_set[target / step_size])
        del mutable_set[target / step_size]
        target = target % step_size
    return result

class ChoosePermutationTests(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(choose_permutation([], 1), [])
        self.assertEqual(choose_permutation([1], 1), [1])
        self.assertEqual(choose_permutation([0, 1], 1), [0, 1])
        self.assertEqual(choose_permutation([0, 1], 2), [1, 0])
        self.assertEqual(choose_permutation([1, 0], 1), [0, 1])
        self.assertEqual(choose_permutation([1, 0], 2), [1, 0])
        self.assertEqual(choose_permutation([0, 1, 2], 1), [0, 1, 2])
        self.assertEqual(choose_permutation([0, 1, 2], 2), [0, 2, 1])
        self.assertEqual(choose_permutation([0, 1, 2], 3), [1, 0, 2])
        self.assertEqual(choose_permutation([0, 1, 2], 4), [1, 2, 0])
        self.assertEqual(choose_permutation([0, 1, 2], 5), [2, 0, 1])
        self.assertEqual(choose_permutation([0, 1, 2], 6), [2, 1, 0])

    def testHands(self):
        self.assertEqual(choose_permutation([card_to_number("AC"),
                                               card_to_number("AD"),
                                               card_to_number("AH"),
                                               card_to_number("AS")],
                                              1), [card_to_number("AC"),
                                                   card_to_number("AD"),
                                                   card_to_number("AH"),
                                                   card_to_number("AS")])
        self.assertEqual(choose_permutation([card_to_number("AD"),
                                               card_to_number("AH"),
                                               card_to_number("AS"),
                                               card_to_number("KC")],
                                              4), [card_to_number("AD"),
                                                   card_to_number("AS"),
                                                   card_to_number("KC"),
                                                   card_to_number("AH")])
        self.assertEqual(choose_permutation([card_to_number("AC"),
                                               card_to_number("AD"),
                                               card_to_number("AH"),
                                               card_to_number("AS")],
                                              24), [card_to_number("AS"),
                                                    card_to_number("AH"),
                                                    card_to_number("AD"),
                                                    card_to_number("AC")])
        self.assertEqual(choose_permutation([card_to_number("AD"),
                                               card_to_number("AH"),
                                               card_to_number("AS"),
                                               card_to_number("8C")],
                                              24), [card_to_number("8C"),
                                                    card_to_number("AS"),
                                                    card_to_number("AH"),
                                                    card_to_number("AD")])



# seq(number) number -> (seq(number), number)
#
# Given a set of numbers and a modulus where the "trick" is possible
# (i.e., the numbers in the set are drawn from range(modulus) and
# math.factorial(len(set)-1)*2+len(set)-1 >= modulus), produces the
# canonical ordered permutation and hold-out card from the set.
#
# For convenience, we also require len(set) >= 2.  (Else, you're only
# doing the 1-card trick anyway!)
def perform_trick_numeric(set, modulus):
    assert all([x in range(modulus) for x in set])
    assert math.factorial(len(set)-1)*2 + len(set)-1 >= modulus

    # Choose the hold-out card based on the limit.
    limit = math.factorial(len(set)-1)
    hold_out = choose_high_low(set, limit)
    others = [x for x in set if x != hold_out]
    others.sort()

    # Choose the permutation.  Note: cannot recall if Python gives the
    # canonical result on range(modulus) or preserves sign somehow;
    # either way, this should work.
    target = (hold_out - others[-1] + modulus) % modulus
    return (hold_out, choose_permutation(others, target))


class PerformTrickNumericTests(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(perform_trick_numeric([0, 1], 2), (1, [0]))
        self.assertEqual(perform_trick_numeric([1, 0], 2), (1, [0]))

        self.assertEqual(perform_trick_numeric([0, 1, 2], 3), (2, [0, 1]))

        self.assertEqual(perform_trick_numeric([0, 1, 2], 4), (2, [0, 1]))
        self.assertEqual(perform_trick_numeric([0, 1, 3], 4), (3, [1, 0]))
        self.assertEqual(perform_trick_numeric([0, 2, 3], 4), (3, [0, 2]))
        self.assertEqual(perform_trick_numeric([1, 2, 3], 4), (3, [1, 2]))

        self.assertEqual(perform_trick_numeric([0, 1, 2], 6), (2, [0, 1]))
        self.assertEqual(perform_trick_numeric([0, 1, 3], 6), (3, [1, 0]))
        self.assertEqual(perform_trick_numeric([0, 1, 4], 6), (0, [4, 1]))
        self.assertEqual(perform_trick_numeric([0, 1, 5], 6), (0, [1, 5]))
        self.assertEqual(perform_trick_numeric([0, 2, 3], 6), (3, [0, 2]))
        self.assertEqual(perform_trick_numeric([0, 2, 4], 6), (4, [2, 0]))
        self.assertEqual(perform_trick_numeric([0, 2, 5], 6), (0, [2, 5]))
        self.assertEqual(perform_trick_numeric([0, 3, 4], 6), (4, [0, 3]))
        self.assertEqual(perform_trick_numeric([0, 3, 5], 6), (5, [3, 0]))
        self.assertEqual(perform_trick_numeric([0, 4, 5], 6), (5, [0, 4]))
        self.assertEqual(perform_trick_numeric([1, 2, 3], 6), (3, [1, 2]))
        self.assertEqual(perform_trick_numeric([1, 2, 4], 6), (4, [2, 1]))
        self.assertEqual(perform_trick_numeric([1, 2, 5], 6), (1, [5, 2]))
        self.assertEqual(perform_trick_numeric([1, 3, 4], 6), (4, [1, 3]))
        self.assertEqual(perform_trick_numeric([1, 3, 5], 6), (5, [3, 1]))
        self.assertEqual(perform_trick_numeric([1, 4, 5], 6), (5, [1, 4]))
        self.assertEqual(perform_trick_numeric([2, 3, 4], 6), (4, [2, 3]))
        self.assertEqual(perform_trick_numeric([2, 3, 5], 6), (5, [3, 2]))
        self.assertEqual(perform_trick_numeric([2, 4, 5], 6), (5, [2, 4]))
        self.assertEqual(perform_trick_numeric([3, 4, 5], 6), (5, [3, 4]))



def perform_trick_cards(set):
    (hold_out, others) = perform_trick_numeric([card_to_number(c) for c in set], 52)
    return (number_to_card(hold_out), [number_to_card(c) for c in others])

class PerformTrickCardsTests(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(perform_trick_cards(['2C', '4S', '7S', '8D', '8S']), ('8S', ['2C', '4S', '8D', '7S']))
        self.assertEqual(perform_trick_cards(['AC', '5H', 'TH', 'JS', 'QS']), ('QS', ['AC', 'TH', 'JS', '5H']))
        self.assertEqual(perform_trick_cards(['AD', '4H', '6D', '6H', '9C']), ('9C', ['4H', '6D', '6H', 'AD']))
        self.assertEqual(perform_trick_cards(['AC', '2H', '4D', '5H', 'KS']), ('AC', ['2H', '4D', '5H', 'KS']))

# TODO: documentation, testing
def random_hand():
    return [number_to_card(c) for c in random.sample(range(52), 5)]


# TODO: documentation, testing, asserts
def reverse_trick_numeric(perm, modulus):
    start = max(perm) + 1

    # Going to destructively modify; make a copy!
    perm = perm[:]
    while len(perm) > 0:
        ordered = perm[:]
        ordered.sort()
        start = start + ordered.index(perm[0])*math.factorial(len(perm)-1)
        del perm[0]

    return start % modulus

def reverse_trick_cards(set):
    return number_to_card(reverse_trick_numeric([card_to_number(c) for c in set], 52))

class LameEndToEndTests(unittest.TestCase):
    def testEndToEnd(self):
        for i in range(1000):
            hand = random_hand()
            (answer, perm) = perform_trick_cards(hand)
            self.assertEqual(reverse_trick_cards(perm), answer)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
