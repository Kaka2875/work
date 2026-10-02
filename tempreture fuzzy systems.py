class FuzzySystem:
    def fuzzify(self, temperature):
        if temperature <= 10:
            return "very_cold"
        elif temperature <= 20:
            return "cold"
        elif temperature <= 30:
            return "warm"
        elif temperature <= 40:
            return "hot"
        else:
            return "very_hot"

    def infer(self, category):
        if category in ("very_cold", "cold"):
            return "heater_on"
        elif category in ("hot", "very_hot"):
            return "fan_on"
        else:
            return "off"

    def evaluate(self, temperature):
        category = self.fuzzify(temperature)
        return self.infer(category)


def get_temperature(default=25.0):
    try:
        user_input = input("Enter temperature: ").strip()
        if user_input == "":
            return default
        return float(user_input)
    except EOFError:
        print("No temperature entered. Using default temperature of 25.0°C.")
        return default
    except ValueError:
        print("Invalid temperature. Using default temperature of 25.0°C.")
        return default


if __name__ == "__main__":
    system = FuzzySystem()
    temperature = get_temperature()
    result = system.evaluate(temperature)

    print("Temperature:", temperature)
    print("Action:", result)