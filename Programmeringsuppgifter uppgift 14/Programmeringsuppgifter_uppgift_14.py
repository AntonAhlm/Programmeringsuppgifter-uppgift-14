print("\n a*x + b = c*x+d \n")

TalA=int(input("Tal A= "))
TalB=int(input("Tal B= "))
TalC=int(input("Tal C= "))
TalD=int(input("Tal D= "))

Tal1=TalD-TalB
Tal2=TalA-TalC
    
if Tal2==0:
    TalX=0
else:
    TalX=(TalD-TalB)/(TalA-TalC)

print("\n",TalA,"*",TalX,"+",TalB,"=",TalC,"*",TalX,"+",TalD,"\n")

vl=TalA*TalX+TalB
hl=TalC*TalX+TalD

if vl!=hl: 
    print("Ekvationen ",vl,"=",hl,"Saknar Losning ")

if TalA*TalX==0 and TalC*TalX==0 and vl==hl :
    print("X = ",TalX)
    print("Ekvationen ",vl,"=",hl,"Har Oandligt Manga Losnignar  ")

if TalA*TalX==0 and TalC*TalX==0 and TalB==TalC and TalX==0 and vl==hl:
    print("X = ",TalX)
    print("Ekvationen ",vl,"=",hl,"Har 1 Losning ")

if TalA*TalX!=0 and TalC*TalX!=0 and vl==hl:
    print("X = ",TalX)
    print("Ekvationen",vl,"=",hl,"Har 1 Losning ")

print("\n\n")