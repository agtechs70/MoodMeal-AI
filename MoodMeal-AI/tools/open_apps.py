import webbrowser
import urllib.parse


def open_swiggy(food_name):

    query = urllib.parse.quote(food_name)

    webbrowser.open(
        f"https://www.swiggy.com/search?query={query}"
    )


def open_zomato(food_name):

    query = urllib.parse.quote(food_name)

    webbrowser.open(
        f"https://www.zomato.com/search?q={query}"
    )


def open_blinkit(item_name):

    query = urllib.parse.quote(item_name)

    webbrowser.open(
        f"https://blinkit.com/s/?q={query}"
    )