from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        hand.sort()

        for elem in hand:
            if counts[elem] == 0:
                continue # used if prev group
            # elem is the smallest remaining card, so start a group here.
            for card in range(elem, elem+groupSize):
                if counts[card] == 0:
                    return False
                counts[card] -= 1
        return True
