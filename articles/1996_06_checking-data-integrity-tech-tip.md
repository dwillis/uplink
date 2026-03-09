# Tech Tip: Checking Data Integrity

## By Drew Sullivan
*Associated Press*

A pair of mantras that NICAR's Richard Mullins teaches his students at the Missouri School of Journalism is: "All databases are bad," and "All data is dirty."

If you've worked with many databases, you soon realize the truth in these statements. Underpaid and overworked government data-entry clerks will forever confuse similar postal codes, such as Missouri (MO) and Montana (MT) or Connecticut (CT) and Colorado (CO). And even the most clever database designers cannot account for incomplete forms, typos and just plain wrong information. But even flawed databases can yield a wealth of information. The key is to understand and quantify the limits of the database. A database must be checked for internal integrity, or how clean the database is kept, and external integrity, or how inclusive is the database.

### Improving Internal Integrity

The first step in processing any database is to "scrub" the data to remove inconsistencies. The user should convert all lower case letters to uppercase and should trim all unwanted spaces. These steps should be done even if the data appear to be uniform; it is not good enough to assume that since the first 1,000 records are upper case all the records will be.

In FoxPro, these steps are easily done with the following statements:

```
REPLACE ALL fieldname WITH;
ALLTRIM(fieldname)

REPLACE ALL fieldname WITH;
UPPER(fieldname)

REPLACE ALL fieldname WITH;
STRTRAN(fieldname,space(2),space(1))
```

The first command removes all spaces before and after the data. The second command converts everything to upper case. The final command replaces every occurrence of two spaces with one space. Run the last command a few times to convert all multiple spaces.

Once the data has been scrubbed, test the important fields to see how populated they are and whether the data meet expected norms. Consider a national database of train accidents (TRAIN). A simple SQL command to test the integrity of the field that reports the state in which the accident occurred (ACCSTATE) would be:

```
SELECT ACCSTATE, COUNT(ACCSTATE);
FROM TRAIN;
GROUP BY ACCSTATE;
ORDER BY COUNT(ACCSTATE)
```

The result would be a list of states and how many accidents occurred in each:

```
IL    23,908
CA    18,991
TX    11,444
       9,773
NY     8,663
```

The result reveals that 9,773 fields — a sizable part of the database — do not contain state names. In addition, it indicates that Illinois has the most accidents, which might be expected because Illinois has a large number of railroad hubs. The absence of a state or the presence of very few records from a state might indicate that data may not have been collected by a state. There is a serious problem if Hawaii leads the nation in railroad accidents.

This same procedure can be used for all geographical entities, including counties, cities, ZIP codes, and congressional districts, as well as to check any field where there is an expected range of values, such as companies, gender, race, candidates for office, or any coded item.

A Minnesota TV station used this method to discover that no rapes had been reported for a particular large police agency. The absence was not due to low crime but because the FBI coded rapes differently than that police agency and, rather than resolving the difference, the FBI simply left out the data.

Also look for codes that do not match the expected code values. Gender codes from one to nine might indicate that the data was improperly imported, data entry was careless, or you're dealing with a very strange group of people.

### Standardizing Data

Often data does not conform to your needs. An AP reporter wanted to list the top metropolitan areas represented by runners in the Boston Marathon. He found a database in which runners reported their hometowns as Brooklyn and Queens, rather than as New York City. The data had to be standardized to get an accurate count. In this case, the command was:

```
REPLACE ALL cityname WITH;
STRTRAN(cityname,'BROOKLYN',;
'NEW YORK CITY')
```

This same procedure can be used to correct for other data errors. For instance, if a database uses the code CO for both Colorado and Connecticut, a simple statement can correct the error. Rather than guessing whether Groton is in Connecticut, use the ZIP code in the database as follows:

```
REPLACE ALL state WITH
STRTRAN(state,'CO','CT') for zip='07'
```

This statement will change all the codes of CO to CT if the ZIP code starts with a 07.

For city names, states names and ZIP codes, the data can be easily checked by joining the data with ZIP code databases. This will standardize all the data in one step. (NICAR keeps such a database on its Web site.)

### Relating the Data

When using relational tables, check the uniqueness of key fields and the referential integrity of the data.

"I don't believe anyone who tells me it's a unique field," says Andy Lehren, database administrator for NICAR. "It's really important to double-check, otherwise all your joins get screwed up."

If a key field is not unique, records may be lost or duplicated, or unrelated records may be joined, depending on the problem. In some databases, a combination of fields may make a record unique. You can use the above SQL COUNT statement with the key field to test uniqueness. A value above one in the count field indicates a non-unique key.

After checking the uniqueness of the key field, check the referential integrity of the database. If a related table has a one-to-one relationship with the master table (i.e., there is one record in the master for each record in the related table), you should end up with the same number of records after the join as before. An outer join (sometimes called a union join) would be empty. Fewer records indicate poor referential integrity; i.e., records deleted from the master were not deleted from the related tables.

A one-to-many join should produce the same number of records as is in the "many" database.

### Null Values

Another common database problem involves null values. Say you have a field that lists state workplace violations fines. If you import the field as a character data, you might find that many of the records list fines equal to zero. Other records might be blank. Can you assume that a blank is equal to a zero? Absolutely not. It's time to call the agency and ask what it means if the field is left blank.

In FoxPro, if you convert the field to numeric to calculate average fine, those blanks will convert to zero, and your numbers will be skewed. Be careful. The lesson may be to import all fields as character fields and convert them to numeric fields later.

One warning: You cannot do this with packed fields. Packed fields must be unpacked as they are described in the record layouts, otherwise you will get bad data.

A word of caution when you modify fields: Any substantial changes increase the possibility that you are introducing errors into the database. To be safe, work only on a copy of the data, preserving the original. And, even in the working copy, it is wise to duplicate fields you wish to modify, leaving the original fields alone.

### External Integrity

After processing data, a number of external checks are recommended. Make sure the record count matches the expected number. Many databases can be checked against a report. The FBI Uniform Crime Report databases, for example, can be checked against the FBI's "Crime in the US" report, which comes out a few months earlier. If there are differences — and there often are — make sure you can explain them.

Ask the agency for reports based on your database. If they don't have them, ask if you can send them some results to look at. They know the data better than anyone and will likely see egregious errors. It's amazing how cooperative they become once they've seen you have done the work. Many times, they will recreate your results to test whether your work is correct.

Jennifer LaFleur, database editor of the *San Jose Mercury News*, checks demographic data in any database she gets against Census data.

The final step is simply to make sure things are reasonable. "Beware of the 'Wow!'," warns LaFleur. "If you see something in a database that's really cool, it's probably an error."

*Drew Sullivan can be reached at (800) 845-8450, ext. 7639, or send e-mail to drew@ap.org*
