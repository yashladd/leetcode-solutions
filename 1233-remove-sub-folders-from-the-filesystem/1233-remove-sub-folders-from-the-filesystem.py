class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        a bc bca cdf aaa aca azb zzo z




        """

        # folder = [x.split("/").lstrip().rstrip() for x in folder]

        folder.sort()
        res = [folder[0]]

        print(folder)

        index = 0

        while index < len(folder):
            nextIndex = index + 1
            while nextIndex < len(folder) and folder[nextIndex].startswith(folder[index] + "/"):
                nextIndex += 1

            if nextIndex < len(folder):
                res.append(folder[nextIndex])

            index = nextIndex
        return res
        