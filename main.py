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
    arr = SList()
    arr.insert(1)
    arr.insert(2)
    arr.insert(5)
    arr.insert(2)

    print(arr)

if __name__ == "__main__":
    main()