class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, s in sorted(zip(position,speed), key=lambda x: x[0], reverse=True):
            time = (target-pos)/s
            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack:
                stack.append(time)
        return len(stack)
        