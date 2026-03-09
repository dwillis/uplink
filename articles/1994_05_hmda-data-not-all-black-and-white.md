### Making sense of it all
## Data only part of HMDA story

**By Seth Hamblin**
*NICAR Staff*

Reporters across the country are turning up the heat on banks with computer-assisted stories that show a much higher loan-denial rate for minorities than caucasians. But the tale told by Home Mortgage Disclosure Act data isn't as clear as black and white, reporters say, and bankers are claiming it's more a matter of green.

In St. Louis, a Jan. 10, 1993, HMDA analysis by George Landau of the Post-Dispatch, who used SPSS statistical software, found that blacks were being rejected for home-purchase loans 2.5 times more often than whites. In Detroit, Dan Gillmor of the Free Press reported in a Jan. 17 story that the loan denial ratio was 2.1 to 1.

And figures for the entire country show only a slightly lower lending gap.

The analysis is so important and so easy to do, Gillmor said, that it should be attempted every year in every community.

"The banks know the stories are being done every year, and they're definitely making more of an effort towards minorities," he said. Due to media attention and stronger home mortgage regulations, Detroit lenders are now reviewing denials of minority applicants, hiring minority loan officers and opening offices in black neighborhoods, Gillmor said.

However, banks say these numbers don't tell the whole story. They claim their decisions are based on wise banking practices, not discrimination. A higher percentage of black applicants are rejected because they have poorer credit histories, fewer assets and less job stability than white applicants, lenders say.

"We deny any overt discrimination," said a banker in Gillmor's story. "The data tell us there's a problem, but reasonable people disagree as to the extent and reason for the problem."

But Orange County Register reporter Ronald Campbell said banks are contradicting themselves when they deny claims of racism.

"They're saying, 'it's not as bad as you claim, but we'll do better next year,'" he said.

Campbell said that with affluent blacks and Hispanics getting turned down more often than poorer whites in Orange County, Calif., the numbers clearly point to lender discrimination. His Nov. 29, 1992, analysis showed that blacks and Hispanics with high incomes ($75,000 or greater) have denial rates of 26 and 27 percent, respectively, while whites with much lower incomes (under $50,000) have a denial rate of only 23 percent.

Although the database includes fields for an applicant's race and income as well as loan amount, lenders aren't required to fill in a field that gives a denial reason, and in many cases, don't. Because of this and other inconsistencies, reporters must recognize the limitations of the data, Gillmor said.

"What this data is good for is raising questions," he said. "It's not a smoking gun, but it gives community activists something to work with."

HMDA records are made available from the Federal Reserve every November and also can be acquired through NICAR. A nationwide database, HMDA is huge, with last year's data containing more than 12 million records from 9,072 lending institutions.

But HMDA can easily be whittled down to a smaller geographic area using fields for county code and census track numbers. From the 1992 data, Gillmor chose seven counties in the Detroit area with about 229,000 loan applications.

HMDA has two datasets, one with loan information and the other with a list of lenders and their ID codes. Gillmor used FoxPro for Windows to combine the two datasets and produce smaller more manageable subsets from the more than 30-megabyte database. He then imported the data into SPSS for windows in order to use the program's more sophisticated cross-tabbing functions.

"It was really simple, but there are a couple of little tricks," Gillmor said. Numbers in the census tract field came through as six-digits without a decimal. Gillmor had to create a new field and divide by 100 in order to get an accurate tract number.

In his story, Campbell combined census tract and HMDA data using FoxPro to look for instances of redlining, the practice of drawing a line on a map around poor or minority areas and denying loans on property within the boundary.

Nowhere did Campbell find clear-cut instances of redlining, where banks denied lending entirely. However, he did find that 18 of the 21 census tracts with denial rates greater than 30 percent were in mostly Hispanic areas.

Campbell also ran into an unusually high denial ratio in a type of area he wasn't looking for. In ritzy Newport Beach, where houses had sold for $750,000 during a 1989 housing boom and two years later dropped in value by one-third, lenders refused a large number of home-purchase and refinancing loans. This could be a story in itself, Campbell suggested.

Looking at St. Louis records, Landau used a HMDA field that identified loan type to isolate a subset just for home-improvement loans. He found that in 14 of the city's 400 census tracts, more than half the black applicants were turned down. In only one of the tracts did the rejection rate for whites top 50 percent.

The numbers demonstrate that banks often refuse to lend money to renovate low-value property in minority areas, Landau said. This creates a viscous circle, where the neighborhoods that most need improvement dollars can't get them.

"It can have a devastating effect on a neighborhood," he said. "It's like cutting off life support."

HMDA records for home-improvement loans may also be a good place to jump into stories that don't center on race. Landau suggested doing a trend story detailing where the most new homes are being bought and where most restoration is being undertaken.

"You could use the data to see what neighborhoods are making a comeback," he said.

---

### HMDA data pitfalls

**While HMDA is in many ways a simple database, there are still many things to watch out for, said** *Allentown Morning Call* **reporter David Washburn. Here are a few of the suggestions he made for avoiding pitfalls:**

- Use an application that can generate crosstabs. Spreadsheets and database managers don't have enough power to create quality crosstabs for HMDA analysis.
- A field called "edit status" tells whether there is an error in the record, but it doesn't say where the error is. Records that are marked as having errors should be thrown out.
- Some of the records have N/A in the fields for race or income. These records must also be thrown out.
- Separate one-to-four family dwellings from multifamily and commercial property when generating percentages.
- When combining HMDA and census data, if your census records are broken down into blocks, you will have to spend some time adding them together into tracts in order to compare them with HMDA records.
- Look out for different banks with the same ID number. If two banks merge after the reporting period, they will be reported as one institution although they were separate entities at the time the data were generated.
- Double check your numbers with each bank. If their numbers are different, make sure they're breaking down the data the same way you are. For instance, if you're looking at just one-to-four family homes, make sure their numbers don't reflect multifamily dwellings as well.
