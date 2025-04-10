from SIS.SIS_Managment import *

def main():
    sis = SISManagement()

    while True:
        print("\n========== STUDENT INFORMATION SYSTEM (SIS) ==========")
        print("STUDENT OPERATIONS")
        print("1. Add Student")
        print("2. Update Student Info")
        print("3. Get Enrollments for a Student")
        print("4. Get Payment History for a Student")
        print("5. Enroll Student in a Course")
        print("6. Make Student Payment")
        print("7. Displaying Student Information")

        print("\nCOURSE OPERATIONS")
        print("8. Get all available courses")
        print("9. Update Course Info")
        print("10. Display All Courses")
        print("11. Assign Teacher to Course")
        print("12. Get Courses for a Teacher")
        print("13. Calculate Course Statistics")

        print("\nTEACHER OPERATIONS")
        print("14. Get Teacher assigned courses")
        print("15. Update Teacher Info")
        print("16. Display Teacher Info")

        print("\nENROLLMENT OPERATIONS")
        print("17. Add Enrollment")
        print("18. View All Enrollments")
        print("19. Enter Student_id to get all enrollments")
        print("20. Enter course Id to get all enrollments")

        print("\nPAYMENT OPERATIONS")
        print("21. Add Payment")
        print("22. Get Payments done by student")
        print("23. Get Amount of Payments done by student")
        print("24. Get payment dates for student")

        print("\nREPORTS")
        print("25. Generate Enrollment Report by Course")
        print("26. Generate Payment Report by Student")

        print("\n0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            sis.add_student()
        elif choice == '2':
            sis.update_studnet_info()
        elif choice == '3':
            sis.get_enrollments_for_student()
        elif choice == '4':
            sis.payment_history()
        elif choice == '5':
            sis.enrolll_in_course()
        elif choice == '6':
            sis.make_payment()
        elif choice == '7':
            sis.display_student_info()
        elif choice == '8':
            sis.get_all_courses()
        elif choice == '9':
            sis.update_course_info()
        elif choice == '10':
            sis.display_course_info()
        elif choice == '11':
            sis.assign_course_to_teacher()
        elif choice == '12':
            sis.get_courses_for_teacher()
        elif choice == '13':
            sis.caluclte_course_stastics()
        elif choice == '14':
            sis.get_courses_for_teacher()
        elif choice == '15':
            sis.update_teacher_info()
        elif choice == '16':
            sis.display_teacher_info()
        elif choice == '17':
            sis.add_enrollment()
        elif choice == '18':
            sis.view_all_enrollments()
        elif choice == '19':
            sis.student_enrollment()
        elif choice == '20':
            sis.course_enrollment()
        elif choice == '21':
            sis.add_payment()
        elif choice == '22':
            sis.get_payment_by_student()
        elif choice == '23':
            sis.payment_amount()
        elif choice == '24':
            sis.paymnet_dates()
        elif choice == '25':
            sis.enrollment_report()
        elif choice == '26':
            sis.payment_report()
        elif choice == '0':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
