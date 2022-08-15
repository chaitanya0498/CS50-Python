**Week 6 - File I/O**

SPECIFICATIONS:

1. LINES OF CODE

In a file called `lines.py`, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.py`, or if the specified file does not exist, the program should instead exit via `sys.exit`.

Assume that any line that starts with `#`, optionally preceded by whitespace, is a comment. (A [docstring](https://peps.python.org/pep-0257/) should not be considered a comment.) Assume that any line that only contains whitespace is blank.


2. PIZZA PY

Perhaps the most popular place for pizza in [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Pinocchio’s Pizza &amp; Subs](https://www.pinocchiospizza.net/), aka Noch’s, known for its [Sicilian pizza](https://www.pinocchiospizza.net/sicilian_vs_regular.html), which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its [menu](https://www.pinocchiospizza.net/menu.html) too, per this CSV file of Sicilian pizzas, [sicilian.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv), below:

```csv
Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95
```

See [regular.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv) for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as [ASCII art](https://en.wikipedia.org/wiki/ASCII_art), like this one:

```
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
```

In a file called `pizza.py`, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using `tabulate`, a package on PyPI at [pypi.org/project/tabulate](https://pypi.org/project/tabulate/). Format the table using the library’s `grid` format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.csv`, or if the specified file does not exist, the program should instead exit via `sys.exit`.


3. SCOURGIFY

> “Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage. “[Scourgify](https://harrypotter.fandom.com/wiki/Scouring_Charm).” A few feathers and droppings vanished.
>
> — *Harry Potter and the Order of the Phoenix*

Data, too, often needs to be “cleaned,” as by reformatting it, so
that values are in a consistent, if not more convenient, format.
Consider, for instance, this CSV file of students, [before.csv](https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv), below:

```csv
name,house
"Abbott, Hannah",Hufflepuff
"Bell, Katie",Gryffindor
"Bones, Susan",Hufflepuff
"Boot, Terry",Ravenclaw
"Brown, Lavender",Gryffindor
"Bulstrode, Millicent",Slytherin
"Chang, Cho",Ravenclaw
"Clearwater, Penelope",Ravenclaw
"Crabbe, Vincent",Slytherin
"Creevey, Colin",Gryffindor
"Creevey, Dennis",Gryffindor
"Diggory, Cedric",Hufflepuff
"Edgecombe, Marietta",Ravenclaw
"Finch-Fletchley, Justin",Hufflepuff
"Finnigan, Seamus",Gryffindor
"Goldstein, Anthony",Ravenclaw
"Goyle, Gregory",Slytherin
"Granger, Hermione",Gryffindor
"Johnson, Angelina",Gryffindor
"Jordan, Lee",Gryffindor
"Longbottom, Neville",Gryffindor
"Lovegood, Luna",Ravenclaw
"Lupin, Remus",Gryffindor
"Malfoy, Draco",Slytherin
"Malfoy, Scorpius",Slytherin
"Macmillan, Ernie",Hufflepuff
"McGonagall, Minerva",Gryffindor
"Midgen, Eloise",Gryffindor
"McLaggen, Cormac",Gryffindor
"Montague, Graham",Slytherin
"Nott, Theodore",Slytherin
"Parkinson, Pansy",Slytherin
"Patil, Padma",Gryffindor
"Patil, Parvati",Gryffindor
"Potter, Harry",Gryffindor
"Riddle, Tom",Slytherin
"Robins, Demelza",Gryffindor
"Scamander, Newt",Hufflepuff
"Slughorn, Horace",Slytherin
"Smith, Zacharias",Hufflepuff
"Snape, Severus",Slytherin
"Spinnet, Alicia",Gryffindor
"Sprout, Pomona",Hufflepuff
"Thomas, Dean",Gryffindor
"Vane, Romilda",Gryffindor
"Warren, Myrtle",Ravenclaw
"Weasley, Fred",Gryffindor
"Weasley, George",Gryffindor
"Weasley, Ginny",Gryffindor
"Weasley, Percy",Gryffindor
"Weasley, Ron",Gryffindor
"Wood, Oliver",Gryffindor
"Zabini, Blaise",Slytherin
```

Source: [en.wikipedia.org/wiki/List_of_Harry_Potter_characters](https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters)

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if [Hogwarts](https://en.wikipedia.org/wiki/Hogwarts) wants to send a [form letter](https://en.wikipedia.org/wiki/Form_letter) to each student, as via [mail merge](https://en.wikipedia.org/wiki/Mail_merge), since it’d be strange to start a letter with:

> Dear Potter, Harry,

Rather than with, for instance:

> Dear Harry,

In a file called `scourgify.py`, implement a program that:

* Expects the user to provide two command-line arguments:

  * the name of an existing CSV file to read as input, whose columns are assumed to be, in order, `name` and `house`, and
  * the name of a new CSV to write as output, whose columns should be, in order, `first`, `last`, and `house`.
* Converts that input to that output, splitting each `name` into a `first` name and `last` name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via `sys.exit` with an error message.


4. CS50 P-SHIRT

After finishing CS50 itself, students on campus at Harvard traditionally receive their very own [I took CS50](https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt) t-shirt. No need to buy one online, but like to try one on virtually?

In a file called `shirt.py`, implement a program that expects exactly two command-line arguments:

* in `sys.argv[1]`, the name (or path) of a JPEG or PNG to read (i.e., open) as input
* in `sys.argv[2]`, the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay [shirt.png](https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png) (which has a transparent background) on the input after resizing and
cropping the input to be the same size, saving the result as its output.

Open the input with `Image.open`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open), resize and crop the input with `ImageOps.fit`, per [pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit](https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit), using default values for `method`, `bleed`, and `centering`, overlay the shirt with `Image.paste`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste), and save the result with `Image.save`, per [pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save).

The program should instead exit via `sys.exit`:

* if the user does not specify exactly two command-line arguments,
* if the input’s and output’s names do not end in `.jpg`, `.jpeg`, or `.png`, case-insensitively,
* if the input’s name does not have the same extension as the output’s name, or
* if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like [these demos](https://cs50.harvard.edu/python/2022/psets/6/shirt/#demos), so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as `shirt.py`.
 No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of [CS50’s communities](https://cs50.harvard.edu/python/communities)!



Link to the lesson

https://cs50.harvard.edu/python/2022/weeks/6/
