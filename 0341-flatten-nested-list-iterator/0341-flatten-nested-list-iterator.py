class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        Does this reduce space complexity?
Yes and No.

Heap Space: It drastically reduces heap space. In your previous approach, if the nested list had 1 million integers, you would create a new list of 1 million integers. With a generator, you only store one integer at a time.

Stack Space: The recursion still uses space on the call stack. If the list is nested 1,000 layers deep, you will have 1,000 function calls sitting in memory.

Overall: It is generally considered "better" because you are only processing what you need when you need it (Lazy Evaluation).
        """
        # We create the generator but don't "run" it yet
        self.generator = self._generator(nestedList)
        # We need to pre-fetch the first value to support hasNext()
        self.peek = next(self.generator, None)

    def _generator(self, nl):
        for element in nl:
            if element.isInteger():
                yield element.getInteger()
            else:
                # Recursively yield from the inner list
                """
                2. What is yield from?
This is a shortcut for nested structures.

Instead of writing: for item in sub_list: yield item

You write: yield from sub_list
                """
                yield from self._generator(element.getList())

    def next(self) -> int:
        result = self.peek
        self.peek = next(self.generator, None)
        return result

    def hasNext(self) -> bool:
        return self.peek is not None