#User function Template for python3
class Solution:
    def search(self, n, arr):
        # your code here
        
        size = len(arr)
        if size == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[size-1] != arr[size-2]:
            return arr[size-1]
        
        i = 2
        j = size -3
        while j>=i:
            
            mid = (i+j) //2

            if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
                return arr[mid]
            
            if arr[mid] == arr[mid+1]:
                if (mid-i)%2 == 1:
                    j = mid - 1
                else:
                    i = mid + 2
            else:
                if (mid-i+1)%2 == 1:
                    j = mid
                else:
                    i  = mid+1
        return -1
                