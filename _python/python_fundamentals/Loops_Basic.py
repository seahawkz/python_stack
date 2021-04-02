# print all numbers from 0 to 150
for n in range(151):
    print(n)
# print all multiples of 5 from 5 to 1000
for n in range(5,1001,5):
    print(n)
# Print integers 1 to 100, if divisable by 5 print Coding, if divisable by 10 print Coding Dojo
for n in range(1,101):
    if n%10 ==0:
        print('Coding Dojo')
    elif n%5 ==0:
        print('Coding')
    else:
        print(n)
# Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for n in range(500001):
    if n%2==1:
        sum += n
print(sum)
# Print positive numbers starting at 2018, counting down by fours
for n in range(2018,0,-4):
    print(n)
# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult
low_num = 2
high_num = 9
mult = 3
for n in range(low_num, high_num + 1):
    if n % mult == 0:
        print(n)