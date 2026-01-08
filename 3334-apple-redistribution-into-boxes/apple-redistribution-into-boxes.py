class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        used_boxes:int = 0
        capacity = sorted(capacity, reverse=True)
        while apple:
            current_apple = apple[0]
            current_capacity = capacity[0]
            if current_apple > current_capacity:
                used_boxes += 1
                apple[0] -= current_capacity
                capacity.pop(0)
            elif current_apple < current_capacity:
                capacity[0] -= current_apple
                apple.pop(0)
                if not apple:
                    used_boxes += 1
            else:
                used_boxes += 1
                apple.pop(0)
                capacity.pop(0)
        return used_boxes