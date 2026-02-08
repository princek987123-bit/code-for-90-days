#if elif ladder 
sub1 = int(input("Enter subject1 marks: "))
sub2 = int(input("Enter subject2 marks: "))
sub3 = int(input("Enter subject3 marks: "))
sub4 = int(input("Enter subject4 marks: "))
sub5 = int(input("Enter subject5 marks: "))

avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5

if avg>=90:
    print("A+")
elif avg>=80:
    print("A")
elif avg>=60:
    print("B+")
elif avg>=50:
    print("B")
elif avg>=33:
    print("C")
else:
    print("Fail ")