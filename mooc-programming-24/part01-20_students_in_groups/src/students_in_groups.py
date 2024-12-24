# Write your solution here
number_of_students = int(input("How many students on the course? "))
size_of_groups = int(input("Desired group size? "))

number_of_groups_formed = number_of_students // size_of_groups
number_of_ungrouped_students = number_of_students % size_of_groups

if (number_of_ungrouped_students != 0):
    number_of_groups_formed += 1

print(f"Number of groups formed: {number_of_groups_formed}")