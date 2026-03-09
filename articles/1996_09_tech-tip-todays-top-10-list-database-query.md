### Tech Tip
## Today's Top 10 list

**By Richard Mullins**
University of Missouri/NICAR

I remember the first few times I was asked a certain "Is there a way to do this?" question. Unfortunately, I said there wasn't a way.

Turns out I was wrong (I'm writing this for penance). I should have said, "Not that I know of yet." I've managed to reassure myself by seeing my error as confirmation of one of the presumptions that I recommend to every reporter using a computer to commit journalism: If you can even dimly conceive it, there is probably a way to do it.

Here was the question: Is there a way to write a query that just gives you the top 10 (or 20 or 101) rows?

I'll cover Access first, then FoxPro. Apologies to those I've left out.

Access users who came to the software tainted with previous knowledge of SQL, a lingua franca of data analysis, probably noticed the extra keyword Access used: DISTINCTROW. I'll explain that one, too, after the ranking business.

In Access, this query, which orders candidates according to their fundraising, doesn't limit the result to any rank:

```sql
SELECT DISTINCTROW CandName, Receipts
FROM CandRept
ORDER BY Receipts DESC
```

Adding one keyword and a number gives the same results, but with a specified cutoff in rank:

```sql
SELECT TOP 10 CandName, Receipts
FROM CandRept
ORDER BY Receipts
```
