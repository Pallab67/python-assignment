num = int(input("Enter the Five Digits :"))

sum = 0
a = (num // 10000)+1
num = num % 10000
sum=sum+(a*10000);
 
a = (num // 1000)+1
num = num % 1000
sum = sum+(a*1000)
 
a = (num // 100)+1
num = num % 100
sum = sum+(a*100)
 
 
a = (num // 10)+1
num = num % 10

 
 
a = num+1
sum = sum+a

print(" Number :",sum)