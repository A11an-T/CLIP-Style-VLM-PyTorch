# Weekend 1, task 1
# Your robot logged these wheel-speed readings during a match.
# Write summarize(speeds) so it returns (average, top_speed).
# Rule: you may NOT use the built-in max().

speeds = [3.2, 4.8, 4.1, 5.6, 2.9, 5.1]


def summarize(speeds):
    numInputs = len(speeds)

    #cases of 0s
    if numInputs == 0:
        return 0,0
    #Caculating Average Speed without using methods
    avgSpeed = 0.0
    maxSpeed = speeds[0]

    for i in speeds:
        avgSpeed += i 
        #can be optimized by setting speeds[i] into another variable
        if i>maxSpeed:
            maxSpeed = i
            
    avgSpeed = avgSpeed/numInputs
    
    #Calculating Maximums without using the max() function 


    #This returns a tuple - are unmodifiable list of data : toys = ("hippo", 2, {"Car": "balblaba", "sdfsdf": 2033})
    return avgSpeed, maxSpeed 

print(summarize(speeds))   # should print roughly (4.283, 5.6)
print(summarize([7.0]))    # should print (7.0, 7.0)
print(summarize([]))       # what SHOULD happen here? Decide, then make it happen.



#pass - placeholders for returns
#tuple - are unmodifiable list of data : toys = ("hippo", 2, {"Car": "balblaba", "sdfsdf": 2033})
"""
nums = [10, 20, 30]
for s in nums:  # s is 10, then 20, then 30
    print(s)
    
basically setting i to be the exact value, instead of letting it be i = 0 or 1, 2, 3 iterations 
"""