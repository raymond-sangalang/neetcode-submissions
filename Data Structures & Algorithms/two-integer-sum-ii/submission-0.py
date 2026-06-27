class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front_ptr = 0
        back_ptr = len(numbers)-1
        
        while front_ptr < back_ptr:
            outcome = numbers[front_ptr] + numbers[back_ptr]
            
            if outcome < target:                  # update pointer accordingly to their sum
                front_ptr += 1
            elif outcome > target:
                back_ptr -= 1
            else:                                 # desired outcome, return indices
                return [front_ptr+1, back_ptr+1]