''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object 
    
    Attributes:
        number (int): The course number
        name (str): The name of the course
        credit_hours (float): The number of credit hours
        grade (float): The grade received for the course
    '''

    def __init__(self, number: int = 0, name: str = "", credit_hours: float = 0.0, grade: float = 0.0):
        """
        Initializes a new instance of the Course class.

        Args:
            number (int): course number
            name (str): name of the course
            credit_hours (float): total credit hours
            grade (float): grade received (0.0-4.0)

        Raises:
            ValueError: If any parameter is of the wrong type or an inappropriate value.
        """
        # number must be an int greater than -1
            # otherwise raises ValueError

        # name must be a string and is not None
            # otherwise raises ValueError
        
        # credit_hours must be a float >= 0.0
            # otherwise raises ValueError

        # grade must be a float >= 0.0 AND <= 4.0 
            # otherwise raise a ValueError

        if not isinstance(number, int):
            raise ValueError("Course number must be an integer")
        if number <= -1:
            raise ValueError("Course number must be a positive integer")
        if not isinstance(name, str):
            raise ValueError("Course name must be a valid string")
        if not isinstance(credit_hours, float):
            raise ValueError("Credit hours must be a float")
        if credit_hours < 0:
            raise ValueError("Credit hours must be 0 or greater")
        if not isinstance(grade, float):
            raise ValueError("Grade must be a float")
        if grade < 0 or grade > 4.0:
            raise ValueError("Grade must be in the range 0.0 to 4.0")

        self._number = number
        self._name = name
        self._credit_hours = credit_hours
        self._grade = grade


    def __eq__(self, other: 'Course') -> bool:
        """
        Checks if this course is equal to another based on the course number.

        Args:
            other (Course): The course to compare with.

        Returns:
        bool: True if course numbers are equal, False if not equal.
        """
        if isinstance(other, Course):
            return self.number == other.number
        return False

    def __ne__(self, other: 'Course') -> bool:
        """
        Checks if this course is not equal to another based on the course number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if course numbers are not equal, False if equal.
        """
        if isinstance(other, Course):
            return self.number != other.number
        return True

    def __lt__(self, other: 'Course') -> bool:
        """
        Checks if this course number is less than another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if self.number is less than other.number, False otherwise.
        """
        if isinstance(other, Course):
            return self.number < other.number
        raise TypeError("Cannot compare course with non-course object")
        
    def __gt__(self, other: 'Course') -> bool:
        """
        Checks if this course number is greater than another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if self.number is greater than other.number, False otherwise.
        """
        if isinstance(other, Course):
            return self.number > other.number
        raise TypeError("Cannot compare course with non-course object")
    
    def __le__(self, other: 'Course') -> bool:
        """
        Checks if this course number is less than or equal to another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if self.number is less than or equal to other.number, False otherwise.
        """
        if isinstance(other, Course):
            return self.number <= other.number
        raise TypeError("Cannot compare course with non-course object")
        
    def __ge__(self, other: 'Course') -> bool:
        """
        Checks if this course number is greater than or equal to another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if self.number is greater than or equal to other.number, False otherwise.
        """
        if isinstance(other, Course):
            return self.number >= other.number
        raise TypeError("Cannot compare course with non-course object")
            
    def __str__(self) -> str:
        """
        Returns a string representation of the course including its number, name, grade, and credit hours.

        Returns:
            str: The string representation of the course.
        """
        return (
            f"Course Information:\n"
            f"  Number: {self._number}\n"
            f"  Name: {self._name}\n"
            f"  Credit Hours: {self._credit_hours}\n"
            f"  Grade: {self._grade}"
        )

            
    def name(self) -> str:
        """
        Returns the name of the course.

        Returns:
            str: course name.
        """
        return self._name
            
    def number(self) -> int:
        """
        Returns the course number.

        Returns:
            int: course number.
        """
        return self._number
            
    def credit_hr(self) -> float:
        """
        Returns the number of credit hours for the course.

        Returns:
            float: number of credit hours.
        """
        return self._credit_hours
            
    def grade(self) -> float:
        """
        Returns the grade received for the course.

        Returns:
            float: The grade.
        """
        return self._grade
