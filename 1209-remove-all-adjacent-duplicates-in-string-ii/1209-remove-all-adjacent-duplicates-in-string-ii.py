class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        string_pref = []

        """
        "pbbcggttciiippooaais"
k = 2
        """
        for ch in s:
            if string_pref and string_pref[-1][-1] == ch:
                string_pref[-1] += ch
            else:
                string_pref.append(ch)

            if string_pref and len(string_pref[-1]) == k:
                string_pref.pop()

        return "".join(string_pref)


            