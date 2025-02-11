from collections import Counter
from random import *


class Game:
    def __init__(self, users):
        self.users = users
        self.user_id = 0

    def para(self, lista):
        points = 0
        powtarzajace_sie = []
        for kosc in lista:
            if 5 > lista.count(kosc) > 1 and kosc not in powtarzajace_sie:
                powtarzajace_sie.append(kosc)

        if len(powtarzajace_sie) == 1:
            points = powtarzajace_sie[0] * 2

        if len(powtarzajace_sie) == 2:
            first = powtarzajace_sie[0]
            second = powtarzajace_sie[1]

            if first > second:
                points = first * 2

            if second > first:
                points = second * 2

        return points

    def triple(self, lista):
        powtarzajace_sie = []
        points = 0
        for kosc in lista:
            if 5 > lista.count(kosc) > 2 and kosc not in powtarzajace_sie:
                powtarzajace_sie.append(kosc)
                points = powtarzajace_sie[0] * 3

        return points

    def small_street(self, lista):
        points = 0
        if all(lista.count(x) for x in [1, 2, 3, 4, 5]):
            points = 15

        return points

    def big_street(self, lista):
        points = 0
        if all(lista.count(x) for x in [2, 3, 4, 5, 6]):
            points = 20

        return points

    def kareta(self, lista):
        points = 0
        counts = Counter(lista)  # Zliczamy wystąpienia każdej liczby

        if len(counts) == 2 and (3 in counts.values() and 2 in counts.values()):
            points = 25
        return points

    def poker(self, lista):
        points = 0
        for kosc in lista:
            if lista.count(kosc) == 5:
                suma = sum(lista)
                points = 50 + suma

        return points

    def chance(self, lista):
        points = sum(lista)
        return points

    def display_status(self, user):
        print("=" * 40)
        print(f'Gracz {self.user_id + 1}: {user.name}')
        print(f'Ilość punktów: {user.points}')
        print("=" * 40)

    def generate(self, list):
        list.clear()
        for i in range(5):
            list.append(randrange(1, 6))

        return list

    def generate_for_roll(self, list, rolls):
        for i in range(rolls):
            list.append(randrange(1, 6))

    def change(self):
        """Variables for rules"""
        amount_of_para = 0
        amount_of_kareta = 0
        amount_of_triple = 0
        amount_of_small_street = 0
        amount_of_big_street = 0
        amount_of_poker = 0
        amount_of_chance = 0

        """category variables for UI"""
        used_para = ""
        used_kareta = ""
        used_triple = ""
        used_small_street = ""
        used_big_street = ""
        used_poker = ""
        used_chance = ""

        while True:
            current_user = self.users[self.user_id]
            list = []
            self.generate(list)
            self.display_status(current_user)
            print(f'Twoje rzuty to {list}')

            for i in range(2):
                decision = input(f'Czy rzucić jeszcze raz kośćmi? (tak/nie): ')

                if decision.lower() == "tak":
                    throw_list = ""
                    throw_list = input("wybierz którymi kośćmi: (numer kości/wszystkie): ")

                    # if throw_list != "wszystkie" and not isinstance(throw_list, tuple):
                    #     print("Wpisałeś źle straciłeś ruch :(")
                    #     continue

                    if throw_list.lower() == "wszystkie":
                        list = []
                        self.generate(list)
                        print(list)
                    else:

                        transformed = [int(x) for x in throw_list.split(',')]
                        transformed_list = sorted(transformed)
                        for idx in transformed_list:
                            list[idx - 1] = randrange(1, 6)
                        print(f"Twoje nowe rzuty{list}")
                else:
                    break

                if decision.lower() == "nie":
                    break

            print(
                f"Do czego chcesz to zapisać?\n para         {used_para}\n trójka       {used_triple}\n mały street  {used_small_street}\n "
                f"duży street  {used_big_street}\n kareta      {used_kareta}\n poker       {used_poker} \n szansa      {used_chance}")
            category = input()
            # if selected categories
            # sownik jeżeli damy sobie 1,2 para i napiszemy jezeli in dict id ma wartość a w innych nieparzystych nie ma wartości to nie można wybrać

            kolumn_dict ={
                1: "", #para
                2: "", # para
                3: "", # 3
                4: "", # 3
                5: "", # kareta
                6: "", # kareta
                7: "", # ms
                8: "", # ms
                9: "", # ds
                10: "", # ds
                11: "", # p
                12: "", # p
                13: "", # s
                14: "", # s
            }
            selected_categories_column1 = 0
            selected_categories_column2 = 0

            while True:
                """Option to choose"""
                points = 0

                # Sprawdzanie poprawności kategorii
                if category not in ["para", "kareta", "trójka", "trojka", "mały street", "maly street", "duży street",
                                    "duzy street", "poker", "szansa"]:
                    print("Błędna kategoria! Wybierz jedną z dostępnych kategorii.")
                    category = input("Wybierz kategorię: ")
                    continue

                if category == "para" and amount_of_para < 3:
                    # Odblokowanie kolumny 1
                    kolumn_dict[1] = "x"

                    # Sprawdzenie, czy kolumna 2 jest odblokowana
                    no_empty = [v for k, v in kolumn_dict.items() if k % 2 == 0 and v != ""]
                    if len(no_empty) >= 2:
                        print("Musisz odblokować kolumnę 2 zanim zaczniesz z niej korzystać")
                        break
                    else:
                        # Dodanie punktów tylko raz
                        points += self.para(list)
                        used_para += "|"
                        amount_of_para += 1
                        selected_categories_column1 += 1


                    if selected_categories_column1 < 1:
                        print("nie masz dostępu do drugiej kolumny")
                        continue

                    break
                elif category in ["kareta"] and amount_of_kareta < 3:
                    points += self.kareta(list)
                    used_kareta += "|"
                    amount_of_kareta += 1
                    break
                elif category in ["trójka", "trojka"] and amount_of_triple < 3:
                    points += self.triple(list)
                    used_triple += "|"
                    amount_of_triple += 1
                    break
                elif category in ["mały street", "maly street"] and amount_of_small_street < 3:
                    points += self.small_street(list)
                    used_small_street += "|"
                    amount_of_small_street += 1
                    break
                elif category in ["duży street", "duzy street"] and amount_of_big_street < 3:
                    points += self.big_street(list)
                    used_big_street += "|"
                    amount_of_big_street += 1
                    break
                elif category == "poker" and amount_of_poker < 3:
                    points += self.poker(list)
                    used_poker += "|"
                    amount_of_poker += 1
                    break
                elif category == "szansa" and amount_of_chance < 3:
                    points += self.chance(list)
                    used_chance += "|"
                    amount_of_chance += 1
                    break
                else:
                    print("Ta kategoria osiągnęła limit 3. Wybierz inną kategorię.")
                    category = input("Wybierz kategorię ponownie: ")

            current_user.add_points(points)
            print(f"Punkty za wybraną kategorię ({category}): {points}")
            print(f"Łączne punkty gracza {current_user.name}: {current_user.points}")

            self.user_id = (self.user_id + 1) % len(self.users)

            # Zapytaj użytkownika, czy chce grać dalej
            continue_game = input("Czy chcesz zagrać kolejną rundę? (tak/nie): ").lower()
            if continue_game != "tak":
                print("Dziękujemy za grę!")
                for user in self.users:
                    print(f'Gracz {user.name} zdobył {user.points}')
                break


class User:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

def initialize_game():
    """Inicjalizuję grę i rozpoczyna rozgrywkę."""
    player_amount = int(input("🎮 Wpisz ilość graczy: "))
    user_list = [User(input(f"👤 Podaj imię gracza {i + 1}: ")) for i in range(player_amount)]

    game = Game(user_list)
    game.change()


if __name__ == "__main__":
    initialize_game()
