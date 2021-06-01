Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input("Enter a number: "))  
Enter a number: 7
>>> 
>>> if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")    
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")

   
7 is a prime number

>>> num=int(input('enter the number'))
enter the number 9
>>> if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")   
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")

   
9 is not a prime number
>>> 