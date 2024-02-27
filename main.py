from s_list import SList
from course import Course
import random

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
        sumGrades += course.data_obj.grade() * course.data_obj.credit_hr()
        credits += course.data_obj.credit_hr()
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


def test_passed_6():
    cl = SList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    cl.insert(Course(1800))

    if len(cl) != 22:
        print("cl len: " + str(len(cl)))
        print("Unexpected SList length result.")
        return False
    cl.remove_all(1200)
    if len(cl) != 2:
        print("cl len: " + str(len(cl)))
        print("Unexpected SList length result.")
        return False
    else:
        return True
    


def test_passed_5():
    random.seed(0)
    cl = SList()
    courseNumbers = []
    for _ in range(37):
        courseNumbers.append(random.randrange(1000, 7000))
    for number in courseNumbers:
        cl.insert(Course(number, "test", 1.0, 2.0))
    course = cl.find(courseNumbers[0])
    if course.data_obj.number() != courseNumbers[0]:
        #print("Course index failed:\ncourse.number() != courseNumbers[0]")
        return False
    course = cl.find(courseNumbers[10])
    if course.data_obj.number() != courseNumbers[10]:
        #print("Course index failed:\ncourse.number() != courseNumbers[10]")
        return False
    course = cl.find(courseNumbers[36])
    if course.data_obj.number() != courseNumbers[36]:
        #print("Course index failed:\ncourse.number() != courseNumbers[36]")
        return False
    #print("Courses added...")
    for i in range(0, 30, 3):
        cl.remove(courseNumbers[i])
    #print("Courses removed...")
    if len(cl) != 27:
        #print("Unexpected SList length result.")
        return False
    if is_sorted(cl) is False:
        #print("SList is not sorted.")
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
    
    # print(arr)
    print(test_passed_5())

if __name__ == "__main__":
    main()
    
    
  