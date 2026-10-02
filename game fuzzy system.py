class GameFuzzySystem:
    @staticmethod
    def get_action(energy, proximity):
        if energy > 70 and proximity <= 70:
            return "Attack"
        elif (30 < energy <= 70 and proximity <= 30) or (
            energy <= 30 and 30 < proximity <= 70
        ):
            return "Defend"
        elif (energy <= 30 and proximity <= 30) or (
            30 < energy <= 70 and proximity > 70
        ):
            return "Run Away"
        else:
            return "No action"


def get_valid_int(prompt, low=0, high=100):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    system = GameFuzzySystem()
    energy = get_valid_int("Energy (0-100): ")
    proximity = get_valid_int("Proximity (0-100): ")
    print(system.get_action(energy, proximity))