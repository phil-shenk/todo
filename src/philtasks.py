
from datetime import date
from datetime import datetime

class Task:
    category = 'none'
    time = datetime.now()
    time = time.strftime("%H:%M")
    def __init__(self, name, duedate):
        self.name = name
        self.description = 'description'
        self.duedate = duedate
   
    def __str__(self):
        #make the name 24 chars for nice formatting
        return self.name[:24].ljust(24)+'  -  '+self.duedate+'  -  '+str(self.time)
    #def toJSON(self):
    #    return json.dumps(self, default=lambda o: o.__dict__, 
    #        sort_keys=True, indent=4)
    
class CourseTask(Task):
    def __init__(self, name, duedate, course):
        Task.__init__(self, name, duedate)
        self.course = course
        self.category = course
    def __str__(self):
        return (Task.__str__(self)) + '    for '+self.course
    
class ProblemSet(CourseTask):
    def __init__(self, name, duedate, course, problems={}):
        CourseTask.__init__(self, name, duedate, course)
        self.problems = problems
        
class Exam(CourseTask):
    preparedness = 0
    def __init__(self, name, duedate, course):
        CourseTask.__init__(self, name, duedate, course)
    def study():
        studying = True
        while(studying == True):
            answer = raw_input("Are you studying?")
            if (answer == 'no'):
                print('well I hope you learned')
                studying = False
            
