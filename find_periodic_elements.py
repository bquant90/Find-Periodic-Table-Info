# This program finds information for any periodic table element between the atomic numbers of 1 - 10.
import sys
ELEMENTS = {
    1: {"name": "Hydrogen", "symbol": "H", "mass": 1.0079, "type": "Nonmetal", "number": 1},
    2: {"name": "Helium", "symbol": "He", "mass": 4.0026, "type": "Nonmetal", "number": 2},
    3: {"name": "Lithium", "symbol": "Li", "mass": 7, "type": "Metal", "number": 3},
    4: {"name": "Beryllium", "symbol": "Be", "mass": 9.012183, "type": "Metal", "number": 4},
    5: {"name": "Boron", "symbol": "B", "mass": 10.81, "type": "Metalloid", "number": 5},
    6: {"name": "Carbon", "symbol": "C", "mass": 12.011, "type": "Nonmetal", "number": 6},
    7: {"name": "Nitrogen", "symbol": "N", "mass": 14.007, "type": "Nonmetal", "number": 7},
    8: {"name": "Oxygen", "symbol": "O", "mass": 15.999, "type": "Nonmetal", "number": 8},
    9: {"name": "Fluorine", "symbol": "F", "mass": 18.9984, "type": "Nonmetal", "number": 9},
    10: {"name": "Neon", "symbol": "Ne", "mass": 20.180, "type": "Nonmetal", "number": 10},
}

def main():
    while (True):
    # Get the atomic number from the user.
        try:
            num = int(input("Enter an atomic number between 1 and 10 (Zero to quit): "))
            if (num == 0):
                break
            elif num in ELEMENTS:
                info(num)
            else:
                print("That is an invalid number. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            
def info(num):
    #Print output to screen.
    selected_element = ELEMENTS[num]
    print(f"Element: {selected_element['name']}")
    print(f"Symbol: {selected_element['symbol']}") 
    print(f"Atomic Mass: {selected_element['mass']}") 
    print(f"Classification: {selected_element['type']}") 
    print(f"Atomic Number: {selected_element['number']}\n")   

try:
    main()
finally:
    # Close the input stream
    sys.stdin.close()
