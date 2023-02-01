"""
Description:
    Shows usage of complex data structures.

Usage:
    python main.py
"""


def print_student_info(data):
    first_name = data["full_name"].split(" ")[0]
    print(f"My name is {data['full_name']}, but you can call me Sir {first_name}.")
    print(f"My student ID is {data['student_id']}")


def add_pizza_toppings(data, new_toppings):
    data["pizza_toppings"].extend(new_toppings)
    data["pizza_toppings"].sort()

    lower_case_toppings = []
    for topping in data["pizza_toppings"]:
        lower_case_toppings.append(topping.lower())
    data["pizza_toppings"] = lower_case_toppings


def print_pizza_toppings(data):
    print("\nMy favourite pizza toppings are:")
    for topping in data["pizza_toppings"]:
        print(f"- {topping}")


def print_movie_genres(data):
    all_genres = [movie["genre"] for movie in data["movies"]]
    genres_str = ", ".join(all_genres[:-1])
    print(f"\nI like to watch {genres_str}, and {all_genres[-1]} movies.")


def print_movie_titles(data):
    all_titles = [movie["title"].title() for movie in data["movies"]]
    titles_str = ", ".join(all_titles[:-1])
    print(f"\nSome of my favourite movies are {titles_str}, and {all_titles[-1]}!")


def main():
    data = {
        "full_name": "Hitesh Verma",
        "student_id": 10277379,
        "pizza_toppings": ["PINEAPPLE", "SAUSAGE", "PEPPERONI"],
        "movies": [
            {
                "title": "dune",
                "genre": "sci-fi",
            },
            {
                "title": "the hangover",
                "genre": "comedy",
            }
        ]
    }

    # adding another movie
    data["movies"].append(
        {
            "title": "the lord of the rings",
            "genre": "fantasy",
        }
    )

    print_student_info(data)

    print_pizza_toppings(data)

    new_toppings = ("BACON", "HOT PEPPERS",)
    add_pizza_toppings(data, new_toppings)

    print_pizza_toppings(data)
    print_movie_genres(data)
    print_movie_titles(data)


if __name__ == "__main__":
    main()
