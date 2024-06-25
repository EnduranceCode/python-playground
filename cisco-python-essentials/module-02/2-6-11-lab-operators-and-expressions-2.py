hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
new_time_in_minutes = hour * 60 + mins + dura

hour = int(new_time_in_minutes / 60) % 24
mins = new_time_in_minutes % 60

print("New time: " + str(hour) + ":" + str(mins))
