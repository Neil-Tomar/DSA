def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if not(-2147483648 <= x <= 2147483647):
            return 0
        k=1
        if x<0:
            x=-x
            k = -1
        rev= int(str(x)[::-1])
        if not(rev <= 2147483647):
            return 0
        return rev*k

print(reverse(-123))