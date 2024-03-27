#P(A|B) = A happening and B happened
#P(B|A) = B happening and A happened
print("Keep 1 if value is not available\nProvide only digits. Don't provide Percentile.")
A=eval(input("Enter Probability of A :"))
B=eval(input("Enter Probability of B :"))
AB=eval(input("Enter Probability of A|B intersection A|B  :"))
C=A*B #intersection of A and B
choice=  int(input("1.P(A|B)\n2.P(B|A)\n3.P(A)\n4.P(B)"))
if choice == 1:
  PA_B=(C/B)*100
  print("The Probality is {} % ".format(PA_B))
elif choice == 2:
  PB_A=(C/A)*100
  print("The Probality is {} % ".format(PB_A))
elif choice == 3:
  PA = (AB/B)*100
  print("The Probality is {} % ".format(PA))
elif choice == 4:
  PB = (AB/A)*100
  print("The Probality is {} % ".format(PB))  
else :
  print("Inavlid Choice.")
