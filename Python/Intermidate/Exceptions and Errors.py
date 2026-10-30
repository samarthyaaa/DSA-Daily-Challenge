#Exceptions - occurs when different errors occurs due to some syntax , indentation , key-value , file, index, KeyboardInterrupt error
#raising an exception - to raise an exceptions intenionally
try:
    result=2/0
    #some line of codes # where the actual code runs
except ZeroDivisionError:
    print("You can't divide by zero")# where all the exception which can be met are written
    #handler <ERROR1>
#except<ERROR2>:
    #handler <ERROR2>
#else:
    #no exception are raised , the code ran successfully
finally: # will excute anyway
    result = 1
    #do something in any case
print(result)
