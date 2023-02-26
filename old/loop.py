loops = 0

"""
while loops < 3:
    print(loops)
    loops += 1 # += means increment, could be done with loops = loops + 1.
"""

# _  is just an unnamed variable that is only used for the "for loop", and not anything else

for i in range(3): # range returns all the values from 0 to 1 number less than the number in the argument
    print(i)

# for i in [0, 1, 2] just sets i to the values from left to right by 1 in each iteration. If the list was [2, 7, 5] i would've had the value of 2 on the first iteration, then 7 and then 5. 

# print("woof\n" * 3, end="") if you use print you can multiply the string by the number of times to print, and set the argument end to empty if you don't want the extra blank line when printing