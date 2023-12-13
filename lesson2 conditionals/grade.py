score = int(input("Score: "))

#为了减少逻辑判断，要使用if 与efif ，而不要一直使用if。
if 90<= score <= 100:
    print("Grade A")
elif 80<= score < 90:
    print("Grade B")
elif 70<= score < 80:
    print("Grade C")
elif 60<= score < 70:
    print("Grade D")
else:
    print("Grade F")        
