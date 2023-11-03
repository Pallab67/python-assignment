num=int(input("Enter the five digits Number :"))
sum=0
a=num%10
n=num//10
sum=sum+a
 
a=n%10
n=n//10
sum=sum+a
 
a=n%10
n=n//10
sum=sum+a
 
a=n%10
n=n//10
sum=sum+a
 
a=n%10
sum=sum+a;
print("sum of the Digits = ",sum)