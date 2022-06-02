"""
approach:
    brute force: (violates problem request of O(n))
        init answer array to array of 1's with same length as nums
        loop over the answer array
            loop over the nums array
                if the indices are not equal, *= answer[i] with nums[j]
    
    recursive DP:
        it's sort of DP in the sense that we don't have to recalculate some products
        consider a list
        subdivide the list
        compute, individually, the products of the elements in each of the two halves
        recurse on the two halves
            within the recursion, consider that:
                - we have a sublist
                - we have the product of all elements not in the sublist
                -> we don't have to compute the product of anything outside of the sublist
            base case:
                our array length == 1 -> the product that was passed to this function call is the product of all elements except the one being considered, which is what we wanted to compute

    iterative DP:
        sort of DP
        populate an array (forwards) with the cumulative products starting from index 0 to end
        populate another array (backwards) with the cumulative products starting from end to index 0
        now, answer[i] = forwards[i-1] * backwards[i+1]
        to reduce space complexity further, we could use the answer list to store the forwards values
            as long as we populate forwards in reverse order
        or, we could use answer list to store backwards values and populate in natural order
    
    iterative with temp var: T O(n) S O(1)
        make two passes of the answer array
        on the first pass, compute the cumulative product for each element
        on the second pass, go in reverse, and multiply ans[i+1] by cumulative prod, store in answer[i]
    
    iterative with two pointers: T O(n) S O(1)
        same idea as iterative with temp var, except that since the two passes don't interfere with each other directly as long as they move at the same pace, we can move things into a single loop and increment/decrement left and right pointers to produce the cumulative sums
        probably the exact same time complexity, but less readable
    
"""

# iterative with two pointers - from the discussion forum
# T: O(n)
# S: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pi = pj = 1
        
        for i in range(len(nums)):
            # start i and j at opposite ends, populate leading indices with cumulative products
            # eventually they will cross and fill in the other portion of the product
            j = -1 -i # right pointer
            ans[i] *= pi
            ans[j] *= pj
            pi *= nums[i]
            pj *= nums[j]
        return ans
        
        
# iterative with temp var
# T: O(n)
# S: O(1)
class __Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 1
        p = 1
        answer = []
        for i in range(len(nums)):
            answer.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1): # from nums[-1] to nums[0]
            answer[i] *= p
            p *= nums[i] # cumulative product from end to i
        return answer

# iterative "DP"
# T: O(3n) (forwards calc, backwards calc, answer calc)
# S: O(2n) for the reverse product array and the answer array
class __Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = 1
        answer = backwards = [c:=c*v for v in reversed(nums)][::-1]
        c = 1
        forwards = [c:=c*v for v in nums]
        for i in range(len(answer)):
            before = forwards[i-1] if i > 0 else 1
            after = backwards[i+1] if i < len(answer)-1 else 1
            answer[i] = before*after
        return answer

    # same as above, but annotated
    def __productExceptSelf(self, nums: List[int]) -> List[int]:
        # store cumulative products (in reverse order) in answer
        c = 1
        answer = backwards = [c:=c*v for v in reversed(nums)][::-1] # backwards is just an alias
        # to clarify above: make an array with cumulative product, with cumulative understood as starting from the end and moving towards the start of nums, then reverse the array (that's [::-1]) so that we can overwrite answer[i] later, relying only on answer[i+1]
        # store cumulative products (in forward order) in forwards
        c = 1
        forwards = [c:=c*v for v in nums]
        # we know that answer[i] = forwards[i-1] * backwards[i+1]
        # because forwards[i-1] is the product of all elements before i
        # and backwards[i+1] is the product of all elements after i
        # since we put backwards in answer, we can populate answer with answers in the forward direction
        # because we only ever need backwards[i+1], never [i-anything]
        for i in range(len(answer)):
            # stay in bounds, answer[1] = 1*after and answer[-1] = before*1
            before = forwards[i-1] if i > 0 else 1
            after = backwards[i+1] if i < len(answer)-1 else 1
            answer[i] = before*after
        return answer
        



# recursive "DP"
# T: O(n*logn)?
# S: O(n) recursive space
class __Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        self.helper(nums, answer, 0, len(nums), 1)
        return answer
    
    # recursive helper
    def helper(self, nums: List[int], answer: List[int], start: int, end: int, product: int) -> None:
        # base cases
        if start == end:
            return None
        if end-start == 1: # then the product passed in is our answer for this cell
            answer[start] = product
            return
        # recursive work
        import numpy
        mid = (start + end) // 2
        leftHalfProduct = product * numpy.prod(nums[start:mid])
        rightHalfProduct = product * numpy.prod(nums[mid:end])
        self.helper(nums, answer, start, mid, rightHalfProduct) # recurse on left half with rhp
        self.helper(nums, answer, mid, end, leftHalfProduct) # recurse on right half with lhp
        
            


# brute force - TLE, violates problem request (to write in O(n) time)
# T: O(n^2)
# S: O(n) for the answer array
class __Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    answer[i] *= nums[j]
        return answer




# solution I wrote before starting grind75
class __Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        productWithoutZeroes = 1
        zeroCount = 0
        for element in nums:
            product *= element  # always calculate the full product
            if element == 0:  
                zeroCount += 1
            else:  # only calculate the zero-omitted product if the current element is *not* zero
                productWithoutZeroes *= element
                
        answer = []
        for i in range(0, len(nums)):
            if nums[i] != 0:  # if current is not 0, calculated as intuitive
                res = product / nums[i]
            if nums[i] == 0:  # if the current is zero, we need to investigate
                if zeroCount < 2: # if greater than 1, omitting current will still give a 0 product
                    res = productWithoutZeroes
                else:
                    res = 0
            answer.append(int(res))
        return answer
