from process_data import process_courses


def add_math_courses(course_list, is_honors):

        math_course_list = []

        if is_honors:
                math_course_list.append(process_courses.pop_course("MATH1941", course_list))
                math_course_list.append(process_courses.pop_course("MATH1942", course_list))
        else:
                math_course_list.append(process_courses.pop_course("MATH1041", course_list))
                math_course_list.append(process_courses.pop_course("MATH1042", course_list))

        return math_course_list
