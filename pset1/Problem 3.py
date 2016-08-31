# Problem Set 1 / Problem 3
# 31 August 2016
# @Dehan Lamprecht
# for MITx 6.00.1x

def isinorder(chr1,chr2):
    if ord(chr1) <= ord(chr2):
        return True
    else:
        return False

#s = "abcdefghijklmnopqrstuvwxyz"
longest1 = ""
longest2 = ""

count = 0
start = 0
for i in range(len(s)-1):
    if isinorder(s[i], s[i + 1]):
        count += 1
    else:
        longest2 = s[start:(start+count+1)]
        count = 0
        start = i + 1
    if len(longest2) > len(longest1):
        longest1 = longest2

longest2 = s[start:start+count+1]
if len(longest2) > len(longest1):
    longest1 = longest2
print("Longest substring in alphabetical order is:", longest1)
