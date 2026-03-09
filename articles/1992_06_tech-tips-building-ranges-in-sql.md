# Tech Tips

## Subject: Building Ranges in SQL

**Problem:** CBS Evening News obtained a database of approximately 15,000 children who took a test to measure the lead levels in their bodies. While the database had individual scores ranging from 0 to 45, CBS wanted a report showing the number of children with lead levels of:

- 10 to 15
- 16 to 20
- 21 to 25
- over 25

There was also the possibility that the producer would want further analysis of the children within one or several of the ranges.

**Solution:** One approach would be to do a count based on the values in the test field:

```sql
select count (*)
from leadtest
where test >= 10
and test < 16
```

This approach requires running the same query, with the test ranges modified, again and again for any further analysis. Also, there would be several pages of reports to sift through. Not a major problem, but not a very elegant solution either.

A better approach is to create a new field called "range." This is a character field 8 bytes long. The next step is to run the following update command:

```sql
update leadtest
set range = "10 to 15"
where test >= 10
and test < 16
```

After this command is run four times for each range, the following query will produce a one page report with all the necessary information.

```sql
select range, count (range)
from leadtest
group by 1
```

Any subsequent analysis would use the range field to group the children presumably saving a substantial amount of time.

If the table were larger, space could be saved by making the range field a one byte code and using a second table called "Ranges" with a code field and the text such as "10 to 15." A join of the two tables would then produce the same results.
