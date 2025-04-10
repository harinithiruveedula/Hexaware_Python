import pyodbc
from dao.course_dao import CourseDAO
from entity.course import Course
from util.DBConnection import DBConnection

class CourseDAOImpl(CourseDAO):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def get_all_courses(self):
        courses = []
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT course_id, course_name, credits FROM info.courses")
            rows = cursor.fetchall()
            for row in rows:
                course = Course(row[0], row[1], row[2])
                courses.append(course)
        except Exception as e:
            print("Error fetching courses:", e)
        return courses

    def assign_teacher(self) -> bool:
        try:
            course_id = int(input("Enter Course ID to assign a teacher: "))
            teacher_id = int(input("Enter Teacher ID to assign to the course: "))

            update_query = """
                UPDATE info.courses
                SET teacher_id = ?
                WHERE course_id = ?
            """

            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute(update_query, (teacher_id, course_id))
            conn.commit()

            if cursor.rowcount > 0:
                print("Teacher assigned successfully to the course.")
                return True
            else:
                print("No matching course found or no update made.")
                return False

        except Exception as e:
            print("Error assigning teacher:", e)
            return False


    def update_course_info(self):
            try:
                course_id = int(input("Enter the Course ID to update: "))

                print("\nWhich field do you want to update?")
                print("1. Course Code")
                print("2. Course Name")
                print("3. Instructor ID")
                choice = input("Enter your choice (1-3): ")

                field_map = {
                    '1': 'course_code',
                    '2': 'course_name',
                    '3': 'instructor_id'
                }

                if choice not in field_map:
                    print("Invalid choice.")
                    return False

                new_value = input(f"Enter new value for {field_map[choice]}: ")

                # Convert instructor_id to int
                if field_map[choice] == 'instructor_id':
                    new_value = int(new_value)

                update_query = f"UPDATE info.courses SET {field_map[choice]} = ? WHERE course_id = ?"

                conn = DBConnection.get_connection()
                cursor = conn.cursor()
                cursor.execute(update_query, (new_value, course_id))
                conn.commit()
                conn.close()

                if cursor.rowcount > 0:
                    print("Course updated successfully.")
                    return True
                else:
                    print("No course found with the given ID.")
                    return False

            except Exception as e:
                print("Error updating course:", e)
                return False

    def display_course_info(self):
        try:
            course_id = int(input("Enter Course ID to display info: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = '''
            SELECT c.course_id, c.course_name,c.credits, 
                   t.teacher_id, t.first_name, t.last_name
            FROM info.courses c
            LEFT JOIN info.teachers t ON c.teacher_id = t.teacher_id
            WHERE c.course_id = ?
            '''

            cursor.execute(query, (course_id,))
            course = cursor.fetchone()
            conn.close()

            if course:
                print("\n--- Course Details ---")
                print(f"Course ID     : {course[0]}")
                print(f"Course Code   : {course[1]}")
                print(f"Course Name   : {course[2]}")
                print(f"Instructor ID : {course[3] if course[3] else 'N/A'}")
                print(f"Instructor    : {course[4]} {course[5]}" if course[3] else "Instructor    : Not Assigned")
            else:
                print("No course found with the given ID.")

        except Exception as e:
            print("Error fetching course info:", e)

    def get_teacher(self):
        try:
            course_id = int(input("Enter Course ID to get assigned teacher: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = '''
            SELECT t.teacher_id, t.first_name, t.last_name, t.email
            FROM info.courses c
            INNER JOIN info.teachers t ON c.teacher_id = t.teacher_id
            WHERE c.course_id = ?
            '''

            cursor.execute(query, (course_id,))
            teacher = cursor.fetchone()
            conn.close()

            if teacher:
                print("\n--- Assigned Teacher Details ---")
                print(f"Teacher ID   : {teacher[0]}")
                print(f"Name         : {teacher[1]} {teacher[2]}")
                print(f"Email        : {teacher[3]}")

            else:
                print("No teacher assigned or course not found.")

        except Exception as e:
            print("Error fetching teacher:", e)