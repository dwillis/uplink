# For the Novice
## Getting Back to Basics

**By Neill A. Borowski**
The Philadelphia Inquirer

At the outset, we have to agree on something: Much of the time we really aren't using "statistics." We're mostly in the business of measuring populations.

This distinction is important.

Many statistical tools are designed to help the researcher use samples to make inferences about the population.

In computer-assisted reporting and analysis, we usually have the population in front of us. There's no guessing what the full universe of data looks like. We have it all: Every teacher's salary in our state, every fatal traffic accident in the nation, or every sentence imposed by a judge.

By over-testing our data, we may be complicating and confusing our analysis. Avoid using statistical tools "because they're there." Always keep it simple.

With that said, here are some fundamental steps to measure your data. Let's say our database is all of the teacher salaries in a state:

### Always, always plot your data

This probably should be your first step after making sure the database is clean. Plot a histogram (for a description of a histogram, see the page margin to the right). It will show how your data are distributed. A normal distribution will be mound-shaped. Look for oddities in your data. Are there a large number of salaries far off to the right of your histogram? This could be a highly paid district.

> **A histogram looks like a column chart. However, a column in a column chart might, for example, reflect average teacher salaries (y axis) by school district (x axis). A histogram portrays the frequencies of the variable intervals we're looking at — in this case, teacher salaries. So the x axis would be intervals of salaries, such as $10,001 to $15,001 to $20,000 and so on. The y axis — which governs the height of the column — simply counts the number of salaries that fall within each of the intervals. If there are 900 teachers making $10,001 to $15,000 and 1,200 making $15,001 to $20,000 it would begin a histogram "stairstep." In a normal distribution, the histogram will rise to a peak in the middle and fall off (mound shaped).**

### Calculate the 'basics'

These are the range, arithmetic mean, the median and the mode (remember "ramm"). Lets say we're looking at salaries. The mean — often called the average — is the sum of the salaries divided by their count. The median is the salary in the middle after the salaries are ranked (when there is an even count of salaries, there will be two salaries in the middle; the mean of these two salaries is the median). The mode is the salary that appears most often. The range is the highest salary minus the lowest salary.

### Rank, rank and compare

Who gets the most? Group the districts and calculate their averages and medians. Which districts pay the most? How do these compare with the state average?

Use the total experience (in years) of each teacher to calculate the salary per experience year. Rank these. Do you have the salary from five years ago? Calculate the percentage change and rank the change. What district salaries changed the most? The least? For me, one of the handiest tools in software is the =rank function in MS Excel. It will tell you where things stand in a flash.

### Look at the spread

Two sets of data could have the same means, but would look far different when they are plotted. The average may be $45,000 for two sets of salaries. However, one may have a low salary of $30,000 and a high salary of $65,000. The other data set may have a low of $8,000 and a high of $90,000.

The range will help. But the standard deviation is a better tool to help with this. Keep in mind that there are two standard deviations – the sample and the population standard deviations. (In Excel, the sample standard deviation function is =stdev and the population standard deviation function is =stdevp).

The standard deviation offers a quick view of how the data are distributed around the mean. Rule of thumb: The mean plus and minus one standard deviation includes about 68% of the data and the mean plus and minus two standard deviation includes about 95% of the data. What are the extreme values or outliers? Check out how many salaries are beyond three standard deviations. How many go beyond two standard deviation? These may be newsworthy.

### Study the scatterplot

We're not explaining regression analysis in this article (regression looks at the impact one variable, such as experience level, has on another variable, such as salaries). However, you can quickly look at the "big picture" through a scatterplot.

The "x" (horizontal) axis is the independent variable – in this case, total years of experience for each teacher. The "y" (vertical) axis is the dependent variable – the salary of each teacher. A scatterplot will show you the regression line and the data points scattered about the line. The points farthest from the line are outliers.

A regression line in a scatterplot of teacher salaries would be upward sloping – it would go from the lower left (low experience/low salary) to the upper right (high experience/high salary). If there are points in the upper-left quadrant of your plot far from the line, it might indicate teachers who are paid a lot with very little experience. And if there are points in the lower-right quadrant, it might indicate teachers with a lot of experience but at low pay.

Neill Borowski can be reached at (609) 779-3884, or send email to neill.borowski@phillynews.com
