import random


class Shop:
    def __init__(self, number_of_items=100, items_per_page=20):
        self.categories = [
            "sports",
            "music",
            "photography",
            "animals",
            "food",
            "fashion",
            "art",
            "gaming",
        ]
        self.products = []
        self.items_per_page = items_per_page
        self.number_of_items = number_of_items
        for i in range(number_of_items):  # Populate the shop with items
            generated_item = Item(random.choice(self.categories))
            self.products.append(generated_item)
        random.shuffle(self.products)  # Shuffle the items in the shop

    def get_products_within_threshold(self):
        return self.products[
            : self.items_per_page
        ]  # shows items at indices 0 - items_per_page

    def get_products_outside_threshold(
        self,
    ):  # shows items at indices items_per_page - 99
        return self.products[self.items_per_page :]

    def print_page(self):
        for item in self.get_products_within_threshold():
            print(item.name, item.category)

    def update_items_within_threshold(self, amount_to_move, category):
        """Deque the last item and push it to the front"""
        for item in self.get_products_outside_threshold():
            # if i == len(self.get_products_outside_threshold()) - 1:
            #     break
            if item.category == category:
                self.products.remove(item)
                self.products.insert(0, item)
                amount_to_move -= 1
                if amount_to_move == 0:
                    break

    def summary_of_products(self):
        for category in self.categories:
            count = 0
            for item in self.products:
                if item.category == category:
                    count += 1
            print(f"{category}: {count}")

    def copy(self):
        new_shop = Shop(self.number_of_items, self.items_per_page)
        new_shop.products = self.products.copy()
        return new_shop

    def __str__(self):
        self.summary_of_products()
        return f"""Shop di Jibran\n
        Categories: {self.categories}\n
        Items per page: {self.items_per_page}\n
        """


class Item:
    def __init__(self, category):
        if category not in [
            "sports",
            "music",
            "photography",
            "animals",
            "food",
            "fashion",
            "art",
            "gaming",
        ]:
            raise ValueError(
                "Category must be one of sports, music, photography, animals, food, fashion, art, gaming"
            )
        self.category = category
        self.possible_item_names = []
        if self.category == "sports":
            self.possible_item_names = [
                "soccer ball",
                "basketball",
                "tennis racket",
                "baseball bat",
                "football",
                "golf club",
                "skateboard",
                "rollerblades",
                "hockey stick",
                "gymnastics mat",
                "bowling ball",
                "helmet",
                "foosball table",
            ]
        elif self.category == "music":
            self.possible_item_names = [
                "guitar",
                "piano",
                "drums",
                "violin",
                "trumpet",
                "flute",
                "saxophone",
                "trombone",
                "metronome",
                "vinyl player",
                "karaoke machine",
                "speakers",
                "microphone",
            ]
        elif self.category == "photography":
            self.possible_item_names = [
                "camera",
                "tripod",
                "lens",
                "memory card",
                "lighting kit",
                "camera bag",
                "camera strap",
                "camera filter",
                "camera lens cap",
                "camera lens hood",
                "camera lens bag",
                "camera lens cleaning kit",
                "camera lens cloth",
            ]
        elif self.category == "animals":
            self.possible_item_names = [
                "dog food",
                "cat food",
                "fish food",
                "fish tank",
                "dog bed",
                "cat bed",
                "dog collar",
                "cat collar",
                "dog leash",
                "animal cage",
                "animal shampoo",
                "animal brush",
                "animal toothbrush",
            ]
        elif self.category == "food":
            self.possible_item_names = [
                "apple",
                "banana",
                "orange",
                "grape",
                "strawberry",
                "blueberry",
                "raspberry",
                "watermelon",
                "pineapple",
                "kiwi",
                "mango",
                "avocado",
                "pear",
            ]
        elif self.category == "fashion":
            self.possible_item_names = [
                "shirt",
                "pants",
                "shorts",
                "dress",
                "skirt",
                "jacket",
                "coat",
                "sweater",
                "sweatshirt",
                "socks",
                "shoes",
                "hat",
                "scarf",
            ]
        elif self.category == "art":
            self.possible_item_names = [
                "paintbrush",
                "paint",
                "canvas",
                "paint palette",
                "paint thinner",
                "paintbrush cleaner",
                "paintbrush holder",
                "paintbrush case",
                "paintbrush organizer",
                "paintbrush stand",
                "paintbrush storage",
                "paintbrush box",
                "paintbrush bag",
            ]
        elif self.category == "gaming":
            self.possible_item_names = [
                "controller",
                "console",
                "game",
                "headset",
                "mouse",
                "keyboard",
                "monitor",
                "chair",
                "desk",
                "headphones",
                "microphone",
                "mouse pad",
            ]
        self.price = random.randint(5, 100)
        self.name = random.choice(self.possible_item_names)

    def __str__(self):
        return f"{self.name} costs {self.price} and is in the {self.category} category."
