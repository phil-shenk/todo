import philtasks as pt
import jsonpickle
import os

print()
files = os.listdir('tasks')
for file in files:
    file = os.path.join('tasks',file)
    if file.endswith('.json'):
        with open(file, 'r') as infile:
            text = infile.read()
            unfrozen = jsonpickle.decode(text)
            print(unfrozen)
