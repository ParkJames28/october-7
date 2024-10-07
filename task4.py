userNums = int(input("how many number/s? "))
nums = []
for data in range (userNums):
    nums2 = input("Enter a number/s: ")
    nums.append (nums2)
print (nums)

warning = input("do you want to sort or reverse? ")
if warning == "sort":
    nums.sort()
elif warning == "reverse":
    nums.reverse()

print (nums)