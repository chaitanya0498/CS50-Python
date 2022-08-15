**Week 3 - Exceptions**

SPECIFICATIONS

1. FUEL GUAGE

In a file called `fuel.py`, implement a program that prompts the user for a fraction, formatted as `X/Y`, wherein each of `X` and `Y`
 is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output `E` instead to indicate that the tank is essentially empty. And if 99% or more remains, output `F` instead to indicate that the tank is essentially full.

If, though, `X` or `Y` is not an integer, `X` is greater than `Y`, or `Y` is `0`, instead prompt the user again. (It is not necessary for `Y` to be `4`.) Be sure to catch any exceptions like [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) or [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).


2. FELIPE'S TAQUERIA

One of the most popular places to eat in [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Felipe’s Taqueria](https://www.felipesboston.com/), which offers a [menu](https://www.felipesboston.com/menu) of entrees, per the `dict` below, wherein the value of each key is a price in dollars:

```
{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

In a file called `taqueria.py`,
 implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (`$`) and formatted to two decimal places. Treat the user’s input case
insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be [titlecased](https://docs.python.org/3/library/stdtypes.html#str.title).


3. GROCERY LIST

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called `grocery.py`, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.


4. OUTDATED

In a file called `outdated.py`, implement a program that prompts the user for a date, [anno Domini](https://en.wikipedia.org/wiki/Anno_Domini), in month-day-year order, formatted like `9/8/1636` or `September 8, 1636`, wherein the month in the latter might be any of the values in the `list` below:

```
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
```

Then output that same date in `YYYY-MM-DD` format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


Link to lecture

https://cs50.harvard.edu/python/2022/weeks/3/
