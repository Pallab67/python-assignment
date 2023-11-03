pop=int(input("enter the value:"))
popmen=(52*pop)/100
popwomen=pop-popmen
poplit=(48*pop)/100
litmen=(35*popmen)/100
litwomen= poplit-litmen
illitmen=popmen-litmen
illitwomen=popwomen-litwomen
print("Total Population          : ",pop)
print("Total illiteracy Mens   : ",illitmen)
print("Total illiteracy Womens : ",illitwomen)