a = int(input("Enter a number: "))
n = int(input("Enter the power: "))

answer = 1

for i in range(n):
    answer = answer * a

print("Answer =", answer)