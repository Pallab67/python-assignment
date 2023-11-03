n=int(input("Enter the four Digits Number :"))
sum=0
a=n//1000
sum=sum+a
a=n%10
sum=sum+a
print("Sum of First and Last digits =",sum)
