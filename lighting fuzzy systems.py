class LightingFuzzySystem:
    def fuzzify(self, light_level):
        if light_level <= 30:
            return "dim"
        elif light_level <= 70:
            return "medium"
        else:
            return "bright"

    def infer(self, category):
        if category == "dim":
            return "lights_on"
        elif category == "medium":
            return "lights_moderate"
        else:
            return "lights_off"

    def evaluate(self, light_level):
        category = self.fuzzify(light_level)
        return self.infer(category)
