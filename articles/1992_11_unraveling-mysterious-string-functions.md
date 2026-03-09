# Unraveling Those Mysterious String Functions

*Tech Tips*

**By George Landau
St. Louis Post-Dispatch**

String functions are the E. Coli of computer-assisted reporting. Digesting a database can be impossible without them, but who likes to talk about it?

I, for one, don't like even to admit knowing such stuff. But this being a forum for geekspeak, I swallow my pride and cough up the following.

## All about string functions:

String functions are the features of a database manager or spreadsheet that allow you to alter text in a field through truncation or substitution.

Say you want to match two databases in which names and addresses are the only identifiers. One of the databases is a list of private lawyers who occasionally do work for the state; the other is a list of contributors to the campaign of the state's attorney general, who hires the private lawyers without competitive bidding.

The database of lawyers has records like this:

| **LAWYER NAME** | **ADDRESS** |
|---|---|
| Dew E. Cheatham | 2424-A Greenback Way |
| Hope U. Cansue II | One Mercantile Center |

And the contributors database looks like this:

| **NAME** | **ADDRESS** |
|---|---|
| Cheatham, Dew E. Jr. | 2424 Greenback |
| Cansue, Hope U. II | #1 Mercantile Ctr. |

To minimize the amount of manual comparison you'll have to do between the databases, you'd want to standardize the formats of names and addresses. It would help to split each name field into four new fields: **LASTNAME**, **FIRSTNAME**, **MIDDLEINIT** and **JRSR**. You could split the address fields into **NUMBER**, **STREETNAME** and **STREETSUFFIX**.

I don't have the space to go through each step, but I'll explain how you could use string functions to extract each piece of information for the new fields. (Note: I'll be referring to string functions available in FoxPro 2.0; I believe that similar functions are available in dBASE and Paradox, although XDB users might find their selections of string functions to be more limited.)

FoxPro has a handy function called **AT( )**, which returns the location of a character in a string. For example, in the **NAME** field with the value "Cheatham, Dew E. Jr.," the function **AT(",",name)** returns the number 9 — the position of the comma from the start of the **NAME** field (the capital "C" is in position 1). If there were two commas in the **NAME** field and we wanted everything to the left of the second one, the **AT( )** action could help us: **AT(",",name,2)** will give the position of the second comma. **AT( )** can have two or three items between its parentheses: the first item is the string to search for (it can be more than one character), the second is the field to search, and the third, optional item denotes which occurrence of the string to search for.

To extract the last name from the field containing "Cheatham, Dew E. Jr.," we want the first eight characters starting from the left. The function **LEFT(name,8)** would yield the string "Cheatham." To automatically extract all characters to the left of a comma, no matter where the comma appears, you can combine the **LEFT( )** function with the **AT( )** function: **LEFT(name,AT(",",name)-1)** will do the trick.

Another function, **SUBSTR( )**, can pull a string of any length from any position in a text field. **SUBSTR(name,3,6)** would return the characters "eatham": the function went to the third character in the **NAME** field and extracted the next six characters.

You could write a short program that scans through each record of the file, combining **SUBSTR( )** with the **AT( )** function to pull out text between the first and second spaces that occur in a name field with the format, "Firstname I. Lastname." Then, using the **LEN( )** function, you could copy that text to the **MIDDLEINIT** field if the text is only one or two characters long, or copy it to the **FIRSTNAME** field if it is longer.

Another string function that can prove mighty useful is **STRTRAN( )**. This one automatically searches a field for any string you specify and replaces it with whatever else you specify — or deletes it altogether.

**STRTRAN(name,"eat","chow")** would replace "Cheatham, Dew E. Jr." with "Chchowham, Dew E. Jr." You can use this function to remove all punctuation — **STRTRAN(name,"-")** would strip the periods from the name field, for example — or to standardize the spellings of small numbers in addresses or street names (**STRTRAN(address,"One ","1")** or **STRTRAN(address,"Tenth","10th")**).

One last tip: A string function called **SOUNDEX( )** can be useful in matching phonetically similar words with minor spelling variations. The function returns a four-character code describing the sound of a word; "Diane," "Dyann" and "Deanne" all produce the same SOUNDEX code of D500. This function is useful in identifying possible matches that deserve closer inspection — matches that the computer would otherwise miss.

If string functions seem a little complicated, don't worry. These things start to make sense only after you've experimented with them for a while. But they are worth learning, because they'll save you lots of time in the long run. If you have any questions, don't hesitate to call me at the Post-Dispatch: (314) 340-8296.
