# Tech Tips: Overcoming Data Entry Errors with Creative SQL

**By Elliot Jaspin**

**Problem:** A database that lists people and companies is nearly impossible to work with because of variations in spelling. A company such as Amalgamated Zoot Suits might be listed as:

- Amalgamated Zoot Suits
- Amalgamated ZootSuits
- Amalgamated Zoot-Suits
- Amalgamated Zoot Suits Inc.
- Amalgamated Zoot-Suits Inc.
- Amalgamatd Zoot Soots

Because the database is large, correcting the spelling of every entry is not an option.

**Solution:** If we look at the variations in the spelling of Amalgamated Zoot Suits, notice that changes occur somewhere in the last half of the name. We can make use of that fact to create a new name field that uses only the first half of the name field. This is done in XDB by using two commands: Update and Xleft.

The first step, of course, is to create a new field in our hypothetical database called Badspell that will hold the new name we are creating. Let us assume we are going to use the first 11 letters of the name field. Thus the "NewName" field will be a "char" field 11 characters wide.

We then run the following command:

```sql
Update Badspell
set NewName = xleft(name, 11)
```

We can now use the "NewName" field to group, sort and order our database. Or can we?

While the "NewName" field is an improvement, it is not a perfect solution. Notice that the last entry for Amalgamated Zoot Suits contains a misspelling within the first 11 letters. If we try to group on the "NewName" field, "Amalgamatd" will be seen as a different company. There are two possible solutions: grab fewer letters to get around the misspelling or correct the original entry and rerun the update command.

Reducing the size of "NewName" might work except that there is also a person in the database named "Amalgam, Arnold." If we take too few letters, "Amalgam, Arnold" and "Amalgamated Zoot Suits" might wind up being lumped together.

It might be simpler to run the following command:

```sql
Update Badspell
set NewName = "Amalgamated"
where xleft(name,11) = "Amalgamated"
```

However, there also might be two companies who start with the word "Amalgamated." To account for that we could make "NewName" field larger and grab more letters from name or, alternatively, keep NewName the same size and use the Update command to change "Amalgamated" to "Amalgam Zoo" wherever the first 13 letters in "name" field are "Amalgamated Z." The second approach would leave us with two different "NewName" entries:

- `"Amalgamated"` for "Amalgamated Federated Industries"
- `"Amalgam Zoo"` for "Amalgamated Zoot Suits"

While we may face several more runs to account for such problems, this approach accomplishes two things: It "solves" the large majority of misspellings on the first pass of the database and it allows us to "correct" any other misspellings in subsequent passes without actually having to go into the database and make the individual changes.
