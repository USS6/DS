# Given an list of elements in sorted order find the two numbers which add up to target number
# [1,2,3,4,5] -> target : 6

# CONCEPT: TWO-POINTER
# PRE: Pointers - left=0,right=len(elements)-1
# ITERATE: while(left<right)
# INSIDE-ITER: left+right<Target==Target->return | left+right<Target->left++ | left+right>target->right--
# TC - O(n) | SC - O(1)

class toSum:
    def TwoSum(self,elements,target):
        left=0
        right=len(elements)-1
        while(elements[left] < elements[right]):
            sum = elements[left]+elements[right]
            if(sum==target):
                return True
            elif(sum<target):
                left+=1
            elif(sum>target):
                right-=1
        return False

ts = toSum()
print(ts.TwoSum([5],5)) 