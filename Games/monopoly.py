import random
from dicts.mapa_data_beginning import map_data


class Player:
    """
        Klasa reprezentująca gracza w grze.

        Atrybuty:
            name (str): Nazwa gracza.
            money (int): Ilość pieniędzy gracza.
            mansion (dict): Nieruchomości posiadane przez gracza.
            position (int): Aktualna pozycja gracza na mapie.
    """
    def __init__(self, name):
        self.name = name
        self.money = 400000
        self.mansion = {}
        self.position = 101  # Początkowa pozycja gracza Granada

    def move_player(self):
        """Przesuwa gracza o wynik rzutu kostką (1-6)."""
        dice_roll = random.randint(1, 6)  # Standardowy rzut kostką
        print(f"\n🎲 Rzut kostką: {dice_roll}")

        # Obliczanie nowej pozycji
        position_to_str = str(self.position)
        first_of_two_id = int(position_to_str[:2]) * 10
        thousandth = self.position - first_of_two_id + dice_roll

        if 0 < thousandth <= 3:
            self.position += 0
        elif 3 < thousandth <= 6:
            if self.position + 100 > 400:
                self.position = 100 + (self.position + 100 - 400)
                self.money += 300000
            else:
                self.position += 100
        elif 6 < thousandth <= 9:
            if self.position + 200 > 400:
                self.position = 100 + (self.position + 200 - 400)
                self.money += 300000
            else:
                self.position += 200

        position_to_str = str(self.position)
        third_id = int(position_to_str[2])

        modulo_thousandth = thousandth % 3
        if modulo_thousandth == 0:
            modulo_thousandth = 3
        self.position = self.position - third_id + modulo_thousandth

        return self.position

    def show_mansion(self):
        """Wyświela posiadłości użytkownika"""
        if self.mansion:
            print("\nPosiadłości gracza:")
            for city, level in self.mansion.items():
                print(f"  - {city}: Poziom {level}")
        else:
            print("Brak posiadłości.")

    # Player can buy a mansion and upgrade it
    def buy_mansion(self, city_name, prices):
        """Pozwala graczowi na zakup lub ulepszenie nieruchomości w danym mieście."""
        if city_name not in self.mansion:
            # Jeśli gracz nie ma jeszcze nieruchomości w tym mieście
            cost = prices['buy'][1]  # Pierwszy poziom
            if self.money >= cost:
                self.money -= cost
                self.mansion[city_name] = 1  # Kupuje pierwszy poziom
                print(f"\n🏠 Kupiłeś nieruchomość w {city_name} za 💵 {cost}$.")
                print(f"💰 Twoje saldo wynosi teraz: {self.money}$")
                self.show_mansion()
            else:
                print("❌ Nie masz wystarczająco pieniędzy na zakup.")
        else:
            current_level = self.mansion[city_name]
            if current_level < max(prices['buy'].keys()):  # Sprawdzenie, czy można ulepszyć
                next_level = current_level + 1
                if next_level == 6:
                    print("🔝 Twoja nieruchomość jest już na najwyższym poziomie.")
                    return

                upgrade_cost = prices['buy'][next_level]
                if self.money >= upgrade_cost:
                    self.money -= upgrade_cost
                    self.mansion[city_name] = next_level  # Ulepszamy poziom nieruchomości
                    print(f"🔼 Ulepszyłeś nieruchomość w {city_name} do poziomu {next_level} za 💵 {upgrade_cost} $.")
                    print(self.mansion)
                else:
                    print("❌ Nie masz wystarczająco pieniędzy na ulepszenie.")



    def repurchase_mansion(self, city_name, prices, current_mansion_level, owner):
        """Pozwala graczowi na odkupienie nieruchomości."""
        protection_money = prices['repurchase'][current_mansion_level]  # Pierwszy poziom
        if self.money >= protection_money:
            del owner.mansion[city_name]
            owner.money += protection_money

            self.money -= protection_money
            self.mansion[city_name] = 1  # Kupuje pierwszy poziom

            print(f"\n🏠 Odkupiłeś nieruchomość w {city_name} za 💵 {protection_money}$.")
            print(f"💰 Twoje saldo wynosi teraz: {self.money}$")
            print(self.mansion)

        else:
            print("❌ Nie masz wystarczająco pieniędzy na ulepszenie.")


    def show_money(self):
        """Wyświetla aktualne saldo uzytkownika"""
        print(f'💰 Twoje Saldo: {self.money} $')






