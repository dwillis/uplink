# To Have or to Have Not

**By J.J. Thompson**
*U.S. News & World Report*

Income inequality—the gap between the haves and have-nots— is a topic that begs the use of computer-assisted journalism. Being one of those trends that creeps slowly and unevenly into our lives, no one has the same perception of it. If you live in Washington, D.C., the gap seems to be huge and growing every day. If you live in Hot Springs, Ark., it may not seem quite so perilous.

So an analysis of income data is a must to answer questions such as:
- How big is the gap?
- Is it getting bigger?
- How much worse is it in X than in Y?

The trick, obviously, is to measure the phenomenon in a way that readers can easily grasp its meaning. When, during the vice presidential debate, Jack Kemp mentioned *USA Today's* article mapping income inequality in the United States, I knew the Gini coefficient of inequality had done the job.

## The Gini Lowdown

The Gini formula produces a single number between 0 and 1, with 0 indicating complete equality (everyone makes the same amount of money) and 1 indicating complete inequality.

Phil Meyer, journalism professor and precision journalism guru at the University of North Carolina at Chapel Hill, heard a presentation using the Gini coefficient of inequality at a research conference. Since I was searching for a thesis topic that would incorporate data-analysis with my interest in social issues, he suggested that I look into it.

The first two hurdles were finding a formula and understanding it. After one laborious false start, I found a formula that would work with aggregated income data.

You may recognize (if you remember 10th-grade geometry better than I did) that the formula for the Gini coefficient is based on the one for measuring a triangle.

It is:

Gini coefficient=1 - SUM(Xi-Xj)(Yi-Yj)

where:
- X is the cumulative proportion of households;
- Y is the cumulative proportion of income;
- i is a particular income category;
- j is i-1, or the preceding income category.

The easiest way to conceptualize this is to picture a graph in which the final point on both X and Y axes is 100 percent, or 1.0. Points are graphed based on cumulative numbers; therefore, in a completely "income-equal" county, 10 percent of the households would take in 10 percent of that county's income, 20 percent of households would take in 20 percent of income and on up to 100 percent of the households, which would account for 100 percent of income. The points in this unusual county would form a straight line from 0,0 to 1,1— think of it as the "line of equality."

In reality, however, 10 percent of the overall households may account for only 2 percent of income; 20 percent of households only 5 percent of income and so on, so that the points would form a curve below the line of equality. By measuring the space below the curve (you can divide it up into a series of triangles) and subtracting it from 1, you get a number that indicates how big the inequality gap is. That's the Gini coefficient.

## Stories by Gini

Being able to use aggregated income instead of individual incomes, like you might do in a smaller sample, was important because the way the Census reports income data. For example, the Census will tell you only that 256 people in County X had incomes between 0 and $2,500, 345 between $2,501 and $5,000 and on up the scale.

I used the midpoint of each interval as the income for all households in that category as well as to calculate total income for each income category. This worked until I got to the final category, which was open ended. Fortunately, the 1990 Census reports total income for the group earning $150,000 or more, so it was fairly simple to divide that amount by the total number of households in that top category for its average income. I also used 1980 income data, and for that year the Census only recorded total income for the whole population. Therefore, a few more computations were needed to get an average income for the top group.

The formula is pretty easy to put into a spreadsheet like Excel, and once the income midpoints and the number of households in an income category are entered, the Gini coefficient can be calculated quickly.

For my thesis, I looked at income inequality for all 100 counties in North Carolina using income data from the 1980 and 1990 U.S. Censuses. The income distribution gap increased by at least 5 percent in 50 counties during the decade; it decreased by 5 percent or more for only nine. For my thesis article, I concentrated on the county where the gap grew the most.

In addition to providing the focus for the story, the analysis with the Gini coefficient proved a powerful reporting tool. When the county manager denied that income inequality was a phenomenon in Montgomery County, I was armed with the Gini coefficient plus the proportion of money being earned by the 400 households with income of $150,000-plus each year. He then started coughing up explanations.

The why behind the phenomenon is what proves so interesting. In this particular county, two concurrent trends were adding to the widening gap. One is that the four or so major businesses there had been family-owned for years, with the family owners/managers keeping ever-larger proportions of the profits for themselves. Meanwhile, their workers' pay had remained relatively stagnant. The other factor was who was moving into the county—at one end, rich retirees who were building homes in a ritzy lake-front community and, at the other end, poorer immigrant workers.

The result was a small but fairly divided community of the "haves" (who took little interest in community life and showed minimal concern for the needs and frustrations of the poor in their county) and the "have-nots" (who tended to be a drain on public funds and services).

Paul Overberg at *USA Today*, with the help of Meyer, used the Gini formula to examine income inequality in all counties in the nation. The analysis resulted in wonderful, detailed maps and a series in September's Money section.
