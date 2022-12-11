# Heroes-War
- Project Title
  Heroes' War
- Project overview and features
  This project is a 2-player game, it opens with letting each player chooses the characters on their team, each team
  has 5 positions; Mage, Carrie, Jungle, Fighter and Tank and each position has a unique abilities i.e. Mage can
  damage every character on the other team.
  After choosing characters, the program will ask the player whether they want to shop for some items (medicine:
  increases strength, weapons: decreases other team's strength) or not.
  Then, the fight begins by letting each player choose 3 characters to perform a fight, and if 
  one of the characters the player picks can attack 3 characters, the program will ask which position the player wants
  to attack (you can choose the same position in 1 round). If overall strength of each team is not 0, the game will
  continue and will end when there's a team that has 0 overall strength.
- Required libraries and tools (e.g., specific version of Python, etc)
  - Python 3.10.8
  - module pyfiglet to decorate the program
  - module tabulate to make the display easier to read
- Program design -- what are your classes are and what are their objectives
  - class Character: This class lets each player chooses their characters on their team
  - class Item: This class is a shop for medicine and weapons
  - class Fight: This is the class the implement the program
- Code structure -- how many source files and what each of them contains
  - description.txt: a text file that explains the user how the game works
  - mage_character.csv: a csv file that stores the information of available mage characters
  - carrie_character.csv: a csv file that stores the information of available carrie characters
  - jungle_character.csv: a csv file that stores the information of available jungle characters
  - fighter_character.csv: a csv file that stores the information of available fighter characters
  - tank_characters.csv: a csv file that stores the information of available tank characters
  - weapons.csv: a csv file that stores the information of weapon items
  - medicine.csv: a csv file that stores the information of medicine items
