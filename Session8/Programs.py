# write a list comprehension in python to get a list of even numbers when a range is given 
N = 20
number_list = [ x for x in range(N) if x % 2 == 0]
print(f'List of Even Numbers:', number_list)


# write a list comprehension in python to get a list of odd numbers when a range is given 
N = 20
number_list = [ x for x in range(N) if x % 2 != 0]
print(f'List of Odd Numbers:', number_list)


# write a python function to display the Fibonacci series
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# write a python lambda function to get remainder when divisor and divident are given
remainder = lambda Divident, Divisor: Divident % Divisor
print(remainder(5,2))

# write a python function to print whether the given year is a leap year or not
 def leapYear(year):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} is a leap year".format(year))
           else:
               print("{0} is not a leap year".format(year))
       else:
           print("{0} is a leap year".format(year))
    else:
       print("{0} is not a leap year".format(year))

# write a python function to convert degree celsius to degree fahrenheit
def fahrenheit(celsius):
    return (celsius * 1.8) + 32

# write a python function to convert degree fahrenheit to degree celsius
 def celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8
    
# write a python function to get the factorial of a given number
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
        
# write a python function to compute the HCF of two numbers
def hcf(x, y):

    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

# write a python function to compute the lcm of two numbers
 def lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
   
 # write a python function to check whether the number is an Armstrong number or not
 def Armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   
    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")
       
 # write a python function to check whether the string is a palindrome or not
 def palindrome(my_str):
    my_str = my_str.casefold()
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
       print("The string is a palindrome.")
    else:
       print("The string is not a palindrome.")
 
# write a python program to remove punctuations in a string
 punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 string = ''.join(e for e in d if e not in punctuations)
 
# write a python program to print the ASCII value of a character
 c = 'p'
 print("The ASCII value of '" + c + "' is", ord(c))

# write a python program to swap two numbers
 a = 1
 b = 2
 a, b = b, a

# write a python lambda function to add three numbers
 x = lambda a, b, c : a + b + c
 print(x(5, 6, 2))
 
# write a python function to check whether the number is a Magic number or not
 def isMagic(n): 
    sum = 0
    
    while (n > 0 or sum > 9): 
        if (n == 0): 
            n = sum; 
            sum = 0; 
        sum = sum + n % 10; 
        n = int(n / 10); 
        
    return True if (sum == 1) else False;

# write a python program to convert a list of values in kilometers to feet
 kilometer = [39.2, 36.5, 37.3, 37.8]
 feet = map(lambda x: float(3280.8399)*x, kilometer)
 print(list(feet))
 
