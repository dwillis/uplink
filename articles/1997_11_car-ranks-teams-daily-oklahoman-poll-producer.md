### Poll producer
## CAR ranks teams

**By Griffin Palmer**
*The Daily Oklahoman*

Much of meat-and-potatoes of day-to-day sports reporting is driven by statistics. FoxPro is ideal for processing statistics and getting them ready to put in the paper.

At *The Daily Oklahoman*, we use FoxPro to generate typesetter-ready prep football standings charts. During the basketball season, sports reporters use FoxPro to generate win-loss reports for prep teams.

Sports staffer Penny Soldan says she used to devote an eight-hour day each week to calculating prep football standings and keying them into the system. Soldan said she used to spend more than eight hours a week wrangling numbers for girls' basketball. She now does the same tasks in about 30 minutes.

### Computer rankings

Because *The Daily Oklahoman's* newsroom network is so crotchety, it has been impossible for us to create a system where agate clerks can key scores into a central database.

We've worked around the network's limitations by transferring weekly scores files out of our SII typesetting system, importing them into FoxPro, and using FoxPro's relational capabilities to write scores from the weekly scores files to a master schedule.

Then, we use FoxPro's report generator to create a weekly standings file, including typesetting codes, from the master schedule. We transfer that report back to the SII system. It's a crude solution, but it works.

I've accomplished all this with the FoxPro training I've gotten at NICAR conferences, what I've picked up off NICAR-L and other Internet lists and newsgroups, and what I've been able to dope out by reading the FoxPro manuals.

Each summer, *The Oklahoman* publishes a master schedule of all prep games. That forms the nucleus of our weekly standings system. The sports staff uses SII macros to convert the schedule into a comma-delimited file, which we import into FoxPro.

Once a week, we take the scores file published in the Saturday paper, convert it to comma-delimited, and import it into FoxPro.

Then, we run a program that compares the team, opponent and date fields in the weekly file with the same fields in the master schedule, and writes the appropriate scores into the master schedule.

This gets a little tricky. In the master schedule, every game involving two in-state teams is listed twice: Once in each team's schedule. The program has to write each score into the table twice — in reversed order. Another twist is the fact that in the weekly scores table, the winner always appears in the left-hand column; the loser, in the right.

Our program accounts for all this, and writes all the scores into the proper columns.

The master schedule contains district win-loss columns, overall win-loss columns, a column for a weighted scoring system developed by our sports staff, a column to indicate district and non-district games, and an overtime column.

After writing scores into the correct columns, the program writes 1s into the appropriate win and loss columns and calculates weighted scores. It sums in-district wins and losses, overall wins and losses and weighted scores for each team, ordering by win-loss and weighted score within each class and district.

It stores the results to a separate table, from which FoxPro generates the report.

I figured out which of FoxPro's special characters correspond to the correct SII typesetting codes by opening an SII-formatted standings file into FoxPro's text editor.

I then selected the necessary characters from FoxPro's menu of special characters and inserted them into the report profile as literals. FoxPro's report generator allows you to build expressions with FoxPro functions.

I used the iif() function to vary insertion of SII spacing codes, depending on the number of bytes written into the win-loss columns and weighted-score columns.

We sometimes get errors when a team's name is written differently in the weekly scores file than in the master schedule.

I've written queries that checks the values in the master schedule, after the program has run, against the values in the weekly scores file. Another query tests for mismatched team names when the two files don't balance out.
