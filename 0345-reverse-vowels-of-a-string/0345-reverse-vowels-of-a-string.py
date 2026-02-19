class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)

        res = ""

        st = [ ]
        for i, ch in enumerate(s):
            if ch in "aeiouAEIOU":
                st.append(ch)


        for ch in s:
            if ch in "aeiouAEIOU":
                res += st.pop()
            else:
                res += ch

        return res

        