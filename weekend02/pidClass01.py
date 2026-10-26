"""  
Writing code down on paper (copied on here)
1. Create the class strucutre 
2. Write the initialization with parameters of (self, kP, kI, KD)
3. Declaring and initilazing the variables self.kP, self.KI, self.kD, self.oldError, self.oldTime 
4. Create a method a updater method that provide new P, I, D ouputs 
5. Given the equation as P = kp(Error) I = kI(Error)(newTime - oldTime) D = kD(newError - oldError)/(newTime - oldTime)
6. Returns P + I + D
"""

class PIDController:
    
    def __init__ (self, P, I, D):
        #Initialziating the variables
        self.kP = P 
        self.kI = I 
        self.kD = D 
        self.I = 0; 
        
        #Initalliation of the oldErrors and OldTimes must be 0, given there are no other datas before it.
        self.oldError = 0; 
        self.oldTime = 0;
        self.numEntries = 0;

    #Updating the PID everytime there are new errors at new times 
    def updatePID (self, newError, newTime):
        #Solving for P, I, D based on the Error and Time
        
        P = self.kP*newError

        if self.numEntries == 0:
            D = 0
            self.numEntries+=1
        else:
            self.I += self.kI*(newTime-self.oldTime)*newError
            if newTime - self.oldTime == 0:
                D = 0
            else:
                D = self.kD*(newError-self.oldError)/(newTime-self.oldTime)


        
        self.oldTime = newTime
        self.oldError = newError
        return P, self.I, D, P+self.I+D
        
        
a = PIDController(2, 0.5, 1)
print(a.updatePID(5,0.1))
#(10, 0, 0, 10.25) In a real PID the output should only be P+I+D, by seperating them into tuples helps me debug issues. 

print(a.updatePID(3,0.2))
#(6, 0.4, -20.0, -13.6)

print(a.updatePID(1,0.3))

b = PIDController(2, 0.5, 1)
b.updatePID(5, 0.1)
b.updatePID(0, 0.2)
print(b.updatePID(2, 0.3))

c = PIDController(2, 0.5, 1)
print(c.updatePID(5, 5.0)) 


e = PIDController(2, 0.5, 1)
e.updatePID(0, 0.0)          
print(e.updatePID(2, 0.1))   


f = PIDController(2, 0.5, 1)
f.updatePID(5, 0.1)
print(f.updatePID(3, 0.1))

### Error Log - My thought proccess
# Issue 1: gave me the value 60.25 why, p is 10, i is 0.25 and d is 50  but D should be 50 on the first call (also called the Derivative Kick)
# Solved: since we know that D needs two real reading, and our 0 was just a place holder, therefore D must output 0, so what I did was 
# use an if statement to detech that if self.oldError == 0 then set D =0, which temperoay fixed the issue. 

# Issue 1a:After running some test cases I found that (look at b=PIDController) it creates an issue if, the new D is 0, then error occurs, so if statments
# doesn't work 
# Sovled: Therefore one thing I know is that the only thing that is different from the first call of the method to the rest is that
# time starts at 0, always, can't have negative time. 

# Issue 1b: After running some more test cases I figure that there is no difference between the two methods of solving they can have the same bug.
# Going back to think again, I thought of using counters, which makes it so that it would run once and be false for the rest. 

# Issue 2: Since I, is an integral it adds up over time, so I need to delcare a variable that is still in scope and at the same time everytime
# the method is called there should be memory of the previous called I value. 
# Solved: Took me 1 hour (need improvnement), the method was to initilaze the varible in the "__init__", and set it to 0, then using the self.I
# I can continously add the value without reseting after every loop add up all the values. 

# Issue 3: The same problem occured at issue 1, because the initilaization is just a place holder therefore caused we can't find the Integral, with only
# one reading.
# Solved: therefore using the same method in 1b adding a counter will solve the problem. 

# Issue 4: ZeroDivisionError appeared for D 
# Sovled: By using an if statment we can easily isloated the problem, and set the value to 0, because it is the saftiest
# because we can't caculate the value so we don't add anything to the change of error per second, which could lead to tempoary overshoot. 
# How to tackle this problem to be more accurate, "using previous calculations, finding a limit at that tangent, or using another model to tempory replace it" 

# Total time Took : 4 hours, I didn't ask AI to write the code or help me problem solve, rather I used it to confirm my understanding 
# Such as derivative kick, and other syntaxes in python I forgot. 
