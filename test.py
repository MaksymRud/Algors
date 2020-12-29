from collections import Counter

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    d1 = Counter(nums1)
    d2 = Counter(nums2)
    l = []
    for i in d1.keys():
        if i in d2.keys():
            if d1[i] >= d2[i]:
                for k in range(d1[i]):
                    l.append(i)
            else:
                for k in range(d2[i]):
                    l.append(i)
    return l
