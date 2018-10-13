import philtasks as pt
import jsonpickle
import os
        
tasks = []

tasks.append(pt.CourseTask('441 Reference material','10/16', "CS 441"))
tasks.append(pt.CourseTask('MORSE COOODE project', '10/21', "CS 447"))
problems = {'2.1':['2', '4a', '10cde', '16', '28', '34b', '42a'],
            '2.2':['14','12','20a','30a'],
            '2.3':['2c', '4ab', '6b', '8gh', '16c', '22b', '30b'],
            '2.4':['2d', '4d', '6d','8', '10c', '14d', '16b', '18d', '32a']
            }
hw5 = pt.ProblemSet('diffeq hw 5', '10/24', 'MATH 290', problems)
tasks.append(hw5)

cs441midterm = pt.Exam('441 Midterm', '10/18', 'CS 441')
tasks.append(cs441midterm)




#write files
for task in tasks:
    with open(task.name+'.json', 'w') as outfile:
        #json.dump(task.toJSON(), outfile)
        frozen = jsonpickle.encode(task)
        outfile.write(frozen)
    frozen = jsonpickle.encode(task)
