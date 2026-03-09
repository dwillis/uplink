### Money & Sports
## Bending the Rules

**Greg Reeves**
*The Kansas City Star*

Eight databases contributed to *The Kansas City Star's* six-day series Oct. 5-11 on the role of the National Collegiate Athletics Association and money in college sports.

The NCAA provided two of the databases on diskettes, including a history of student-athlete graduation rates by school, sport, race and sex, and 100,000-plus votes by member schools on NCAA legislation in the past four years.

The NCAA also gave us early access to its Web site that will contain text files of all major NCAA infraction cases since 1987.

We built several other databases by scanning the NCAA membership directory and 1,200 pages of NCAA convention books containing 694 legislative proposals since 1993 with accompanying discussion.

And, like several other news organizations, we used data entry to create tables from the 1996 Gender Equity Disclosure Act forms we requested from 305 NCAA Division 1 colleges and universities.

None of the databases in this project were particularly complicated. The lessons for computer-assisted reporting had more to do with scanning, data entry and text analysis.

The generated files gave us the ability to search for statements on NCAA legislation by school officials and others. It also enabled us to build a searchable database of every NCAA legislative proposal since 1993.

The data entry taught me a valuable lesson. We hired temps, some of them very good, to input gender equity forms and NCAA infraction summaries. Then we hired other temps to proofread the work. At the end we still had errors embedded in the data — fewer than a dozen, but dangerously hidden until uncovered by a query or report.

It would have been cheaper to have two persons enter the data, then compare the results. That's how I plan to approach future projects requiring data entry.

The NCAA graduation-rates database comes from a complex report submitted annually by Division 1 schools detailing enrollment and degrees received in 42 categories by student-athletes and other students.

Most of the same data is published in the NCAA's yearly Graduation Rates Report. The book lists a number range for athletes graduating in each sport; the database lists the actual number. We asked the NCAA for this database and they provided us with four Paradox tables zipped onto a single diskette.

The database makes it possible to rank schools by graduation rates of student-athletes or other students.

We created flags for whether schools were public or private, and which had the best won-loss records over the past decade.

These flags, along with fields on gender, sport, race and athlete type (aid or transfer) made it possible to analyze graduation rates in literally hundreds of ways.

The infractions files, which we downloaded from the NCAA's yet-to-be-released Web site, totaled more than four megabytes of text. There were 124 files, some as long as 10,000 words.

As I read each file I typed in brief markers, or flags, for the source of the infraction (the NCAA, the school, the press, etc.) and for every penalty listed (coach fired, sport suspended, etc.).

Then I wrote a short program in XPL, the Xywrite scripting language, that flew through the files and threw the file name and flagged text (usually just a few words) into a file.

I appended this 1,700-line text file to a FoxPro table, then linked that with the NCAA Enforcement Summary, which lists probation, postseason bans and television bans for major infractions since 1952.

We now had a powerful way to analyze NCAA enforcement trends and show, that tough measures like bans on post-season play and television were being replaced by often meaningless probation.

We collected gender equity forms from 305 Division 1 NCAA schools and analyzed them about the same time as several other newspapers.

The reports showed that women are 52 percent of students at Division I schools, but only 37 percent of athletes. It also showed schools overall lost about $200 million on sports programs in 1996.

The federal law requires schools to fill out eight tables, on enrollment, athletic participation, number of coaches, average coaches' salaries, operating expenses, recruiting expenses, athletic aid and overall revenue and expenses. The reports are due Oct. 15 each year.

The NCAA also gave us with diskettes containing FoxPro tables of more than 100,000 votes by the 933 member schools at the organization's past four annual legislative conventions.

This database showed how hard it is to categorize political legislation.

We examined each of nearly 700 proposals and tried to flag each one with some kind of meaningful evaluation. In the end, however, the database told us mainly what the NCAA did and did not address.

**News releases about recent cases involving rule infractions are now available at www.ncaa.org/releases.**

*Greg Reeves can be reached at (816) 234-4366 or by e-mail at greeves@kcstar.com*
