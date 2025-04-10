from dao.student_dao_impl import StudentDAOImpl
from dao.course_dao_impl import CourseDAOImpl
from dao.enrollment_dao_impl import EnrollmentDAOImpl
from dao.payment_dao_impl import PaymentDAOImpl
from util.DBConnection import DBConnection
from dao.teacher_dao_impl import TeacherDAOImpl
from dao.SIS_dao_impl import SISDAOImpl

from exception.app_exceptions import StudentNotFoundException, CourseNotFoundException

class SISManagement:
    def __init__(self):
        self.conn = DBConnection.get_connection()
        print("Database connection established!")
        self.student_dao = StudentDAOImpl()
        self.course_dao = CourseDAOImpl()
        self.enrollment_dao = EnrollmentDAOImpl()
        self.payment_dao = PaymentDAOImpl()
        self.teacher_dao = TeacherDAOImpl()
        self.sis_dao = SISDAOImpl()

    ####Student Information
    def enrolll_in_course(self):
        self.student_dao.enroll_in_course()
    def update_studnet_info(self):
        self.student_dao.update_student_info()
    def add_student(self):
        self.student_dao.add_student()
    def get_enrollments_for_student(self):
        self.student_dao.get_enrolled_courses()
    def payment_history(self):
        self.student_dao.get_payment_history()
    def make_payment(self):
        self.student_dao.make_payment()
    def display_student_info(self):
        self.student_dao.display_student_info()

    ####
    def get_all_courses(self):
        self.course_dao.get_all_courses()
    def update_course_info(self):
        self.course_dao.update_course_info()
    def display_course_info(self):
        self.course_dao.display_course_info()
    def assign_course_to_teacher(self):
        self.course_dao.assign_teacher()
    def get_courses_for_teacher(self):
        self.course_dao.get_teacher()
    def caluclte_course_stastics(self):
        self.sis_dao.calculate_course_statistics()

    ########
    def get_teacher_assigned_courses(self):
        self.teacher_dao.get_assigned_courses()
    def update_teacher_info(self):
        self.teacher_dao.update_teacher_info()
    def display_teacher_info(self):
        self.teacher_dao.display_teacher_info()

    #####
    def add_enrollment(self):
        self.enrollment_dao.add_enrollment()
    def view_all_enrollments(self):
        self.enrollment_dao.get_all_enrollments()
    def student_enrollment(self):
        self.enrollment_dao.get_student_by_enrollment()
    def course_enrollment(self):
        self.enrollment_dao.get_course_by_enrollment()


    ##
    def add_payment(self):
        self.payment_dao.add_payment()
    def get_payment_by_student(self):
        self.payment_dao.get_student()
    def payment_amount(self):
        self.payment_dao.get_payment_amount()
    def paymnet_dates(self):
        self.payment_dao.get_payment_date()

    ###reports
    def enrollment_report(self):
        self.sis_dao.generate_enrollment_report()
    def payment_report(self):
        self.sis_dao.generate_payment_report()