class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        string_pref = []

        """
        "pbbcggttciiippooaais"
k = 2
        """
        for ch in s:
            if string_pref:
                if string_pref[-1][0] == ch:
                    if len(string_pref[-1]) + 1 >= k:
                        string_pref.pop()
                    else:
                        string_pref[-1] += ch
                else:
                    string_pref.append(ch)
            else:
                string_pref.append(ch)

        return "".join(string_pref)


            