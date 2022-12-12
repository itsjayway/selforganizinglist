class Profile:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.revenue_generated = 0
        self.like_hits = []

    def __str__(self):
        print(f"{self.name}'s preferences:")
        for category in self.preferences:
            print(f"{category}: {self.preferences[category]}")
        return f"Revenue generated: {self.revenue_generated}"
