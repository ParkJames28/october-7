userNums = int(input("how many number/s? "))
nums = []
for data in range (userNums):
    nums2 = input("Enter a number/s: ")
    nums.append (nums2)
print (nums)

warning = input ("do you want to clear this list? ")
if warning == "yes":
    nums.clear()
    print (nums)
elif warning == "no":
    print (nums)