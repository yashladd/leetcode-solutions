class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0 

        rs, cs, ld, rd = set(), set(), set(), set()

        def f(i):
            nonlocal cnt
            if i == n:
                cnt += 1

            for j in range(n):
                if i not in rs and j not in cs \
                    and (i + j) not in rd and (i-j) not in ld:
                    rs.add(i)
                    cs.add(j)
                    ld.add(i-j)
                    rd.add(i+j)
                    f(i+1)
                    rs.remove(i)
                    cs.remove(j)
                    ld.remove(i-j)
                    rd.remove(i+j)

        f(0)

        return cnt


        