from canvasapi import Canvas
import os
from dotenv import load_dotenv
import datetime

load_dotenv()


CANVAS_API_KEY = os.getenv("CANVAS_API_KEY")
API_URL = os.getenv("API_URL")

canvas = Canvas(API_URL, CANVAS_API_KEY)


def get_assignments():
  start_time = datetime.date(2023, 8, 23)
  end_time = datetime.date(2023, 9, 30)
  delta = datetime.timedelta(days=1)
  course = canvas.get_course(3395962)
  assignments = course.get_assignments()

  for assignment in assignments:
  # If assignments have no due date, ignore so it doesn't show up as a weekly assignment
    if assignment.due_at is None:
      pass
    else:
    # Convert to YEAR/MONTH/DAY format so i can check if the assignment due date is between the 2 restrictions
      convert_due_date = datetime.datetime.strptime(assignment.due_at, "%Y-%m-%dT%H:%M:%SZ")
      formatted_due_date = convert_due_date.strftime("%Y-%m-%d")
      print(formatted_due_date , assignment)


get_assignments()
# TODO: Access all my courses and get the assignments per week/day



# future implementations: 
  # have a slash command like !grades and the bot would send the current grades for all classes
  # have a slash command like !done1 if I finished an assignment and want to cross it out of the list
  # have a slash command like !quizzes to remind the person with the quizzes due that week