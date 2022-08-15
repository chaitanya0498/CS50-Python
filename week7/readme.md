**Week 7 - Regular Expressions**

SPECIFICATIONS:

1. NUMB3RS

In a file called `numb3rs.py`, implement a function called `validate` that expects an IPv4 address as input as a `str` and then returns `True` or `False`, respectively, if that input is a valid IPv4 address or not.

Structure `numb3rs.py` as follows, wherein you’re welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use `re` and/or `sys`.

```
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ...


...


if __name__ == "__main__":
    main()
```

Either before or after you implement `validate` in `numb3rs.py`, additionally implement, in a file called `test_numb3rs.py`, **two or more** functions that collectively test your implementation of `validate` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_numb3rs.py
```


2. WATCH ON YOUTUBE

It turns out that (most) YouTube videos can be embedded in other websites, just like the above. For instance, if you visit [https://youtu.be/xvFZjo5PgG0](https://youtu.be/xvFZjo5PgG0) on a laptop or desktop, click  **Share** , and then click  **Embed** , you’ll see [HTML](https://en.wikipedia.org/wiki/HTML) (the language in which web pages are written) like the below, which you
 could then copy into your own website’s source code, wherein [`iframe`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) is an HTML “element,” and `src` is one of several HTML “attributes” therein, the value of which, between quotes, is `https://www.youtube.com/embed/xvFZjo5PgG0`.

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Because some HTML attributes are optional, you could instead minimally embed just the below.

```
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
```

Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g., `https://www.youtube.com/embed/xvFZjo5PgG0`), converting them back to shorter, shareable `youtu.be` URLs (e.g., `https://youtu.be/xvFZjo5PgG0`) where they can be watched on YouTube itself.

In a file called `watch.py`, implement a function called `parse` that expects a `str` of HTML as input, extracts any YouTube URL that’s the value of a `src` attribute of an `iframe` element therein, and returns its shorter, shareable `youtu.be` equivalent as a `str`. Expect that any such URL will be in one of the formats below. Assume that the value of `src` will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return `None`.

* `http://youtube.com/embed/xvFZjo5PgG0`
* `https://youtube.com/embed/xvFZjo5PgG0`
* `https://www.youtube.com/embed/xvFZjo5PgG0`

Structure `watch.py` as follows, wherein you’re welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use `re` and/or `sys`.

```
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    ...


...


if __name__ == "__main__":
    main()
```


3. WORKING 9 TO 5

In a file called `working.py`, implement a function called `convert` that expects a `str` in either of the 12-hour formats below and returns the corresponding `str` in 24-hour format (i.e., `9:00 to 17:00`). Expect that `AM` and `PM` will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

* `9:00 AM to 5:00 PM`
* `9 AM to 5 PM`

Raise a `ValueError` instead if the input to `convert` is not in either of those formats or if either time is invalid (e.g., `12:60 AM`, `13:00 PM`, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., `5:00 PM to 9:00 AM`).

Structure `working.py` as follows, wherein you’re welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use `re` and/or `sys`.

```
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
```

Either before or after you implement `convert` in `working.py`, additionally implement, in a file called `test_working.py`, **three or more** functions that collectively test your implementation of `convert` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_working.py
```


4. REGULAR, UM, EXPRESSIONS

It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The more you do it, though, the more noticeable it tends to be!

In a file called `um.py`, implement a function called `count` that expects a line of text as input as a `str` and returns, as an `int`,
 the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word. For instance, given text like `hello, um, world`, the function should return `1`. Given text like `yummy`, though, the function should return `0`.

Structure `um.py` as follows, wherein you’re welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use `re` and/or `sys`.

```
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ...


...


if __name__ == "__main__":
    main()
```

Either before or after you implement `count` in `um.py`, additionally implement, in a file called `test_um.py`, **three or more** functions that collectively test your implementation of `count` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```
pytest test_um.py
```


5. RESPONSE VALIDATION

When creating a [Google Form](https://www.google.com/forms/about/) that prompts users for a short answer (or paragraph), it’s possible to enable [response validation](https://support.google.com/docs/answer/3378864) and require that the user’s input match a [regular expression](https://support.google.com/a/answer/1371415). For instance, you could require that a user input an email address with a regex like [this one](https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address):

```
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
```

Or you could more easily use Google’s built-in support for validating
 an email address, per the screenshot below, much like you could use a
library in your own code:

![Google Form](https://cs50.harvard.edu/python/2022/psets/7/response/form.png)

In a file called `response.py`, using either [validator-collection](https://pypi.org/project/validator-collection/) or [validators](https://github.com/kvesteri/validators) from PyPI, implement a program that prompts the user for an email address via `input` and then prints `Valid` or `Invalid`, respectively, if the input is a syntatically valid email address. You may not use `re`. And do not validate whether the email address’s domain name actually exists.


Link to the lesson

https://cs50.harvard.edu/python/2022/weeks/7/
