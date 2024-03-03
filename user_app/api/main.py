
grades = []

for _ in range(3):
    grade = float(input())
    grades.append(grade)

weighted_average = (grades[0] + grades[1] + grades[2]) / 3
decimal_number = "{:.1f}".format(weighted_average)

print(f"MEDIA = {decimal_number}")