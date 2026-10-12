# Lab-1_F-1

input_seconds = int(input("Input seconds: "))

hours = input_seconds // 3600
seconds = input_seconds % 3600
minutes = seconds // 60
leftover_seconds = seconds % 60

print(hours)
print(minutes)
print(leftover_seconds)
