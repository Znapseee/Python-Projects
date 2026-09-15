# Exercise 1: Create a right triangle using for loop
row1 = 7

for i in range(1, 8):
    print("#" * i)
    

# Exercise 2: Create an 8x8 pound pattern
row2 = 8

for i in range(1, row2+1):
    bars = "# " * 8
    print(bars)

    
# Exercise 3: Crete a list of perfect square numbers in a x a = b format.
row3 = 10

for i in range(0, row3 + 1):
    product = i * i
    print(f"{i} x {i} = {product}")

# Exercise 4: Print the sum of the number from 0 to 100
total = 0
for i in range(0, 101):
    total += i

print(total)

# Exercise 5: Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds
total1 = 0
total2 = 0

for i in range(0, 101):
    if i % 2 == 0:
        total1 += i
    else:
        total2 += i

print(f"The sum of all evens is {total1}. And the sum of all odds is {total2}.")