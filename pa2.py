# Set Operators
from pyscript import display, document

def add_member(e):
    grade7 = {'Chesca Irinco', 'Johanna Guarin', 'Joaquin Conde'}
    grade8 = {'Yeshua Simon','Castor Ong', 'Beau Palic'}
    grade9 = {'Bruce Cuenca', 'Chelsea Coronado', 'Shaun Cortes'}
    grade10 = {'Cedric Visorde', 'Samantha Jose', 'Niqa Agasi'}
    first_name = document.getElementById('firstname').value.title().strip() # input 1
    last_name = document.getElementById('lastname').value.title().strip() # input 2
    full_name = first_name + ' ' + last_name # concatenation
    full_list = {'Chesca Irinco', 'Johanna Guarin', 'Joaquin Conde','Yeshua Simon','Castor Ong', 'Beau Palic','Bruce Cuenca', 'Chelsea Coronado', 'Shaun Cortes', 'Cedric Visorde', 'Samantha Jose', 'Niqa Agasi' }
    full_list.add(full_name)

    display(full_list, target = 'results') # union for all members to be displayed
    display(f'Total number of members: {len(full_list)}', target = 'results') # length


