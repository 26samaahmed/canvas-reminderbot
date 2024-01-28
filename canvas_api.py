from canvasapi import Canvas
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, date

load_dotenv()


CANVAS_API_KEY = os.getenv("CANVAS_API_KEY")
API_URL = os.getenv("API_URL")

canvas = Canvas(API_URL, CANVAS_API_KEY)


def get_assignments(course_id):
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    assignment_list = []

    for assignment in assignments:
        # If assignments have no due date, ignore so it doesn't show up as a weekly assignment
        if assignment.due_at is None:
            pass
        else:
            # Convert to YEAR/MONTH/DAY format so i can check if the assignment due date is between the 2 restrictions
            due_date = datetime.strptime(
                assignment.due_at, "%Y-%m-%dT%H:%M:%SZ").date()
            # If the assignment's due date is within the next 7 days then print it
            if date.today() + timedelta(days=1) <= due_date <= date.today() + timedelta(days=7):
                print(course.name, '->', assignment.name, 'due at', due_date)
                assignment_list.append(assignment.name)
            else:
                continue
    return assignment_list


def get_courses():
    user = canvas.get_user('user id')
    courses = user.get_courses()  # retrieve user courses
    course_list = []
    for course in courses:
        if hasattr(course, 'name'):
            if 'Spring 2024' in course.name:  # get the courses for that specific semester
              course_list.append(get_assignments(course.id))  # wip
            else:
              print(f"Course object does not have 'name' attribute: {course}")

    return course_list