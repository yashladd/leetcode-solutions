class Solution:
    def compress(self, chars: List[str]) -> int:
        char_idx = 0
        N = len(chars)
        ptr = 0
        while char_idx < N:
            curr_char = chars[char_idx]
            curr_len = 1
            while char_idx + 1 < N and chars[char_idx + 1] == curr_char:
                char_idx += 1
                curr_len += 1

            chars[ptr] = curr_char
            ptr += 1
            if curr_len > 1:
                for ch in str(curr_len):
                    chars[ptr] = ch
                    ptr += 1
            char_idx += 1

        return ptr
