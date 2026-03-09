# Asbury Park Press exposes voting fraud: Voters cast ballots from grave

**By Paul D'Ambrosio**
*Asbury Park (NJ) Press*

Egads! The dead are still voting in New Jersey.

Since the invention of the ballot box, politicos around the country have always found clever ways of stuffing it with illegal votes. Rumors abound that Kennedy won the 1960 presidential election with votes from the silent majority resting in the graveyards of Hudson County, N.J., and Chicago.

Now, with proposed reforms that will make registering to vote as easy as signing a form, the *Press* wanted to see if the dearly departed were still actively involved in earthly politics. But we encountered one major obstacle: Death records kept by New Jersey, as in some other states, are private.

We had the voter registration tapes. But without death records, no comparison could be made.

The Social Security Administration came to our rescue.

The SSA has developed a "Death Master File" to record everyone with a Social Security number who has died since 1937. That translates into 40 million dead, enough records to fill 19 6,250 bpi 9-track tapes.

While the list is not perfect, it is the best there is if you can't get the full records from your state's vital statistics department. In fact, the U.S. General Accounting Office this summer praised the DMF as the most accurate collection of death records in the United States. Other departments, such as defense, routinely use the DMF to remove the dead from pension records.

I pulled out New Jersey's death records from the DMF using Nine-Track Express and compared the names and dates of birth with our voter registration tapes.

It took a 486/66 an hour to process the information with FoxPro, but it delivered gold: We found more than 400 deceased still on the voting rolls. More importantly, we found some — three in one county alone — who were continuing to vote from the grave. One man's political party even changed from Democrat to Republican after his death.

I examined the findings in conjunction with information on the National Voter Registration Act that will go into effect Jan. 1.

The act, better known as the Motor Voter law, makes registration easier, but mandates that states keep their voting rolls as clean as possible. The law is forcing states to develop statewide, computerized registration lists so they can purge those who have died or moved.

New Jersey is spending $4 million to develop such a database. For now, each county controls its own voter rolls. Checking for deaths is as low-tech as reading the obit page. However, after I told one county how we found their dead voters, officials there said they would begin using the DMF.

While the DMF only has eight fields (SSN, last name, first name, middle name, date of birth, state, zip of last residence and zip of lump sum payment), there were some tricks to massaging the information.

The DOB uses century, a format not known to Nine-Track Express. It looks like 12/12/960. To get around this, I told Nine-Track to set up four separate fields: month, day, century and year.

This meant I had to split the voter's date of birth into two new fields: month and year.

After pulling out names of the deceased by their zip codes, I joined the two files using last name, first name, month and year of birth. I excluded the day of birth since the SSA sometimes used "00" to denote an unknown day. Out of 1.3 million deaths and 450,000 voters, I only got a handful of duplicate matches on common names.

That was the easy part. In one county, about 10 percent of the voters listed as dead by the DMF were still alive. Apparently the local SSA office had a habit of killing off living spouses the same day their husband or wife died. This became a sidebar.

To be absolutely certain a voter was dead, I obtained hard copy death certificates from the state, checked voting signature books and called the next of kin before confronting election officials.

Officials tried to claim that votes by the dead were clerical errors until they saw the signature sheets showing that someone had signed in after the voter's death. Investigations are now pending.

*— Paul D'Ambrosio can be reached at pmd@app.com or by phone at (908)922-6000, ext. 4261.*

> **Note:** The master set of DMF costs about $1,073 from the National Technical Information Service (703/487-4630). NICAR is in the process of purchasing the data and will offer it to newspapers for approximately $200.
