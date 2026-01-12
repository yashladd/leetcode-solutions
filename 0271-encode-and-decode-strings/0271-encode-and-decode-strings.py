class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for s in strs:
            ans += str(len(s))
            ans += "!"
            ans += s
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        n = len(s)
        ans = []
        while i < n:
            # j = i
            j = s.index("!", i)
            # print("HashIdxex", x, s, i)
            while s[j] != "!":
                j += 1
            l = int(s[i:j])
            ans.append(s[j+1:j+l+1])

            i = j + l + 1

        return ans 


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))