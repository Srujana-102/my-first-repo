##Docstring:--
'''
You are building a simple marks analysis utility. Complete the following tasks in order.

Task 1. Write a function calculate_total(marks) that accepts a list of marks and returns their sum.

Task 2. Write a function calculate_average(marks) that calls calculate_total() and returns the average.

Task 3. Write a function get_grade(average) that returns "A" if average > 90, "B" if average > 75, and "C" otherwise.

Task 4. Write a function display_report(marks) that calls all three functions above and prints:

Total: <value>
Average: <value>
Grade: <value>
Task 5. Add a docstring to each function describing what it does.

Test your solution with the list [88, 76, 95, 60, 82].
'''
##Codes:--
#Task 1
def calculate_total(marks):
    return sum(marks)
#Task 2
average=0
def calculate_average(marks):
    average=calculate_total(marks)/len(marks)
    return average
#Task 3
def get_grade(average):
    if average>90:
        return "A"
    elif average>75 and average<90:
        return "B"
    else:
        return "C"
#Task 4
def display_report(marks):
    total=calculate_total(marks)
    avg=calculate_average(marks)
    grade=get_grade(average)
    print(f"Total: {total}\nAverage: {avg}\nGrade: {grade}")
#Task 5
display_report([88, 76, 95, 60, 82])