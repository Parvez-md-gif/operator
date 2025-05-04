#1
a = input("enter your string: ")
print(a)



#2
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count


string = "Hello, rahul_sir"
print("Number of vowels:", count_vowels(string))




string = "Hello, rahul_sir"
reversed_string = string[::-1]
words_reversed = " ".join(reversed_string.split()[::-1])
print(words_reversed)



# 3define name of 10 string in list and find their duplicate value or araange in decending order


names = ["shivam", "rahul", "shivam", "kohli", "abd", "rahul", "vaishali", "kohli", "abd", "rahul"]


duplicates = {name for name in names if names.count(name) > 1}


sorted_names = sorted(names, reverse=True)

print("Duplicate values:", duplicates)
print("Sorted list in descending order:", sorted_names)






#5
for i in range(1, 6):
    print("*" * i)




#6
def calculate_grade(average):
    if average > 90:
        return 'A'
    elif 75 <= average < 90:
        return 'B'
    elif 60 <= average < 75:
        return 'C'
    else:
        return 'D'


name = input("Enter student name: ")
marks = []
for i in range(3):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)


total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)


print("-" * 30)
print(f"{name:<10}{total:<15}{average:<10.2f}{grade:<10}")




