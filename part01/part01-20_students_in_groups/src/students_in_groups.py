# Write your solution here
total_students = int(input("How many students on the course?  "))
grp_size = int(input("Desired group size? "))
grp_form = total_students // grp_size
if (total_students % grp_size) != 0:
    grp_form += 1
print(f"Number of groups formed: {grp_form}")