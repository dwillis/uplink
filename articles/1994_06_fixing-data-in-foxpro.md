# Fixing Data in FoxPro

**By Richard Mullins**
*University of Missouri*

When you're cleaning up data or making names, addresses, and other details consistent, some changes can be done on a field as a whole. For example, if the city field has "St. Louis" or "Saint Lewis" you can issue a command to change it to "ST LOUIS" in every case.

The SQL command for this is UPDATE. FoxPro, while it supports SQL, does not include the UPDATE command, since the XBase command language that FoxPro also uses already had an equivalent command for UPDATE.

In FoxPro, the command for this task is:

```
REPLACE ALL city WITH "ST LOUIS" ;
FOR city = "St. Louis" OR city = "Saint Lewis"
```

The FoxPro command words are capitalized in this example for clarity. The semicolon allows you to continue the command to the next line.

You'll notice that not only did this example fix a gross misspelling and standardize on the abbreviation for "Saint," it also capitalized every letter and got rid of the period in the abbreviation. Both of these steps are good standards for address information and are used by the Federal Election Commission and the Postal Service.

To carry out this standard of no periods in an address field, we need a command to search and replace inside a field. Here's the FoxPro command:

```
REPLACE ALL address WITH STRTRAN(address, "." )
```

The STRTRAN() function does the work inside the fields. The syntax for STRTRAN() looks like this:

```
STRTRAN ( <FieldName>, <SearchFor>, <ReplaceWith>)
```

The function takes its working instructions from the stuff you put inside the parentheses. The computer word for "stuff inside the parentheses" is "arguments."

The first argument says "Here's where to do the work." A comma signals the second argument, which says "Look for this string of characters." The third argument says "Replace all the strings with this string." If the third argument is missing, then the search string is replaced with nothing. In this case, the periods are removed and nothing is put in their place.

Here's a before-and-after picture:

```
23 Elm St. N.W.
23 Elm St NW
```

To capitalize everything in the address field:

```
REPLACE ALL address with UPPER (address)
```

*Mullins can be reached at Jourram@muccmail.missouri.edu.*
