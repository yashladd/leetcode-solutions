class OrderedStream:

    def __init__(self, n: int):
        # We need a pointer to track the next expected ID (starts at 1)
        self.ptr = 1
        # Create a list to store values. (n + 1) size to make 1-based indexing easier
        self.stream = [None] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        # 1. Store the incoming value
        self.stream[idKey] = value
        
        result = []
        
        # 2. If the inserted ID matches our pointer (or we have data waiting at the pointer),
        #    we collect all consecutive values available.
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
            
        return result