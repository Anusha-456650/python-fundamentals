# Student Result Application using functions

def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return total, average, grade


def main():
    print("=== Student Result Calculator ===")

    name = input("Enter student name: ").strip()

    marks = []
    subjects = int(input("Enter number of subjects: "))

    # Taking marks input
    for i in range(subjects):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    # Calling function
    total, average, grade = calculate_result(marks)

    # Display result
    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


# Run the program
main()