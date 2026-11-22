# Periodic Table Informaton Finder
from pyscript import display, document


def find_element(e):
    document.getElementById('result').innerHTML = ' '
    element_input = document.getElementById('nonmetal').value.capitalize().strip()

    #in order: symbol, element, atomic number, atomic mass
    elements = {
        'H' : ['H', 'Hydrogen', '1', '1.008'],
        'C' : ['C', 'Carbon', '6', '12.01'],
        'N' : ['N', 'Nitrogen', '7', '14.01'],
        'O' : ['O', 'Oxygen', '8', '16'],
        'F' : ['F', 'Fluorine', '9', '19'],
        'Ne': ['Ne', 'Neon', '10', '20.18'],
        'P' : ['P', 'Phosphorus', '15', '30.97'],
        'S' : ['S', 'Sulfur', '16', '32.07'],
        'Cl' : ['Cl', 'Chlorine', '17', '35.45'],
        'Ar' : ['Ar', 'Argon', '18', '39.95'],
        'Se' : ['Se', 'Selenium', '34', '78.96'],
        'Br' : ['Br', 'Bromine', '35', '79.90'],
        'Kr' : ['Kr', 'Krypton', '36', '83.80'],
        'I' : ['I', 'Iodine', '53', '126.9'],
        'Xe' : ['Xe', 'Xenon', '54', '131.3'],
        'Rn' : ['Rn', 'Radon', '84', '222']
    }


    represent = elements.get(element_input, f'Cannot find {element_input}')
    display(represent, target = 'result')
