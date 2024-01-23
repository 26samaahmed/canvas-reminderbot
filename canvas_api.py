from canvasapi import Canvas
import os
from dotenv import load_dotenv
import datetime

load_dotenv()


CANVAS_API_KEY = os.getenv("CANVAS_API_KEY")
API_URL = os.getenv("API_URL")

canvas = Canvas(API_URL, CANVAS_API_KEY)


def get_assignments(course_id):
  # Dates are for testing purposes. Change eventually to display assignments for today only using data.today() == assignment.due_date
  start_time = datetime.date(2024, 1, 23)
  end_time = datetime.date(2024, 1, 30)
  course = canvas.get_course(course_id)
  assignments = course.get_assignments()

  for assignment in assignments:
  # If assignments have no due date, ignore so it doesn't show up as a weekly assignment
    if assignment.due_at is None:
      pass
    else:
    # Convert to YEAR/MONTH/DAY format so i can check if the assignment due date is between the 2 restrictions
      due_date = datetime.datetime.strptime(assignment.due_at, "%Y-%m-%dT%H:%M:%SZ").date()
      if start_time <= due_date <= end_time:
        print(due_date , assignment)
      '''
      if assigment.due_date == date.today():
        print(assignment)
      else:
        print("No assignments due today for {course}")
      '''



# get_assignments("user code")

# Create a function that retrieves all the user's current_courses.
# Call the get_assignment function, passing the course's id in it, Assignments will then be printed for each cpurse
#def get_courses():
user = canvas.get_user("user_id")
print(user)
courses = user.get_courses() # WIP
for course in courses:
  if hasattr(course, 'name'):
    if 'Spring 2024' in course.name:
      print(course.name)
 # else:
    #print(f"Course object does not have 'name' attribute: {course}")



#get_courses()


# future implementations: 
  # have a slash command like !grades and the bot would send the current grades for all classes
  # have a slash command like !done1 if I finished an assignment and want to cross it out of the list
  # have a slash command like !quizzes to remind the person with the quizzes due that week
