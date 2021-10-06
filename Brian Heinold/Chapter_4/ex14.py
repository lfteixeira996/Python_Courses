"""
Write a program that prints out on separate lines the following 200 items: file0.jpg, file1.jpg, . . . ,
file199.jpg, except that it should not print anything when the number ends in 8, like file8.jpg
,file18.jpg, etc. [Hint: if i % 10 is not 8, then i doesn’t end in 8.]
"""

for i in range(200):
    if i % 10 != 8:
        print(f"file{i}.jpg")