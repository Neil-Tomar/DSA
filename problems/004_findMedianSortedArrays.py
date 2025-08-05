def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=0
        l = nums1+nums2
        l.sort()
        length=len(l)
        if(length%2==0):
            a=l[int(length/2)]
            b=l[int(length/2)-1]
            m=(a+b)/2
        else:
            m=l[int(length/2)]
        return m
        

print(findMedianSortedArrays([1,2],[3,4]))