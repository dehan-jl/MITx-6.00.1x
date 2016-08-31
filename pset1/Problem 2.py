# Problem Set 1 / Problem 2
# 31 August 2016
# @Dehan Lamprecht
# for MITx 6.00.1x

#s = "rohadsohboblkhasde"
bob = "bob"
count = 0
for i in range(len(s) - 2):
    if s[i:i + 3] == bob:
        count += 1

print("Number of times bob occurs is:", count)
