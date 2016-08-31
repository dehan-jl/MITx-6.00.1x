# Problem Set 1 / Problem 1
# 31 August 2016
# Dehan Lamprecht
# for MITx 6.00.1x

#s = "blebleblea"
vowels = ["a","e","i","o","u"]
count = 0
for l in s:
    for v in vowels:
        if l == v:
            count += 1

print("Number of vowels:", count)
