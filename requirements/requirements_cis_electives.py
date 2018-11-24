import random
from process_data import process_courses, process_prerequisites


def add_cis_elective_courses(course_list, is_honors):

        elective_credit_count = 0.0
        elective_taken_list = []
        has_math = False

        process_courses.find_course("CIS4282", course_list).prereqs = \
                process_courses.find_course("CIS3603", course_list).prereqs

        cis_elective_list = []
        cis_elective_list.append(process_courses.find_course("CIS3203", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3211", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3219", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3242", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3308", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3319", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3381", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3515", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3603", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3715", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4282", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4305", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4307", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4308", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4319", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4324", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4331", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4350", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4360", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4382", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4515", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4615", course_list))

        math_elective_list = []
        math_elective_list.append(process_courses.find_course("MATH2101", course_list))
        math_elective_list.append(process_courses.find_course("MATH2103", course_list))
        math_elective_list.append(process_courses.find_course("MATH2043", course_list))

        open_elective_list = cis_elective_list + math_elective_list
        while elective_credit_count < 15.0:

                if has_math:
                        r = random.randint(0, len(open_elective_list) - 1)
                        elective_credit_count += int(open_elective_list[r].credits)
                        if open_elective_list[r].name == "CIS4515" and process_courses.find_course("CIS3515", elective_taken_list) == None:
                                elective_credit_count += int(process_courses.find_course("CIS3515", open_elective_list).credits)
                                elective_taken_list.append(process_courses.pop_course("CIS3515", open_elective_list))
                                r -= 1
                        if open_elective_list[r].name == "CIS4615" and process_courses.find_course("CIS3319", elective_taken_list) == None:
                                elective_credit_count += int(process_courses.find_course("CIS3319", open_elective_list).credits)
                                elective_taken_list.append(process_courses.pop_course("CIS3319", open_elective_list))
                                r -= 1
                        elective_taken_list.append(
                                process_courses.pop_course(open_elective_list.pop(r).name, course_list))

                else:
                        r = random.randint(0, len(open_elective_list) - 1)
                        elective_credit_count += int(open_elective_list[r].credits)
                        if math_elective_list.__contains__(open_elective_list[r]):
                                has_math = True
                                elective_taken_list.append(
                                        process_courses.pop_course(open_elective_list[r].name, course_list))
                                for each in math_elective_list:
                                        open_elective_list.remove(each)
                        else:
                                if open_elective_list[r].name == "CIS4515" and process_courses.find_course("CIS3515", elective_taken_list) == None:
                                        elective_credit_count += int(process_courses.find_course("CIS3515", open_elective_list).credits)
                                        elective_taken_list.append(process_courses.pop_course("CIS3515", open_elective_list))
                                        r -= 1
                                if open_elective_list[r].name == "CIS4615" and process_courses.find_course("CIS3319", elective_taken_list) == None:
                                        elective_credit_count += int(process_courses.find_course("CIS3319", open_elective_list).credits)
                                        elective_taken_list.append(process_courses.pop_course("CIS3319", open_elective_list))
                                        r -= 1
                                elective_taken_list.append(
                                        process_courses.pop_course(open_elective_list.pop(r).name, course_list))

        return elective_taken_list
