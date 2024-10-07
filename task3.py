userNums = int(input("how many number/s? "))
nums = []
for data in range (userNums):
    nums2 = input("Enter a number/s: ")
    nums.append (nums2)
print (nums)

warning = input("do you want to remove your list by index or by value? ")

if warning == "index":
    print(nums)
    index = int(input("which index? "))
    nums.pop(index)
elif warning == "value":
    print(nums)
    value = (input("which value do you want to remove? "))
    nums.remove(value)

print(nums)