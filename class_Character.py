import csv
from tabulate import tabulate
from colorama import Fore, Back, Style
from pyfiglet import figlet_format


def start_the_game():
    print("Welcome to...")
    print(figlet_format("Heroes' War", font="standard"))
    with open('description.txt', 'r') as data_file:
        data_list = data_file.read().splitlines()
        for i in data_list:
            print(i)


class Character:

    def __init__(self):
        player_name = input("What is your name? ")
        self.player = player_name
        print(f"{self.player}, please choose your characters")
        self.__mage = self.choose_character('Mage', 'mage_character.csv')
        self.__jungle = self.choose_character('Jungle', 'jungle_character.csv')
        self.__fighter = self.choose_character('Fighter', 'fighter_character.csv')
        self.__carrie = self.choose_character('Carrie', 'carrie_character.csv')
        self.__tank = self.choose_character('Tank', 'tank_character.csv')
        self.character_dict = {}
        self.update_character_dict()

    def choose_character(self, position, file):
        print("❁❃❀⚘✿᯽❈❁❃❀⚘✿᯽❈❁❃❀⚘✿᯽❈❁❃❀⚘✿᯽❈❁❃❀⚘✿᯽❈❁❃❀⚘✿᯽❈❁❃❀⚘✿᯽❈")
        with open(file, 'r') as cha_folder:
            data_list = csv.reader(cha_folder)
            col_name = ['Name', 'Strength', 'Attack Damage', 'Position Attack']
            next(data_list)
            cha_list = [x for x in data_list]
            print(f"These are available {position} characters")
            print(tabulate(cha_list, headers=col_name))
            chosen_cha = input(f"Choose your {position} character: ")
            cha_name = [cha_list[x][0] for x in range(len(cha_list))]
            while chosen_cha not in cha_name:
                print(Fore.RED + "Your character is not available! Please choose again")
                print(Style.RESET_ALL)
                chosen_cha = input(f"Choose your {position} character: ")
            print(f"{chosen_cha} is on your side!!")
            for i in cha_list:
                if i[0].lower() == chosen_cha.lower():
                    return [i[0], int(i[1]), int(i[2]), i[3]]

    def update_character_dict(self):
        self.character_dict['Mage'] = self.__mage
        self.character_dict['Jungle'] = self.__jungle
        self.character_dict['Fighter'] = self.__fighter
        self.character_dict['Carrie'] = self.__carrie
        self.character_dict['Tank'] = self.__tank


class Item:
    with open('medicine.csv', 'r') as data_file:
        medicine_file = csv.reader(data_file)
        medicine_list = [x for x in medicine_file]
    with open('weapons.csv', 'r') as data_file:
        weapons_file = csv.reader(data_file)
        weapons_list = [x for x in weapons_file]

    def __init__(self, character, coin=500):
        self.coin = coin
        self.items = {'Medicine': [], 'Weapons': []}
        self.character = character
        if self.check_treasury():
            self.welcome_player_to_shop()
        else:
            print("You've reached the limit of items that can be bought")

    def welcome_player_to_shop(self):
        with open('shop_description.txt') as welcome_file:
            [print(line.strip()) for line in welcome_file.readlines()]
        print(f"Your balance is {self.coin}")

        choice = input("What do you want to buy (medicine/weapons) or 'no' to quit ")
        if choice.lower() == 'medicine':
            self.medicine()
        if choice.lower() == 'weapons':
            self.weapons()
        if choice.lower() == 'no':
            pass

    def medicine(self):
        with open('medicine.csv', 'r') as data_file:
            medicine_list = csv.reader(data_file)
            print('These are items for healing')
            col_name = ['Name', 'Healing Point', 'Attack Damage', 'Position', 'Price']
            next(medicine_list)
            med_list = [x for x in medicine_list]
            print(tabulate(med_list, headers=col_name))
        med_input = input("Buy your medicine:")
        self.update_strength(med_input)
        for i in med_list:
            if i[0] == med_input:
                self.items['Medicine'].append(i)
        if self.update_balance('medicine.csv', med_input) is False:
            pass

    def weapons(self):
        with open('weapons.csv', 'r') as data_file:
            weapons_list = csv.reader(data_file)
            print('These are items for healing')
            col_name = ['Name', 'Healing Point', 'Attack Damage', 'Position', 'Price']
            next(weapons_list)
            data_list = [x for x in weapons_list]
            print(tabulate(data_list, headers=col_name))
        weapon_input = input("Buy your medicine:")
        self.update_damage(weapon_input)
        for i in data_list:
            if i[0] == weapon_input:
                self.items['Weapons'].append(i)
        self.update_balance('weapons.csv', weapon_input)

    def check_treasury(self):
        num = 0
        for items_list in self.items.values():
            num += len(items_list)
        return num <= 3

    def update_balance(self, file, item_input):
        with open(file, 'r') as data:
            data_items = csv.reader(data)
            next(data_items)
            items_list = [x for x in data_items]
        for i in items_list:
            if item_input == i[0]:
                if self.coin < int(i[4]):
                    print("You don't have enough money.")
                    return False
                self.coin -= int(i[4])
        print(f"This is your balance: {self.coin}")

    def update_strength(self, item_name):
        for i in self.medicine_list:
            if item_name == i[0]:
                item_list = i
                if item_list[3] == 'All':
                    for value in self.character.values():
                        value[1] += int(item_list[1])
                elif item_name == item_list[0]:
                    self.character[i[3]][1] += int(item_list[1])

    def update_damage(self, item_name):
        for i in self.weapons_list:
            if item_name == i[0]:
                item_list = i
                if item_list[3] == 'All':
                    for value in self.character.values():
                        value[2] += int(item_list[2])
                elif item_name == item_list[0]:
                    self.character[i[3]][2] += int(item_list[2])


