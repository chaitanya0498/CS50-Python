**Week 5 - Unit Tests**

SPECIFICATIONS:

1. TESTING MY TWTTR

In a file called `twttr.py`, reimplement [Setting up my twttr](https://cs50.harvard.edu/python/2022/psets/2/twttr/) from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/), restructuring your code per the below, wherein `shorten` expects a `str` as input and returns that same `str` but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

```
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_twttr.py`, implement **one or more** functions that collectively test your implementation of `shorten` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_twttr.py
```


2. BACK TO THE BANK

In a file called `bank.py`, reimplement [Home Federal Savings Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/) from [Problem Set 1](https://cs50.harvard.edu/python/2022/psets/1/), restructuring your code per the below, wherein `value` expects a `str` as input and returns `0` if that `str` starts with “hello”, `20` if that `str` starts with an “h” (but not “hello”), or `100` otherwise, treating the `str` case-insensitively. Only `main` should call `print`.

```
def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_bank.py`, implement **three or more** functions that collectively test your implementation of `value` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_bank.py
```


3. RE-REQUESTING A VANITY PLATE

In a file called `plates.py`, reimplement [Vanity Plates](https://cs50.harvard.edu/python/2022/psets/2/plates/) from [Problem Set 2](https://cs50.harvard.edu/python/2022/psets/2/), restructuring your code per the below, wherein `is_valid` still expects a `str` as input and returns `True` if that `str` meets all requirements and `False` if it does not, but `main` is only called if the value of `__name__` is `"__main__"`:

```
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_plates.py`, implement **four or more** functions that collectively test your implementation of `is_valid` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_plates.py
```


4. REFUELING

In a file called `fuel.py`, reimplement [Fuel Gauge](https://cs50.harvard.edu/python/2022/psets/3/fuel/) from [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/), restructuring your code per the below, wherein:

* `convert` expects a `str` in `X/Y` format as input, wherein each of `X` and `Y` is an integer, and returns that fraction as a percentage rounded to the nearest `int` between `0` and `100`, inclusive. If `X` and/or `Y` is not an integer, or if `X` is greater than `Y`, then `convert` should raise a `ValueError`. If `Y` is `0`, then `convert` should raise a `ZeroDivisionError`.
* `gauge` expects an `int` and returns a `str` that is:

  * `"E"` if that `int` is less than or equal to `1`,
  * `"F"` if that `int` is greater than or equal to `99`,
  * and `"Z%"` otherwise, wherein `Z` is that same `int`.

```
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_fuel.py`, implement **two or more** functions that collectively test your implementations of `convert` and `gauge` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_fuel.py
```




Link to the lesson

https://cs50.harvard.edu/python/2022/weeks/5/
