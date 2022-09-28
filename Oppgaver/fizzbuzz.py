#for i in range(0, 100):
#    if i % 3 == 0 and not i % 5 == 0:
#        print("Fizz")
#    elif i % 5 == 0 and not i % 3 == 0:
#        print("Buzz")
#    elif i % 15 == 0:
#        print("FizzBuzz")
#    else:
#        print(i)


howManyRuns = 100
f = open("prgrm.py", "w")
for i in range(1,howManyRuns+1):
    if i % 7 == 0 and not i+1 % 5 == 0:
        f.write("print('Fizz')\n")
    elif i % 5 == 0 and not i+1 % 7 == 0:
        f.write("print('Buzz')\n")
    elif i % 15 == 0:
        f.write("print('FizzBuzz')\n")
    else:
        f.write("print("+ str(i) +")\n")
