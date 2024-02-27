from s_list import SList
from course import Course

def calculate_gpa(courseList: SList) -> float:
    """
    Calculates the GPA based on a list of Course objects.

    Parameters:
        courseList (SList): A sorted list containing Course objects.

    Returns:
        float: The calculated GPA.
    """
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.value.grade() * course.value.credit_hr()
        credits += course.value.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst: SList) -> bool:
    """
    Checks if the provided list is sorted.

    Parameters:
        lyst (SList): A sorted list containing Course objects.

    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    for i in range(0, len(lyst)  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True


def main():
    
    math_1 = Course(1010, "Algebra", 4.0, 3.0)
    math_2 = Course(1010, "Algebra", 4.0, 3.5)
    english = Course(2030, "English", 4.0, 3.8)
    science = Course(3000, "Biology", 4.0, 3.9)
    art = Course(4810, "Painting", 4.0, 3.1)
    
    arr = SList()
    arr.insert(math_1)
    arr.insert(math_2)
    arr.insert(art)
    arr.insert(science)
    arr.insert(english)

    print(arr)

if __name__ == "__main__":
    main()