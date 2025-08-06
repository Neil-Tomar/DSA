def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        s="0"+s
        pal=""
        length = len(s)
        for start in range(1,length):
            for end in range(length,start-1,-1):
                    sse =s[start:end]
                    if ((len(sse) > len(pal)) and (sse==s[end-1:start-1:-1])):
                        pal = sse
        
        return pal


print(longestPalindrome("babad"))