# Tech tips

## Adventures in sampling: Using brute force to compensate for your ignorance about statistics

**By George Landau
St. Louis Post-Dispatch**

Using your computer's ability to generate random numbers and to repeat tasks thousands of times in a few minutes, you can use common sense — rather than a statistical formula — to figure out how likely it is that the results of your investigation are a chance occurrence.

The technique is called sampling. It requires only that you write a program that tells your computer to dip repeatedly into the data while keeping track of the results.

I decided to use this technique when I was working with the data from a corrupt workers compensation fund in Missouri. Using a database of about 12,000 claims, we had identified 15 lawyers who were working both sides of the fund — alternately filing claims on behalf of injured workers and then, with other cases, working *for* the state defending the fund against excessive claims.

Our analysis showed that this group of 15 lawyers somehow managed to win settlements that were about three-and-a-half times higher than everybody else's. One question we were asking ourselves (and that we knew our critics might raise) was this:

What are the odds that this disparity between the 15 lawyers and the rest (who numbered about 1,000) is due to chance? In other words, if you randomly picked groups of 15 lawyers from the database, how often would their combined average settlement be 3.5 times higher than everybody else's?

As you can probably gather at this point, the answer lay in the question itself. We created a table that listed each attorney whose name appeared in the database, along with the total number of cases he filed against the fund and the grand total of his settlements.

Then we wrote a program (in FoxPro, although you could do the same in Paradox) that instructed the computer to do the following:

1. Do three things 15 times:
   1. Pick a number between 1 and the total number of records.
   2. Goto that record (i.e., if the random number is 553, goto the 553rd record).
   3. Mark the record, either by tagging it for deletion or setting a value in a marker field.

2. Count the total value of settlements and the total number of claims for these 15 lawyers (summing the marked records only).

3. Calculate their average settlement (total dollars/total cases) and place this number in a field called "avg_15" in another database table called "results."

4. Count the total value of settlements and the total number of claims for everyone *but* those 15 lawyers (summing the unmarked records only).

5. Again, calculate their average settlement (total dollars/total cases) and put this number in the "results" table, into a field called "avg_rest" in the same record you just wrote to.

6. Unmark all records in the table of lawyers.

7. Do it all again. And again. And again.

> The technique is called *sampling*. It requires only that you write a program that tells your computer to dip repeatedly into the data while keeping track of the results.

We used a FOR/NEXT loop that counted from 1 to 10,000, doing the above routine 10,000 times. It took maybe 20 minutes to run. If the database had been much larger or the computer slower, we simply would have run it overnight. We probably didn't need to repeat the sampling loop so many times, but hey — we wanted to be sure.

With the inhumane chore of data sampling done, the answer to the question — how often would this happen by chance — was quickly in hand. We just counted the number of records in our "results" table where the 15 lawyers' average settlement was at least 3.5 times larger than everybody else's. There were about 60 such records among those 10,000. So the likelihood that our story was the result of chance was 6 out of 1,000, or 0.6 percent.

Knowing that pollsters and scientists are happy when the uncertainty falls below 5 percent, we were downright giddy.
