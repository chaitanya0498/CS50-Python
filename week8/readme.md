**Week 8 - Object Oriented Programming**

SPECIFICATIONS:

1. SEASONS OF LOVE

Python comes with a `datetime` module that has a class called `date` that can help, per [docs.python.org/3/library/datetime.html#date-objects](https://docs.python.org/3/library/datetime.html#date-objects).

In a file called `seasons.py`, implement a program that prompts the user for their date of birth in `YYYY-MM-DD` format and then ~sings~ prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from  *Rent* , without any `and` between words. Since a user might not know the time at which they wereborn, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use `datetime.date.today` to get today’s date, per [docs.python.org/3/library/datetime.html#datetime.date.today](https://docs.python.org/3/library/datetime.html#datetime.date.today).

Structure your program per the below, not only with a `main` function but also with one or more other functions as well:

```
from datetime import date


def main():
    ...


...


if __name__ == "__main__":
    main()
```

You’re welcome to import other (built-in) libraries. Exit via `sys.exit` if the user does not input a date in `YYYY-MM-DD` format. Ensure that your program will not raise any exceptions.

Either before or after you implement `seasons.py`, additionally implement, in a file called `test_seasons.py`, **one or more** functions that test your implementation of any functions besides `main` in `seasons.py` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_seasons.py
```


2. COOKIE JAR

Suppose that you’d like to implement a [cookie jar](https://en.wikipedia.org/wiki/Cookie_jar) in which to store cookies. In a file called `jar.py`, implement a `class` called `Jar` with these methods:

* `__init__` should initialize a cookie jar with the given `capacity`, which represents the maximum number of cookies that can fit in the cookie jar. If `capacity` is not a non-negative `int`, though, `__init__` should instead raise a `ValueError`.
* `__str__` should return a `str` with

 `🍪`, where *  is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then `str` should return `"🍪🍪🍪"`

* `deposit` should add `n` cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, `deposit` should instead raise a `ValueError`.
* `withdraw` should remove `n` cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, `withdraw` should instead raise a `ValueError`.
* `capacity` should return the cookie jar’s capacity.
* `size` should return the number of cookies actually in the cookie jar.

Structure your `class` per the below. You may not alter these methods’ parameters, but you may add your own methods.

```
class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...
```

Either before or after you implement `jar.py`, additionally implement, in a file called `test_jar.py`, **four or more** functions that collectively test your implementation of `Jar` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_jar.py
```

Note that it’s not as easy to test instance methods as it is to test
functions alone, since instance methods sometimes manipulate the same “state” (i.e., instance variables). To test one method (e.g., `withdraw`), then, you might need to call another method first (e.g., `deposit`). But the method you call first might itself not be correct!

And so programmers sometimes [mock](https://en.wikipedia.org/wiki/Mock_object) (i.e., simulate) state when testing methods, as with Python’s own [mock object library](https://docs.python.org/3/library/unittest.mock.html), so that you can call just the one method but modify the underlying state first, without calling the other method to do so.

For simplicity, though, no need to mock any state. Implement your tests as you normally would!


3. CS50 SHIRTIFICATE
   https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.png

Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt) t-shirt, [shirtificate.png](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png), customized with a user’s own name.

In a file called `shirtificate.py`, implement a program that prompts the user for their name and outputs, using [fpdf2](https://pypi.org/project/fpdf2/), a CS50 shirtificate in a file called `shirtificate.pdf` similar to [this one for John Harvard](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/jharvard.pdf), with these specifications:

* The [orientation](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html) of the PDF should be Portrait.
* The [format](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html) of the PDF should be A4, which is 210mm wide by 297mm tall.
* The top of the PDF should “CS50 Shirtificate” as [text](https://pyfpdf.github.io/fpdf2/Text.html), centered horizontally.
* The shirt’s [image](https://pyfpdf.github.io/fpdf2/Images.html) should be centered horizontally.
* The user’s name should be on top of the shirt, in white [text](https://pyfpdf.github.io/fpdf2/TextStyling.html).

All other details we leave to you. You’re even welcome to add borders, colors, and [lines](https://pyfpdf.github.io/fpdf2/Shapes.html#lines). Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s [tutorial](https://pyfpdf.github.io/fpdf2/Tutorial.html) to learn how to use it. Then skim fpdf2’s [API](https://pyfpdf.github.io/fpdf2/fpdf/) (application programming interface) to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of [CS50’s communities](https://cs50.harvard.edu/python/communities)!


Link to lecture

https://cs50.harvard.edu/python/2022/weeks/8/
