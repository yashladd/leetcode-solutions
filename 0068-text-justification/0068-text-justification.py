class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        1, 1, 1     14
        spaces = 11 
        slots = 2
        3 3 
        4 3
        2, 2 
        extra = 1

        """ 


        line = []
        line_chars = 0
        res = []

        def make_line(line, line_chars):
            spaces = maxWidth - line_chars
            if len(line) == 1:
                return line[0] + " " * spaces
            space_insertions = len(line) - 1
            even_spaces = spaces // space_insertions
            extra_spaces = spaces % space_insertions
            res = ""

            for i, w in enumerate(line):
                res += w
                if i != len(line)-1:
                    req_spaces = even_spaces + (1 if extra_spaces > 0 else 0)
                    res += " " * (req_spaces)
                    extra_spaces -= 1

            return res

        for word in words:
            if line_chars + len(word) + len(line) > maxWidth:
                res.append(make_line(line, line_chars))
                line = [word]
                line_chars = len(word)
            else:
                line_chars += len(word)
                line.append(word)

        if len(line):
            last_line = " ".join(line)
            padding = maxWidth - len(last_line)
            last_line += " " * padding

            res.append(last_line)

        return res

