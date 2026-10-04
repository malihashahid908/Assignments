def validate_marks(marks):
    """Check the number of marks and their allowed range."""
    if len(marks) != 3:
        raise ValueError("Enter exactly three marks.")
    for mark in marks:
        if not 0 <= mark <= 100:
            raise ValueError("Marks must be between 0 and 100.")


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def determine_grade(average):
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def display_result(name, total, average, grade):
    """Print values that have already been calculated."""
    print("\nStudent Result")
    print("----------------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


def process_student(name, marks):
    """Coordinate validation, calculation, grading and display."""
    validate_marks(marks)
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = determine_grade(average)
    display_result(name, total, average, grade)


def main():
    name = input("Enter student name: ")
    marks = []
    for subject in range(1, 4):
        marks.append(float(input(f"Enter marks for subject {subject}: ")))
    try:
        process_student(name, marks)
    except ValueError as error:
        print("Invalid marks:", error)


if __name__ == "__main__":
    main()
