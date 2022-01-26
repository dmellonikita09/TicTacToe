"""
Given array of integers [ 1  2 5 11 22 27]  
 and target sum = 24  return true/false if there exists 
 two numbers that sums to the target


"""

def target_sum(arr, target):
    hash_mp={}
    for i, n in enumerate(arr):
        diff = target - n
        if diff not in hash_mp:
            hash_mp[n]= i
        else:
            return[hash_mp[diff], i]
arr = [1, 2, 5, 11, 22, 27]
target = 24
print(target_sum(arr, target))
# if it's aleady sorted there is no need for hash map.

