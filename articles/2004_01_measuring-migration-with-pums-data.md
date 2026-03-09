# Measuring migration with PUMS data

By Ron Shawgo, *The (Fort Wayne) Journal Gazette*

If someone would have asked me a year ago what PUMS stood for I might have said a "Pretty Ugly Mess of Statistics," with the meaning of the "s-word" negotiable.

I've known for some time that the U.S. Census Bureau's Public Use Microdata Sample allowed users to dive deeper into the seemingly bottomless pit of Census data. But after three years as my newspaper's Census coordinator and writing numerous Census stories, I was ready to relegate PUMS to the "Isn't That Nice" pile. What more could be written?

That changed when journalists like Robert Gebeloff of *The* (Newark N.J.) *Star Ledger*, Mark Houser of Pittsburgh's *Tribune-Review* and *The Charleston Daily Mail's* Brian Bowling mentioned stories using PUMS on the IRE and NICAR listservs. All three wrote about population migration, in particular about the loss of people to other states.

Borrowing from their ideas, I later told our readers that Indiana had the largest estimated net loss of college-educated 25- to 34-year-olds of any state between 1995 and 2000. It would have been difficult to do the story without the Integrated Public Use Microdata Series (IPUMS) maintained on a user-friendly Web site by the University of Minnesota. More on that later.

In barest terms, PUMS data contains responses from individual Census returns with identifying information such as names and addresses removed. The results are weighted so the data from a single return might represent 100 people.

Journalists and other researchers unsatisfied with the tabulations the Census Bureau routinely releases can pick and choose the information they want for their own tabulations. Simply sum the number of people in the weighted column and you're on your way.

PUMS comes in two flavors: 1 percent and 5 percent samples of the population. The 5 percent files are much larger and were just being released as I began my research. I chose the 1 percent sample for that reason and because it was available on the IPUMS Web site. Mindful of sampling error in the data I went no smaller than the state level for my analysis.

### Downloading PUMS

The Web site, *www.ipums.org*, allows users to download extracts containing just the information they need, including figures for all states. This ability to compare states is important. Otherwise, journalists looking at state trends would have to download large files for all 50 states (51 including Washington D.C.) from the Census Bureau Web site. I don't have that kind of computer storage space.

One caveat: IPUMS data file options are SPSS, SAS and Stata, all statistical programs. Anyone using the site should read the online documentation.

IPUMS is a free service, but registration is required. The IPUMS folks ask for proper attribution and a copy of any story published, and require those who download information to "Use it for GOOD — never for EVIL." A fair deal, I think.

After registering, you start the IPUMS download at the "Create New Extract" link. The page asks for your e-mail address and lets you chose the type of file you want (regular density for the 1 percent sample). Selecting "Only the most commonly requested samples," will serve up the 2000 PUMS data as an option.

Click "Continue to Sample Selection." On this page I chose a rectangular file in SPSS format and checked the box for "2000 1% Census PUMS."

Click "Continue to Variable Selection." This is where you'll choose the information in which you are interested.

For my statewide migration story I chose STATEFIP (state FIPS code), PERWT (the weighted number of people for a given variable), AGE (I also checked the "case selection" box to the right), BPL (birthplace – general), EDUC99 (educational attainment), MIGRATE5 general (migration status five years ago) and MIGPLAC5 (State or country FIPS code of residence five years ago). I also was interested in income so I chose INCTOT (total personal income) and INCWAGE (wage and salary income).

Click "Continue to Case & Flag Selection." Here I chose "Include only those persons meeting case selection criteria." Because I marked the case selection box for AGE on the previous screen, the Web site now gave me the option of selecting the ages I wanted. I chose 25 through 34.

Click "Continue to Extract Request Summary." Users are given the chance to make changes and write a brief description of the data before clicking "Submit Extract Request." The data will be delivered to your e-mail account. It's been my experience that the data usually is delivered within 10 minutes. A modem connection might be slower.

The e-mail includes a link to where the data can be downloaded. The files come zipped, so you'll need a program to expand them. I easily opened my data in SPSS. Because I'm not yet proficient in that program I then saved the data as dBASE file, which I imported into Microsoft Access.

### Filtering and querying

I ran a query to extract from the EDUC99 field those with at least a bachelor's degree. For this and other operations you'll need to know IPUMS codes (14 = bachelor's degree, 15 = master's degree, etc.). Read the online documentation.

To find how many college-educated 25- to 34-year-olds left Indiana between 1995 and 2000, I filtered out Indiana in the STATEFIPS column but used it as the criterion in the MIGPLAC5 column. In other words, I asked to see those folks who lived in Indiana in 1995 but left by 2000. Summing the PERWT column gave me 58,887. Another caveat: It's impossible to get the number who moved abroad.

To find how many entered the state, I did just the opposite. I used Indiana as the criterion in the STATEFIPS column but filtered it out of the MIGPLAC5 column. Still, this didn't give me an accurate answer. People who lived in the same house in Indiana (those recognized as not applicable to my query criteria) also popped up. MIGPLAC5 assigns "0" to those not applicable folks. After filtering them out, summing the PERWT column gave me 41,782.

I did this for every state, placed the results in Microsoft Excel and sorted on the difference between those who entered and left. Indiana's estimated net loss of 17,105 was the largest.

I used STATEFIPS (where people lived in 2000) and MIGPLAC5 (where they lived in 1995) and BPL (birthplace) to track the migration of native Hoosiers for a sidebar, an idea I stole from Robert Gebeloff, who had looked at New Jerseyans. I was able to compare education and income levels of native Hoosiers who still lived in Indiana with those who left the state. I also found that some of Indiana's largest salaries go to residents who were born elsewhere.

With the numbers crunched I was able to find native Hoosiers living in other states by tapping into Purdue University and Indiana University alumni clubs listed online. Club presidents in other states were usually willing to talk or forward me to someone who would.

Contact Ron Shawgo by e-mail at rshawgo@jg.net.

---

**readme.txt**

For a detailed introduction to PUMS read Tipsheet No. 1614 by Richard O'Reilly of the *Los Angeles Times*, available at no cost to members at the IRE Resource Center Web site at **www.ire.org/resourcecenter**. Others can order a copy of the tipsheet by contacting the Resource Center at 573-882-3364 or rescntr@ire.org.
