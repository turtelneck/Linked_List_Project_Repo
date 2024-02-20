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


        # magic methods
    def __eq__(self, other: 'Course') -> bool:
        """
        Checks if this course is equal to another based on the course number.

        Args:
            other (Course): The course to compare with.

        Returns:
        bool: True if the course numbers are the same, False otherwise.
        """
        pass

    def __ne__(self, other: 'Course') -> bool:
        """
        Checks if this course is not equal to another based on the course number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if the course numbers are different, False otherwise.
        """
        pass

    def __lt__(self, other: 'Course') -> bool:
        """
        Checks if this course number is less than another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if this course number is less than the other's, False otherwise.
        """
        pass
        
    def __gt__(self, other: 'Course') -> bool:
        """
        Checks if this course number is greater than another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if this course number is greater than the other's, False otherwise.
        """
        pass
    
    def __le__(self, other: 'Course') -> bool:
        """
        Checks if this course number is less than or equal to another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if this course number is less than or equal to the other's, False otherwise.
        """
        pass
        
    def __ge__(self, other: 'Course') -> bool:
        """
        Checks if this course number is greater than or equal to another course's number.

        Args:
            other (Course): The course to compare with.

        Returns:
            bool: True if this course number is greater than or equal to the other's, False otherwise.
        """
        pass
            
    def __str__(self) -> str:
        """
        Returns a string representation of the course including its number, name, grade, and credit hours.

        Returns:
            str: The string representation of the course.
        """
        pass
            
    def name(self) -> str:
        """
        Returns the name of the course.

        Returns:
            str: The course name.
        """
        pass
            
    def number(self) -> int:
        """
        Returns the course number.

        Returns:
            int: The course number.
        """
        pass
            
    def credit_hr(self) -> float:
        """
        Returns the number of credit hours for the course.

        Returns:
            float: The number of credit hours.
        """
        pass
            
    def grade(self) -> float:
        """
        Returns the grade received for the course.

        Returns:
            float: The grade.
        """
        pass