class Solution:
    def perfect_number(self, num: int) -> bool:
        n = num // 2
        result = 0
        for i in range(1, n +1):
            if num % i == 0:
                result += i

        return result == num

    def perfect_number2(self, num: int) -> bool:
        n = num // 2
        result = 0
        i = 0
        while i < n:
            if num % i == 0:
                result += i
            if result > num:
                return False
            i += 1

        return result == num

    def perfect_number3(self, num: int) -> bool:
        if num <= 1:
            return False
        result = 1
        n = (num // 2) + 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                result += i + num // i
        return result == num

    def perfect_number4(self, num: int) -> int:
        '''
        Euclid–Euler theorem
        2^(p-1)((2^p)-1)
        where p is a prime number
        '''
        primes = {2, 3, 5, 7, 13, 17, 19, 31}

        for item in primes:
            if (2 ** (item - 1)) * ((2 ** item) - 1) == num:
                return True

        return False


s = Solution()
print((s.perfect_number4(28)))
