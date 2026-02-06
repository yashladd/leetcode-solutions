from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)                  # char -> count
        countOfFreq = Counter(freq.values())  # count -> how many chars have that count

        if len(countOfFreq) == 1:
            (f, how_many) = next(iter(countOfFreq.items()))
            # either all are 1 (remove any char, remaining still equal)
            # or only one unique letter (e.g. "aaaa" -> remove one -> "aaa")
            return f == 1 or how_many == 1

        if len(countOfFreq) == 2:
            (f1, c1), (f2, c2) = sorted(countOfFreq.items())  # f1 < f2

            # remove the only char with freq 1
            if f1 == 1 and c1 == 1:
                return True

            # reduce the only high-frequency char by 1 to match f1
            if f2 == f1 + 1 and c2 == 1:
                return True

        return False
