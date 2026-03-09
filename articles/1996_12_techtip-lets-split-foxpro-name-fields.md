## TechTip — Let's split

**By Richard Mullins**
University of Missouri/NICAR

One of the recurring questions on NICAR-L is some variation of: "I have a table with a name field and I need to ..." Those who are starting to bear the stains of exposure to computer-assisted reporting will use the term "string functions."

The advice on several occasions recently has been a brief pointer at part of the FoxPro manual or the online help, accompanied by the encouragement to sweat it out on your own. This is good, sound advice. It's not motivated by laziness or a certain relish in picturing you slogging through the personal hell they were forced to go through, back in the old days, and not like you kids today, and ... you know the rest.

Here is how to slug it out on your own. Take short steps and make sure you understand each part before you go on.

Here is the sort of answer you might get if you asked, "How do I put into a new field everything in a field that is found to the right of the comma?" (This might come in handy for fields with contents like this: Smith, Robert — or, as in our example, Clinton, William Jefferson)

```
REPLACE ALL RestName ;
WITH SUBSTR(name, AT(",",name)+1)
```

If you're thinking, "This looks cryptic and hard to understand," then you should be declared legally sane. If you get the command to work, it may be the result of some luck and a few guesses in correcting the syntax errors after FoxPro tells you that you are missing argument, missing parenthesis, etc.

To illustrate the approach, assume a table called PREZ with a field called NAME. If the table is open and the record pointer (or cursor) is on the first row, you can try out the various functions and see the results on a single row, before you make any changes to your data. In the syntax examples that follow, the line in bold type is what you see on the FoxPro screen when you type in the command window. This is the convention used in the FoxPro manual. The question mark acts as a command word and means, "print this on screen."

```
? name
Clinton, William Jefferson
```

Try out the **left** function with assorted numbers:

```
? left(name, 3)
Cli
? left(name, 11)
Clinton, Wi
? left(name, 1)
C
```

Now, the original problem, posed for the sake of discussion and also one that comes up all the time in real life, is splitting name fields that are separated by a comma. If you understand how the FoxPro **replace all** command does the changes, then you only need three string functions to do the splitting:

- left()
- at()
- substr()

The advice about sweating it out is related to the old "teach someone to fish" proverb: If you see these functions in action fixing one problem, you'll be able to figure out how to use them on new problems. After that, there is good news and more good news: There are more than three functions in FoxPro (and Access), and you know something useful about how to learn to use them.

Now, back to the command window and taking small steps to solve the task at hand. We could state our instructions in English like this: "For every row, find the location of the comma, then pick up the characters on the left side, up to, but not including the comma."

We've already seen how to print a certain number of characters, starting from the left. But names are not all the same length, which means the comma is not in the same place in every row of a table. This is not an obstacle, because of two facts about FoxPro: 1) There is a function to locate the position of a character within a string of characters, and 2) The results from one function can be submitted to another function. A short term for this, used by geeks, is nesting, an obvious metaphor when you think about it.

Applying this, we try out the **at()** function, then try combining it with **left()**, and when we're finished with that, put it all into the replace command. Using the at function on "Clinton, William Jefferson" gives the answer of 8 as the position of the comma. Note the syntax is:

```
AT(CharacterToSearchFor, StringToSearchIn)
```
