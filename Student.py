from process_data import process_courses
from requirements import probability, requirements_math, requirements_free_electives, requirements_geneds, \
        requirements_lab_science, requirements_cis_electives, requirements_core
import random


class Student:

        def print_completed_courses(self):
                i = 0
                n = 0
                for course in self.completed_courses:
                        i += 1
                        n += course.credits
                        print (str(i).ljust(4) + course.name + ":").ljust(15) + course.title

                print "Number of Credits: " + str(n)
                print "Number of Classes: " + str(len(self.completed_courses))


        def sum_credit_count(self, completed_courses):

                credit_count = 0
                for course in completed_courses:
                        credit_count += course.credits

                return credit_count



        def add_student_courses(self, course_list, is_honors):

                completed_courses = []
                completed_courses += requirements_core.add_core_courses(course_list, is_honors)
                completed_courses += requirements_math.add_math_courses(course_list, is_honors)
                completed_courses += requirements_cis_electives.add_cis_elective_courses(course_list, is_honors)
                completed_courses += requirements_lab_science.add_lab_science_courses(course_list, is_honors)
                completed_courses += requirements_geneds.add_geneds(course_list, is_honors)
                credit_count = self.sum_credit_count(completed_courses)
                completed_courses += requirements_free_electives.add_free_electives(completed_courses, course_list, is_honors, credit_count)

                return completed_courses


        def __init__(self):

                self.course_list = process_courses.create_courses()
                if random.random() > probability.honors:
                        self.is_honors = False
                else:
                        self.is_honors = True
                self.completed_courses = self.add_student_courses(self.course_list, self.is_honors)
                self.credit_count = self.sum_credit_count(self.completed_courses)

