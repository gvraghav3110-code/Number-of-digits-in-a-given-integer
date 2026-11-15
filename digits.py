N=int(input("Please enter the integer:"))
N=abs(N)
counter=0
if N==0:
  counter=1
else:
  while N>0:
    counter=counter+1
    N = N//10
print("The digits are:",counter)
