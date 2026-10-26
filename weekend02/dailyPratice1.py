"""
🧠 Problem: Exact-Distance Segments

Your rover’s encoder logs how far it moved each tick, in metres. A negative value means the rover reversed during that tick.
moves = [2, -1, 1, 2]

A segment is a run of consecutive ticks. Write count_segments(moves, k), which returns how many segments have a net displacement of exactly k.

🟡 Test cases (all must pass)
print(count_segments([1, 2, 3], 3))        # 2
print(count_segments([1, 1, 1], 2))        # 2
print(count_segments([2, -1, 1, 2], 2))    # 4
print(count_segments([0, 0, 0], 0))        # 6
print(count_segments([3, -3, 3, -3], 0))   # 4
print(count_segments([], 0))               # 0

🔴 Part A: make it correct
Any approach is fine as long as all six tests pass.
Before you code it, write one line explaining why [0, 0, 0] gives 6 and not 3. If you can’t explain that, your loop bounds will come out wrong.

🔥 Part B: make it fast
The real log has 100,000 ticks.
[Certain] An approach that checks every segment does about 5 billion operations, which takes minutes in Python. Your target is one pass through the list.
[Likely] The first fast idea most people try is a sliding window (grow the right edge, shrink the left edge). Before you commit to it, run it on test case 5 by hand and see what happens.
⚪ Rules
No googling the problem.
I won’t give you hints unless you ask. When you ask, you’ll get a question back, not the answer.
"""

    