# write a python list comprehension to flatten a list of lists
 list_of_list = [[1,2,3],[4,5,6],[7,8]]`
 flatten = [y for x in list_of_list for y in x]
 
# write a python list comprehension to transpose a 2D matrix (provided as list)
 matrix = [[1,2,3],[4,5,6],[7,8,9]]
 matrixT = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
 
# write a python list comprehension to print numbers in a given string
 string = "Hello 12345 World"
 numbers = [x for x in string if x.isdigit()]
 print (numbers)
 
# write a python function for binary search

def binary_search(arr, low, high, x): 
    if high >= low: 
  
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 

        else: 
            return binary_search(arr, mid + 1, high, x) 
    else: 
        return -1
 
# write a python function to bubblesort an array
 
 def bubbleSort(arr): 
    n = len(arr) 

    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 


# write a python program to do selection sort

A = [64, 25, 12, 22, 11] 

for i in range(len(A)): 

    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
      
    A[i], A[min_idx] = A[min_idx], A[i] 

print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i])
    
# write a python function to do insertion sort

def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
 
 # write a python program to print prime numbers within a range
 
 lower = 5
 upper = 20

 print("Prime numbers between", lower, "and", upper, "are:")

 for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
 
# write a python proram to check whether the number is prime

num = 407
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")
 
# write a python function to linearly search an array for a given number and return its index else return -1

def search(arr, n, x): 
    for i in range(0, n): 
        if (arr[i] == x): 
            return i 
    return -1
  
  
# write a python function to check whether the number is a lucky number 

def isLucky(n):
    
    isLucky.counter = 2
    next_position = n 
    if isLucky.counter > n:
        return 1
    if n % isLucky.counter == 0:
        return 0
    next_position = next_position - next_position /isLucky.counter
    isLucky.counter = isLucky.counter + 1
    return isLucky(next_position)
 
# write a python function to obtain the square root of a number
 
 def squareRoot(n): 
        x = n 
        y = 1
        e = 0.000001
        while(x - y > e):  
            x = (x + y)/2
            y = n / x   
        return x 

# write a python function to convert a number from decimal to binary
 
 def decToBinary(n): 
    binaryNum = [0] * n;  
    i = 0; 
    while (n > 0):   
        binaryNum[i] = n % 2; 
        n = int(n / 2); 
        i += 1; 
    for j in range(i - 1, -1, -1): 
        print(binaryNum[j], end = ""); 
 
# write a python function to convert a number from binary to decimal
 
 def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base = 1;  
    temp = num;
    while(temp):
        last_digit = temp % 10;
        temp = int(temp / 10);
         
        dec_value += last_digit * base;
        base = base * 2;
    return dec_value;
    
# write a python function to convert a number from decimal to octal
 
 def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")
      
# write a python function to convert a number from octal to decimal
    
  def octalToDecimal(n): 
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while (temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
        dec_value += last_digit * base; 
        base = base * 8; 
  
    return dec_value; 
    
# write a dictionary comprehension in python so that the values are square of the key number
  
  square_dict = {num: num*num for num in range(1, 11)}
  print(square_dict)
  
# write a python program to get indexes for each element in a list using enumerate
  
  l1 = ["eat","sleep","repeat"] 
  for ele in enumerate(l1): 
      print (ele) 
    
# write a python program to get indexes starting at a specified number for each element in a list using enumerate
  
  l1 = ["eat","sleep","repeat"] 
  for count,ele in enumerate(l1,100): 
      print (count,ele )
      
# write a python program to demonstarate working of map
  
  def addition(n): 
    return n + n   
  numbers = (1, 2, 3, 4) 
  result = map(addition, numbers) 
  print(list(result)) 
  
# write a python function to calculate simple interest
  
  def simple_interest(p,t,r):  
    si = (p * t * r)/100    
    return si 
    
 # write a python function to calculate compound interest
 
 def compound_interest(principle, rate, time): 
    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    print("Compound interest is", CI) 

# write a python function to convert a list of characters to a string

 def convert(s): 
     str1 = "" 
     return(str1.join(s)) 

# write a python function to check whether a number is perfect

 def isPerfect( n ): 
     sum = 1
     i = 2
     while i * i <= n: 
         if n % i == 0: 
             sum = sum + i + n/i 
         i += 1
     return (True if sum == n and n!=1 else False) 

# write a python function to find the sum of digits in a number until one digit (no more than one digit)

 def digSum(n): 
    sum = 0
    while(n > 0 or sum > 9): 
      
        if(n == 0): 
            n = sum
            sum = 0         
        sum += n % 10
        n = int(n/10)    
    return sum
 
# write a python function to get the sum of numbers in a given digit
 
 def getSum(n):     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
 

# write a python function to find the largest number in an array

 def largest(arr,n): 
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max

# write a python function to find the nth catalan number

def catalan(n): 
    # Base Case 
    if n <= 1: 
        return 1
    res = 0
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
    return res 

# write a python function to convert decimal to hexadecimal

 def decToHexa(n): 
    hexaDeciNum = ['0'] * 100; 
    i = 0; 
    while(n != 0):  
        temp = 0;  
        temp = n % 16; 
        if(temp < 10): 
            hexaDeciNum[i] = chr(temp + 48); 
            i = i + 1; 
        else: 
            hexaDeciNum[i] = chr(temp + 55); 
            i = i + 1; 
        n = int(n / 16); 
    j = i - 1; 
    while(j >= 0): 
        print((hexaDeciNum[j]), end = ""); 
        j = j - 1;
 
# write a python program to convert hexadecimal to decimal
 
 def hexadecimalToDecimal(hexval): 
    length = len(hexval) 
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):  
        if hexval[i] >= '0' and hexval[i] <= '9': 
            dec_val += (ord(hexval[i]) - 48) * base 
            base = base * 16
        elif hexval[i] >= 'A' and hexval[i] <= 'F': 
            dec_val += (ord(hexval[i]) - 55) * base 
            base = base * 16
    return dec_val
 
# write a python program to add two hexadecimal numbers
 
 a = "B"
 b = "C"
 sum = hex(int(a, 16) + int(b, 16)) 
 print(sum[2:]) 
 
# write a python program to add two octal numbers
 
 a = "123"
 b = "456"
 sum = oct(int(a, 8) + int(b, 8)) 
 print(sum[2:]) 
 
# write a python program to add two binary numbers
 
 a = "1101"
 b = "100"
 sum = bin(int(a, 2) + int(b, 2))  
 print(sum[2:]) 
 
# write s python program to print the union of two sets

 A = {1, 2, 3, 4, 5}
 B = {4, 5, 6, 7, 8}
 print(A | B)
 
# write s python program to print the intersection of two sets

 A = {1, 2, 3, 4, 5}
 B = {4, 5, 6, 7, 8}
 print(A & B)
 
 
# write s python program to print the difference of two sets
 A = {1, 2, 3, 4, 5}
 B = {4, 5, 6, 7, 8}
 print(A - B)
 
# write s python program to print the symmetric difference of two sets

 A = {1, 2, 3, 4, 5}
 B = {4, 5, 6, 7, 8}
 print(A ^ B)
 
# write a python function to find nCr
 
 def nCr(n, r): 

    def fact(n): 
        res = 1
        for i in range(2, n+1): 
            res = res * i 
        return res
    
    return (fact(n) / (fact(r)  
                * fact(n - r)))

# write a python function to calculate nPr

 def nPr(n, r):  
    
    def fact(n):  
        if (n <= 1): 
            return 1
        return n * fact(n - 1)

    return int(fact(n) /
                fact(n - r))
                
# write a python function to calculate the volume of ellipsoid

 def volumeOfEllipsoid(r1, r2, r3): 
    return 1.33 * 22 * r1 * r2 * r3/7
    
# write a python function to calculate the area of tetraheadron

 def area_of_tetrahedron(side): 
    return (1.73205 * 
           (side * side));
           
# write a python function to find the volume of tetraheadron

 def vol_tetra(side): 
    volume = (side ** 3 / (6 * 1.414)) 
    return round(volume, 2)
 
# write a python function to determing the volume of a cube whose space diagonal measure is given
 
  def CubeVolume(d): 
    Volume = (1.73205 * pow(d, 3)) / 9
    return Volume
    
# write a python function to calcuate the easter date using Gauss's Algorithm

 def gaussEaster(Y):
    A = Y % 19
    B = Y % 4
    C = Y % 7

    P = int(Y / 100)
    Q = int((13 + 8 * P) / 25)
    M = (15 - Q + P - P // 4) % 30
    N = (4 + P - P // 4) % 7
    D = (19 * A + M) % 30
    E = (2 * B + 4 * C + 6 * D + N) % 7
    days = (22 + D + E)
    if ((D == 29) and (E == 6)):
        print(Y, "-04-19")
        return
    elif ((D == 28) and (E == 6)):
        print(Y, "-04-18")
        return

    else:
        if (days > 31):
            print(Y, "-04-", (days - 31))
            return

        else:
            print(Y, "-03-", days)
            return
     