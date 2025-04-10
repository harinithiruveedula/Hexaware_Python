#Thrown when a student is already enrolled in a course and tries to enroll again
class DuplicateEnrollmentException(Exception):
    def __init__(self):
        self.message = "Student is already enrolled in this course."

    def __str__(self):
        return self.message
#course not found exception
class CourseNotFoundException(Exception):
    def __init__(self):
        self.message = "Course not found"
    def __str__(self):
        return self.message

#student not found exception
class StudentNotFoundException(Exception):
    def __init__(self):
        self.message = "Student not found"
    def __str__(self):
        return self.message
#teacher
class TeacherNotFoundException(Exception):
    def __init__(self):
        self.message = "Teacher not found"
    def __str__(self):
        return self.message
#paymnet
class PaymnetValidException(Exception):
    def __init__(self):
        self.message = "Paymnet is not valid"
    def __str__(self):
        return self.message
#
class InvalidStudentException(Exception):
    def __init__(self):
        self.message = "Invalid student number"
    def __str__(self):
        return self.message
#invalid course
class InvalidCourseException(Exception):
    def __init__(self):
        self.message = "Invalid course number"
    def __str__(self):
        return self.message
#invalid enrollment data
class InvalidEnrollmentDataException(Exception):
    def __init__(self):
        self.message = "Invalid enrollment number"
    def __str__(self):
        return self.message
#
class InvalidTeacherDataException(Exception):
    def __init__(self):
        self.message = "Invalid teacher number"
    def __str__(self):
        return self.message
#
class InsufficentFundsException(Exception):
    def __init__(self):
        self.message = "Insufficient funds"
    def __str__(self):
        return self.message



