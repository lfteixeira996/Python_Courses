"""
In 24-hour time, hours run from 0 o’clock (midnight) to 23 o’clock (aka 11 pm). Write a program that
asks the user for the current hour and for how many hours in the future they want to go. Have the
program print out what the hour will be that many hours in the future. For instance, if it’s 13 o’clock
now, 27 hours from now it will be 16 o’clock. [Hint: Use the mod operator.]
"""

now = eval(input("Now: "))
future = eval(input("Future: "))
time = now

for i in range(now, future+1):
    if time == 24:
        time = 0
    time = time + 1

print(time)
