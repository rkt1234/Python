fruits = ["apple", "banana", "mango"]
print(fruits[0])       
print(fruits[-1])      
fruits[1] = "orange"
print(fruits)  

# // Looping throguh list
for fruit in fruits:
    print(fruit)


# // Common list methods


# // | Method          | Usage                          |
# // | --------------- | ------------------------------ |
# // | `.append(x)`    | Add item at end                |
# // | `.insert(i, x)` | Insert at index                |
# // | `.pop()`        | Remove last item (or by index) |
# // | `.remove(x)`    | Remove first occurrence of x   |
# // | `.sort()`       | Sort list in-place             |
# // | `.reverse()`    | Reverse the list               |
# // | `len(list)`     | Get number of elements         |

nums = [10, 5, 7]
nums.append(12)
nums.remove(5)
nums.sort()
print(nums)  



