import copy, csv, random, time
from Student import Student
from Semester import Semester
from process_data import process_courses, process_prerequisites


def add_lab(student, semester_credit_count, lab_name):
        if process_courses.find_course(lab_name, student.completed_courses) != None:
                semester_credit_count += process_courses.find_course(lab_name,
                                                                     student.completed_courses).credits
                classes_taken.append(process_courses.pop_course(lab_name, student.completed_courses))

for n in range(0, 10000):
        transcript_list = []

        for i in range(0, 100):

                t0 = time.clock()
                student = Student()

                completed_courses = copy.copy(student.completed_courses)
                classes_taken = []
                classes_taken.append("MATH1022")
                classes_taken.append("MATH1039")
                classes_taken.append("MATH0701")
                classes_taken.append("MATH1031")
                semester_list = []
                while len(student.completed_courses) > 0:
                        semester = Semester()
                        while semester.credit_count < 16 and len(semester.courses) < 5 and (len(student.completed_courses)) > 0:
                                r = random.randint(0, len(student.completed_courses) - 1)
                                if process_prerequisites.are_prereqs_satisfied(classes_taken, student.completed_courses[r].prereqs):
                                        classes_taken.append(student.completed_courses[r].name)
                                        semester.courses.append(student.completed_courses.pop(r))
                                else:
                                        if time.clock() - t0 > 3.0:
                                                print "Remaining Courses: "
                                                for course in student.completed_courses:
                                                        print "   " + course.name + "  " + str(course.prereqs)
                                                print
                                                print "Taken Courses: "
                                                for course in classes_taken:
                                                        print "   " + course
                                                exit()
                        semester_list.append(semester)
                        print "    " + str(len(student.completed_courses))

                        transcript_semester = []
                for semester in semester_list:
                        courses = []
                        for course in semester.courses:
                                courses.append(copy.copy(course.name))
                        transcript_semester.append(courses)
                        print courses
                print len(semester_list)
                print i
                transcript_list.append(transcript_semester)

        print "..................................."

        for transcript in transcript_list:
                print
                for semester in transcript:
                        print semester

        with open('transcripts.csv', 'ab') as csvfile:
                writer = csv.writer(csvfile)
                for transcript in transcript_list:
                        i = 1
                        row = []
                        for semester in transcript:
                                row.append(i)
                                for course in semester:
                                        row.append(course)
                                i += 1
                        print row
                        writer.writerow(row)




