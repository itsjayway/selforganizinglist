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
    # gene_preferences = {"sports": 0.7, "music": 0.3}
    # alen_preferences = {"photography": 0.4, "music": 0.3, "sports": 0.3}
    # yuto_preferences = {"animals": 0.6, "sports": 0.3, "photography": 0.1}
    # gene_preferences = {"sports": 0.7}
    # alen_preferences = {"photography": 0.4}
    # yuto_preferences = {"animals": 0.6}
    gene_preferences = {}
    alen_preferences = {}
    yuto_preferences = {}

    gene = Profile("Gene", gene_preferences)
    alen = Profile("Alen", alen_preferences)
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
    print(shop)
    for customer in [yuto]:
        shop = store_shop.copy()
        print(f"\n\n\n===============CUSTOMER {customer.name}===============")
        for i in range(1, VISITS + 1):
            # shop.print_page()
            like_hits = 0
            print(f"*************Visit {i}*************")
            items_to_remove = []
            increase_preference_by = 0
            initialize_these_preferences = []
            for item in shop.get_products_within_threshold():
                # print(f"{customer.name} is looking at {item.name}")
                if item.category in customer.preferences:
                    like_hits += 1
                    # print(f"{customer.name} likes {item.category}")
                    if customer.preferences[item.category] > random.random():
                        # customer.preferences[item.category] += CURIOSITY[
                        #     "increase_preference"
                        # ] * random.choice([0, 1])
                        increase_preference_by += CURIOSITY[
                            "increase_preference"
                        ] * random.choice([0, 1])
                        print(
                            f"✔️  {customer.name} likes and bought {item.name} (new preference = {customer.preferences[item.category]})"
                        )
                        customer.revenue_generated += item.price
                        items_to_remove.append(item)
                        shop.products.remove(item)
                        # shop.update_items_within_threshold(AMBITION, item.category)
                    else:
                        print(f"❌ {customer.name} likes but did not buy {item.name}")
                else:
                    if CURIOSITY["multiplier"] > random.random():
                        # customer.preferences[item.category] = CURIOSITY[
                        #     "initialize_preference"
                        # ]
                        initialize_these_preferences.append(item.category)
                        print(
                            f">> {customer.name} bought {item.name} because of curiosity)"
                        )
                        customer.revenue_generated += item.price
                        items_to_remove.append(item)
                        shop.products.remove(item)
                        # shop.update_items_within_threshold(AMBITION, item.category)
                    else:
                        print(f"❌ {customer.name} did not buy {item.name} (curiosity)")

            for item in items_to_remove:  # update shop
                shop.update_items_within_threshold(AMBITION, item.category)
            for category in initialize_these_preferences:
                customer.preferences[category] = CURIOSITY["initialize_preference"]
            for category in customer.preferences:
                customer.preferences[category] += increase_preference_by

            customer.like_hits.append(like_hits)
            print(f"@@@@@@@ Like hits for visit {i} = {like_hits} @@@@@@@")
    # print(gene, end="\n\n")
    # print(alen, end="\n\n")
    print(yuto, end="\n\n")
    # plot_preferences(gene)
    # plot_preferences(alen)
    # plot_preferences(yuto)


if __name__ == "__main__":
    main()
