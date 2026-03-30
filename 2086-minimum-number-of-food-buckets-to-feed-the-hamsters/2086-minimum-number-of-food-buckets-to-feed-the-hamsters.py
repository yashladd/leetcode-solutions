class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        positions = list(hamsters)
        # print(positions)

        num_buckets = 0

        for i, pos in enumerate(positions):
            if pos == "H":
                if i > 0 and positions[i-1] == "B":
                    continue

                if i + 1 < len(hamsters) and positions[i+1] == ".":
                    positions[i+1] = "B"
                    num_buckets += 1
                elif i - 1 >= 0 and positions[i-1] == ".":
                    positions[i-1] = "B"
                    num_buckets += 1
                else:
                    return -1

        return num_buckets