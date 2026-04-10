class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #stores the number of times a number appears
        count = {}
        #is a list of lists where the index represents
        #the frequency and the values at that index is the
        #number that appears that many times 
        freq = [[] for i in range(len(nums) + 1)]

        #this loop populates the count dictionary
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #populates the frequency array
        for n, c in count.items():
            freq[c].append(n)
        
        #the answer array
        res = []

        #outer loop starts from the last element in freq 
        #until the first element 
        for i in range(len(freq) - 1, 0, -1):
            #inner loop goes through each inner lists and
            #and appends them to the result until the array is
            #of size k in that case we return
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res