start_the_game()


class Fight:
    def __init__(self, player_1=Character(), player_2=Character()):
        self.character_list = [player_1, player_2]  # player1 and player2 are objects from class Character
        while self.check_who_wins() == 'GO':
            self.choose_hero_to_attack(self.character_list[0].character_dict
                                       , self.character_list[1].character_dict, self.character_list[0].player)
            self.choose_hero_to_attack(self.character_list[1].character_dict
                                       , self.character_list[0].character_dict, self.character_list[1].player)
        if self.check_who_wins() != 'GO':
            lose_player = self.check_who_wins()
            if lose_player == 'player_2':
                print(figlet_format(f'{self.character_list[0].player} wins', font='standard'))
            elif lose_player == 'player_1':
                print(figlet_format(f'{self.character_list[1].player} wins', font='standard'))

    def choose_the_hero_to_fight(self, player, name):
        print(f"{name} please choose 3 characters to perform a fight")
        self.display_result()
        hero_dict = {}
        n = 1
        while n < 4:
            hero = input(f"Hero #{n} ")
            for position, value in player.items():
                if hero == value[0]:
                    hero_dict[position] = value
            n += 1
        items = Item(player)
        return hero_dict, items

    def choose_hero_to_attack(self, player_dict, player_2, player_name):
        player_1, item_dict = self.choose_the_hero_to_fight(player_dict, player_name)
        player_1_copy = player_1.copy()
        for position, value in player_1_copy.items():
            if position == 'Mage':
                for j in player_2:
                    player_2[j][1] -= value[2]
                player_1.pop(position)
            elif position == 'Jungle':
                attacked_position = input("Choose 1 opponent's position to attack: ")
                player_2[attacked_position][1] -= int(value[2])
                player_1.pop(position)
            elif position == 'Fighter':
                attacked_list = []
                n = 1
                while n < 4:
                    attacked_position = input(f"Choose #{n} opponent's position to attack: ")
                    attacked_list.append(attacked_position)
                    n += 1
                for i in attacked_list:
                    player_2[i][1] -= value[2]
                player_1.pop(position)
            elif position == 'Carrie':
                attacked_list = []
                n = 1
                while n < 3:
                    attacked_position = input(f"Choose #{n} opponent's position to attack: ")
                    attacked_list.append(attacked_position)
                    n += 1
                for i in attacked_list:
                    player_2[i][1] -= value[2]
                player_1.pop(position)
            elif position == 'Tank':
                for j in player_2:
                    player_2[j][1] -= value[2]
                player_1.pop(position)
        self.check_character()
        if self.check_who_wins() == 'GO':
            pass
        elif self.check_who_wins() == 'player1':
            print(f"Congratulations! {self.character_list[1].player} WINS.")
        elif self.check_who_wins() == 'player2':
            print(f"Congratulations! {self.character_list[0].player} WINS.")

    def display_result(self):
        table_1 = tabulate(self.character_list[0].character_dict, headers='keys', tablefmt='fancy_grid')
        table_2 = tabulate(self.character_list[1].character_dict, headers='keys', tablefmt='fancy_grid')
        print(f"This is the player on {self.character_list[0].player}'s team and their strength")
        print(table_1)
        print(f"This is the player on {self.character_list[1].player}'s team and their strength")
        print(table_2)
        with open('character_1.txt', 'w') as data:
            data.write(table_1)
        with open('character_2.txt', 'w') as data:
            data.write(table_2)

    def check_character(self):
        for position, name in self.character_list[0].character_dict.items():
            if name[1] <= 0:
                self.character_list[0].character_dict.pop(position)
                break
        for position, name in self.character_list[1].character_dict.items():
            if name[1] <= 0:
                self.character_list[0].character_dict.pop(position)
                break

    def check_who_wins(self):
        strength_sum_1 = sum([x[1] for x in self.character_list[0].character_dict.values()])
        strength_sum_2 = sum([x[1] for x in self.character_list[1].character_dict.values()])
        if strength_sum_2 > 0 and strength_sum_1 > 0:
            return 'GO'
        elif strength_sum_2 <= 0:
            return 'player_2'
        elif strength_sum_1 <= 0:
            return 'player_1'


fight = Fight()