class MapGenerator:
    """Klasa generująca mapę i zarządzająca pozycjami gracza."""
    def __init__(self, player_instance):
        self.player = player_instance

    def generate_map_positions(self):
        """Tworzy i zwraca mapę z pozycjami miast i ich cenami."""
        positions = {}
        for country_id, country_data in map_data.items():
            country_name = country_data["name"]
            for city_id, city_data in country_data["cities"].items():
                position_id = country_id * 100 + city_id
                positions[position_id] = {
                    "country": country_name,
                    "city": city_data["name"],
                    "prices": city_data["prices"],
                }
        return positions

    def generate_position_mansion(self):
        pass

    def show_player_position(self):
        """Wyświetla aktualną pozycję gracza na mapie."""
        current_position = self.player.position  # Pobranie aktualnej pozycji gracza
        positions = self.generate_map_positions()
        if current_position in positions:
            print(
                f"📍 Znajdujesz się po rzucie kostką w: {positions[current_position]['city']} ({positions[current_position]['country']}){positions[current_position]["prices"]}" )
        else:
            print("❌ Lokalizacja nieznana")


class Game:
    """
        Klasa reprezentująca główną logikę gry.

        Atrybuty
        users (list): Lista obiektów klasy Player reprezentujących graczy.
        user_id (int): Indeks aktualnego gracza w liście users.
    """

    def __init__(self, users):
        self.users = users
        self.user_id = 0

    def play(self):
        """Rozpoczyna grę"""
        print(f"\n🔄 Grę rozpoczyna: 👤 {self.users[0].name}")
        while True:

            current_user = self.users[self.user_id]
            map_gen = MapGenerator(current_user)

            current_user.move_player()  # Przesuwa gracza na podstawie rzutu kostką
            map_gen.show_player_position()  # Wyświetla aktualną pozycję gracza na mapie

            current_position = current_user.position  # Pobiera aktualną pozycję gracza
            positions = map_gen.generate_map_positions()  # Generuje słownik z dostępnymi pozycjami na mapie


            """----------------------------------Logika wynajm posiadłości----------------------------------------------"""
            if current_position in positions:
                city_name = positions[current_position]['city']
                prices = positions[current_position]['prices']

                owner = None
                for player in self.users:
                    if city_name in player.mansion:
                        owner = player


                if owner and owner != current_user:
                    current_mansion_level = owner.mansion[city_name]
                    if current_mansion_level in prices['rent']:
                        rent_cost = prices['rent'][current_mansion_level]
                        print(f"🚨 Stanąłeś na posesje gracza {owner.name} płacisz mu czynsz 💵 {rent_cost}")
                        current_user.money -= rent_cost
                        owner.money += rent_cost


                        current_user.show_money()

                        """----------------------------------Logika odkupienia posiadłości----------------------------------------------"""
                        decision = input(f"Czy chcesz odkupić posiadłość za 💵 {prices['repurchase'][current_mansion_level]} (tak/nie): ").strip().lower()
                        if decision != 'tak':
                            self.user_id = (self.user_id + 1) % len(self.users)
                            print(f"\n🔄 Zamiana gracza na: 👤 {self.users[self.user_id].name}")
                            continue
                        else:
                            current_user.repurchase_mansion(city_name, prices, current_mansion_level, owner)
                            self.user_id = (self.user_id + 1) % len(self.users)
                            print(f"\n🔄 Zamiana gracza na: 👤 {self.users[self.user_id].name}")
                            continue

            current_user.show_money()
            """----------------------------------Logika zakupu posiadłości----------------------------------------------"""
            if current_position in positions:
                city_name = positions[current_position]['city']
                prices = positions[current_position]["prices"]

                if city_name not in current_user.mansion:
                    choice = input(
                        f"🏠 Możesz kupić nieruchomość w {city_name} za 💵 {prices['buy'][1]}$. Chcesz kupić? (tak/nie): ").strip().lower()
                    if choice == "tak":
                        current_user.buy_mansion(city_name, prices)
                        current_user.show_money()
                else:
                    current_level = current_user.mansion[city_name]
                    next_level = current_level + 1

                    if next_level in prices['buy']:
                        upgrade_cost = prices['buy'][next_level]
                        choice = input(
                            f"🔼 Masz już nieruchomość w {city_name}. Chcesz ją ulepszyć do poziomu {next_level} za 💵 {upgrade_cost}$? (tak/nie): ").strip().lower()

                        if choice == "tak":
                            current_user.buy_mansion(city_name, prices)

            self.user_id = (self.user_id + 1) % len(self.users)
            print(f"\n🔄 Zamiana gracza na: 👤 {self.users[self.user_id].name}")


def initialize_game():
    """Inicjalizuję grę i rozpoczyna rozgrywkę."""
    player_amount = int(input("🎮 Wpisz ilość graczy: "))
    user_list = [Player(input(f"👤 Podaj imię gracza {i + 1}: ")) for i in range(player_amount)]

    game = Game(user_list)
    game.play()


if __name__ == "__main__":
    initialize_game()
