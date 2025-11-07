class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    lst.append("FizzBuzz")
                    continue
                lst.append("Fizz")
                continue
            if i % 5 == 0:
                lst.append("Buzz")
                continue
            lst.append(str(i))
        return lst
