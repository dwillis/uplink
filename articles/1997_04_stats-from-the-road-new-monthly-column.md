# New monthly column
## Stats from the road

*Have a problem you would like tackled in this space? Perhaps you know of a technique that you've found valuable in your work? Maybe there is something you've heard of, but would like to see discussed in greater detail? Let us know about it. Beginning this month Uplink will publish a monthly column intended to help reporters sort out the numbers they are facing every day. Written by NICAR's on-the-road training director, Sarah Cohen, the column will focus on the most basic definition of statistics — the attempt to present numbers in some meaningful way.*

**By Sarah Cohen**
NICAR Training Director

*statistics: numerical data assembled and classified so as to present significant information*
— Webster's New World Dictionary

When scores of otherwise street-wise reporters show up at conference panels with titles like "significance testing" and "regression techniques", it's clear that something is happening within the world of journalism.

And when an Associated Press bureau chief actually asks for a lecture on the use of numbers in the newsroom, it's yet another sign that numbers — yes, statistics — are becoming an important element in the beat reporter's toolbox.

Most statistics courses and books begin with a simple premise that is just not true for most reporters. They assume the bulk of our work comes from surveys, not from comprehensive reports that are collected from everyone.

We don't take a sample of hospital discharges; we look at all 40 million of them. Instead of surveying borrowers to find out if they feel discriminated against, reporters usually look to existing reports that compile information on all loan applications in their areas. In other words, instead of designing the perfect survey, reporters must decide whether to attempt a study at all, or if they should fight for records that may be of use.

We do need some simple measures that don't bog down our readers or our stories. Sure, experts will claim there's no analysis that will compensate for all the flaws in medical, education, or lending data. Fair enough. But our job is to use present information, not hide it, even when it's somewhat flawed. Our challenge is to decide when it's fatally flawed, or how to present it most fairly.

This month I'll focus on one of the tools that has become a staple in journalism — the humble crosstab. Crosstabs can reveal many relationships without clouding them through complicated formulas.

How? By giving you an apples-to-apples comparison and by providing you with information that conforms to the way reporters think — in neat categories like high and low, big and small, yes and no.

A crosstab will do the job quickly and cleanly.

We're going to use Philip Meyer's rule for crosstabs to get started: Put the "independent variable" in your crosstab as a column, and put the "dependent variable" in your crosstab as a row. Now generate the percents of the column, and you have a neat little table that you can describe easily to readers, editors and even your next-door neighbors.

### Step 1: Figure out your categories

Some categories are natural: race, sex or vote. Others require a little work. One common category is high- versus low-income. You can make this sensitive to your area or your numbers by using the quartiles in your data as cutoffs for your categories. Another approach is to split detailed categories, like those found in Census data, into natural groups. An example is the highest level of school people in an area completed: No high school, high school, some college, college, graduate school. Now you have six groups where you began with 20 or so possible values for the number of years of school completed.

Make sure every category is included in your analysis. This may mean doing a little arithmetic, or thinking of your data in a new way.

How can you get these groups? If you have SPSS, it's easy — just run Transform, Ranks, then choose quartiles instead of rank. It will give you a 1 for the lowest quartile, through 4 for the highest, as a new variable.

If you're using Excel, it takes a few more steps. The simplest way is simply to sort the values and assign them in order. You can also use the PERCENTRANK function, and round it to the next lowest quartile by using the FLOOR function. This won't be exact, but it will be close.

### Step 2: Decide which field, or variable, is independent, and which is dependent

One clue is to look for which one came first in time. The choice of insurance (or the lack of it) probably came before the birth of your newborn. The ethnic group membership (black, white or Hispanic) obviously came before income. And the income probably came before the decision to apply for a mortgage. When you have this kind of obvious sequence, the later event could depend on the earlier event. It's dependent. Remember, statistics can't tell you this. So it involves some thinking before you get started.

### Step 3: Produce the crosstab (in SPSS) or a PivotTable (in Excel)

This will count up the number of people in each cell of a square. If you've set up your crosstab with the independent variable in columns, then you just need to ask for the column percents in a crosstab or PivotTable. In SPSS, the option is under the "Cell Statistics" button. In Excel, it's under "Options" when you double-click on the data field. Here is an example of a crosstab, using an Excel PivotTable, for 2,800 mortgage applications in 1995 from high-income home-buyers in Nashville, Tenn.

| IncGrp | High | | | |
|---|---|---|---|---|
| | | **ETHNIC1** | | |
| **GIVEN** | **Data** | **White** | **Black** | **Grand Total** |
| Denied | # | 314 | 41 | 355 |
| | % Col | 12% | 31% | 13% |
| Approved | # | 2333 | 93 | 2425 |
| | % Col | 88% | 69% | 87% |
| Total # | | 2646 | 134 | 2780 |
| Total % Col | | 100% | 100% | 100% |

It doesn't take a lot of sophistication to see that the rate of denials for black applicants in this high-income group is about three times higher than the rate for white applicants. That's because you simply have to glance across the line you care about to see the difference, adjusted for the number of applications from each group.

Is this legitimate? Did it happen by chance?

We'll tackle the use of significance testing in another column. But the short answer is: It happened. For the high-income applicants in Nashville in 1995, it may not matter whether it was a fluke. We haven't tried to make anything bigger of this analysis than it is. It's a description of the facts for that year and that place, not an indication of something bigger.

### Step 4 (or is it step 1?): Don't leave your brain behind

You can make all kinds of comparisons in tables like this, but please don't leave behind what you already know about the relationship between income and education. If you test it, you'll probably find big news: People with less education have higher incomes! The reason is the "lurking variable" that so many people forget about. In this case, it's age. People reach their prime earning power in their 40s and 50s. But people are also becoming more educated.

So just like we had to control this analysis for income, we also have to control other analyses for items like age, education, poverty or a whole rash of other factors. That's why this last step might easily be your first: If you don't know what you're looking for, then read the academic literature, talk to other reporters who have covered the issue and talk with local experts before you even start.

Sarah Cohen can be reached at (301) 942-2199 or e-mail her at sarah@nicar.org.

*NICAR and IRE have many books available for purchase. Among those available are the Reporter's Handbook (3rd edition) by Steve Weinberg and The New Precision Journalism by Philip Meyer. For information on other books and ordering and pricing information call Wendy Charron at (573) 882-0684 or send her email at wendy@nicar.org*
