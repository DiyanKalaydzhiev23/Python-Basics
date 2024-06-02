exam_hour = int(input())  # 10
exam_minutes = int(input())  # 30

student_hour = int(input())  # 9
student_minutes = int(input())  # 00

exam_time_in_minutes = exam_hour * 60 + exam_minutes  # 10 * 60 + 30  => 630
student_time_in_minutes = student_hour * 60 + student_minutes  # 10 * 60 + 0 => 540

time_diff = exam_time_in_minutes - student_time_in_minutes  # 630 - 540 => 90

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = abs(time_diff) // 60  # 90 // 60 => 1
minutes = abs(time_diff) % 60  # 90 % 60 => 30

result = ""

if hours > 0:
    result = f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result = f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"

print(result)
