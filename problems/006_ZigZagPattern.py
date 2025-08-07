def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= 2 or len(s) <= numRows:
             return s
        a = [""] * numRows
        row=0
        directionDown = False
        for i in s:
            a[row] += i
            if row == 0 or row == numRows - 1:
                directionDown = not(directionDown)
            row += 1 if directionDown else -1
        return ''.join(a)


print(convert("PAYPALISHIRING" ,3))