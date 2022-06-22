""" In this project i want to solve 50 well-known binary search problem listed in the website
https://igotanoffer.com/blogs/tech/binary-search-interview-questions"""


# this notebbok is for easy level binary search problem

# Problem number 01
# The easiest binary search problem is the Seach insert  position
# Leetcode problem number 35
def searchinsertposition(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        mid = (l + r) // 2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return l


#problem number 02
# compute the square root of x sqrt(x)
# Leetcode problem number 69
def mysqrt(x):
    l,r=0,x  # x is a non negatice integer
    while l<=r:
        mid=(l+r)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            l=mid+1
        else:
            r=mid-1
    return r  # when mid*mid greater than x then right pointer become the truncated dicimal digit

#  problem number 03
#  first bad version
#  Leetcode problem number number 278

def firstbadversion(n):
    """ Here isBadVersion is an application programming interface(API)
    which i can use. I have to minimize the API calls.
    This can be done by binary search"""
    l,r=1,n
    while l<=r:
        mid=(l+r)//2

        if  isBadVersion(mid):  # The API is available in the Leetcode interface. the function has already submitted and it works
            r=mid-1
        else:
            l=mid+1
    return l

# Problem 04
# Intersection of two arrays(not based on binary search)
# Leetcode problem number 349

def intersectionoftwoarrays(nums1,nums2):
    """ There may be other technique to solve this problem.
    But here we want to see the binary search technique. But first see the other technique"""
    res=[]
    import  collections
    counts=collections.Counter(nums1)
    for num in nums2:
        if counts[num]>0:
            counts[num]-=1
            if num not in res: # Each item in the intersection is unique
              res+=num,
    return res

#  Porblem 05
#  Intersection of two arrays based on binary search
# Leetcode problem number 349

def intersectionoftwoarrays1(nums1,nums2):
    """ Lets's see the binary search solution.
    For binary search the arrays must be sorted"""
    nums1.sort()
    nums2.sort()
    res=[]
    for target in nums1:
        l,r=0,len(nums2)-1
        while l<=r:  # Binary search in the second array for each target
            mid=(l+r)//2
            if nums2[mid]==target:
                if target not in res: # each item of the intersection is unique
                    res+=target,
                break
            elif nums2[mid]>target:
                r=mid-1
            else:
                l=mid+1
    return res

#  Problem 06
# Intersection of two arrays based on bianry search (Each element in the result must appear as many times as it shows in both arrays)
#  Leetcode problem number 350

def intersectionoftwoarrays2(nums1,nums2):
    import collections
    nums1.sort()
    nums2.sort()
    res=[]

    for target in nums1:
        l,r=0,len(nums2)-1

        while l<=r:
            mid=(l+r)//2
            if nums2[mid]==target and res.count(target)<nums2.count(target):


                res+=target, # Each element in the result must appear as many times as it shows in both arrays
                break
            elif nums2[mid]>target:
                r=mid-1
            else:
                l=mid+1
    return res



#  problem 07
#  valid perfect square
# Leetcode problem number 367

def ValidpecfectSquare(num):
    """ There are many ways to solve the problem.
    But here we want to see the binary search approach"""
    l,r=0,num
    while l<=r:
        mid=(l+r)//2
        if mid*mid==num:
            return True
        elif mid*mid<num:
            l=mid+1
        else:
            r=mid-1
    return False

#  Problem 08
#  Guess Number higher or lower
#  Leetcode problem number 374

def Guesshigherlower(n):
    """ There is a pre-defined Application user interfacec
    called int guess"""
    l,r=0,n
    while l<=r:
        mid=(l+r)//2
        if guess(mid)==0: # Call the API named guess
            return mid
        elif guess(mid)==-1:
            r=mid-1
        else:
            l=mid+1

# Problem 09
# Arranging coins
# Leetcode problem number 441

def arrangingcoins(n):
    """There are many ways to solve the problem.
    But we want to see the binary search solution"""
    l,r=0,n
    while l<=r:
        mid=(l+r)//2
        if (mid*(mid+1))/2==n:
            return mid
        elif (mid*(mid+1))/2>n:
            r=mid-1
        else:
            l=mid+1
    return r



# Problem 10
# Binary search (the well-known example of binary search)
# Leetcode problem number 704

def binarySearch(nums,target):
    l,r=0,len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return  mid
        elif nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return -1

#  Problem 11
#  Smalllest letter greater than target
#  Leetcode problem number 744

def Smallestgreaterletter(letters,tagret):
    """The problem is initially a binary search problem.
    So binary search for the character which comes immediately after character target.
    But as because  the letters wrap around if the target is greater than or equal to
    last character the search for the first character in the list"""
    if tagret>=letters[-1]:
        return letters[0]
    l,r=0,len(letters)-1
    while l<r:
        mid=(l+r)//2
        if letters[mid]<=tagret:
            l=mid+1 #don't return consider this testcase ["e","e","e","e","e","e","n","n","n","n"],'e'
        else:
            r=mid
    return  letters[l]


# problem 12
# Peak index in a mountain array
# Leetcode problem number 852


def peakindexmountainarry(arr):
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if arr[mid]<arr[mid+1]:
            l=mid+1
        else:
            r=mid
    return l


# problem number 13
# Count negative number in a sorted matrix
# Leetcode problem number 1351

def countnegativenum(grid):
    count=0
    for arr in grid:
        l,r=0,len(grid[0])-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]>=0:
                l=mid+1
            else:
                r=mid
        if arr[l]<0:
          count+=len(arr[l:])
    return count




#  Problem number 13
#  find the distance values between two arrays
#  Leetcode problem number 1385

def distancebetweenarray(arr1,arr2,d):
    """Find the insert position for each num in arr1 in arr2.
    then take the min distance of the neighbouring"""
    count=0
    arr2.sort()
    for num in arr1:
        l,r=0,len(arr2)-1
        while l<=r:
            mid=(l+r)//2
            if arr2[mid]>num:
                r=mid-1
            else:
                l=mid+1

        if l==0 and abs(num-arr2[0])>d:
            count+=1
        if l==len(arr2) and abs(num-arr2[-1])>d:
            count+=1
        if 0<l<len(arr2) and min(abs(num-arr2[l-1]),abs(num-arr2[l]))>d:
            count+=1
    return count





#  problem 14
#  kth missing positive
#  Leetcode problem number 1539

def MissingPositive(arr,k):
    """Find the missing at  each index.
    Then compute where it greater than k"""
    l,r=0,len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]-mid-1<k: # Missing a index k
            l=mid+1
        else:
            r=mid
    return r+k










