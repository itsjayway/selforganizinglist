from Profile import Profile
from Shop import Shop
import random

import matplotlib.pyplot as plt


def plot_preferences(profile):
    for category in profile.preferences:
        plt.plot(
            [i for i in range(1, len(profile.like_hits) + 1)],
            [
                profile.preferences[category]
                for i in range(1, len(profile.like_hits) + 1)
            ],
            label=category,
        )
    plt.legend()
    plt.title(f"{profile.name}'s preferences over time")
    plt.xlabel("Time")
    plt.ylabel("Preference")
    plt.show()


def main():
    yuto_preferences = {}
    yuto = Profile("Yuto", yuto_preferences)

    VISITS = 10
    AMBITION = 1
    CURIOSITY = {
        "multiplier": 0.15,
        "initialize_preference": 0.15,
        "increase_preference": 0.05,
    }
    shop = Shop(number_of_items=1000, items_per_page=10)
    store_shop = shop.copy()
    print(f"\n\n\n===============yuto {yuto.name}===============")
    for i in range(1, VISITS + 1):
        like_hits = 0
        print(f"*************Visit {i}*************")
        # iterate through the first 10 items in the shop, and if the yuto likes the category, buy it.
        items_to_remove = []
        increase_preference_by = 0
        initialize_these_preferences = []
        for item in shop.get_products_within_threshold():
            # compare the item to the yuto's preference probabilities
            if item.category in yuto.preferences:
                # yuto likes the item
                like_hits += 1
                # check probability and buy if it's greater than the random number
                if yuto.preferences[item.category] > random.random():
                    increase_preference_by += CURIOSITY[
                        "increase_preference"
                    ] * random.choice([0, 1])
                    # 50% chance of increasing preference
                    print(
                        f"✔️  {yuto.name} likes and bought {item.name} (new preference = {yuto.preferences[item.category]})"
                    )
                    yuto.revenue_generated += item.price
                    items_to_remove.append(item)
                    shop.products.remove(item)
                else:
                    print(f"❌ {yuto.name} likes but did not buy {item.name}")
            else:
                if CURIOSITY["multiplier"] > random.random():
                    initialize_these_preferences.append(item.category)
                    print(f">> {yuto.name} bought {item.name} because of curiosity)")
                    yuto.revenue_generated += item.price
                    items_to_remove.append(item)
                    shop.products.remove(item)
                else:
                    print(f"❌ {yuto.name} did not buy {item.name} (curiosity)")

        # After a visit, update the shop
        for item in items_to_remove:
            shop.update_items_within_threshold(AMBITION, item.category)
        for category in initialize_these_preferences:
            yuto.preferences[category] = CURIOSITY["initialize_preference"]
        for category in yuto.preferences:
            yuto.preferences[category] += increase_preference_by

        yuto.like_hits.append(like_hits)
        print(f"@@@@@@@ Like hits for visit {i} = {like_hits} @@@@@@@")

    print(yuto, end="\n\n")


if __name__ == "__main__":
    main()
