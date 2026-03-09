# Second Chances

**By David A. Milliron**
*Atlanta Journal-Constitution*
**and Chris Cantergiani**
*WSB-TV Channel 2*

Georgia courts have given Barry Williams, a low-level drug offender, a second chance — five times.

Williams is one of more than 4,900 individuals found to be given a second bite at the apple multiple times since 1985 under a law intended to give criminals with no previous record a second chance.

But an analysis by *The Atlanta Journal-Constitution* and WSB-TV Channel 2 of computer records kept by the Georgia Bureau of Investigation and the state Department of Corrections found those who already had a felony conviction — or had used the second chance offered by the legal system — managed to take advantage of loopholes and bad record-keeping to get another crack at first offender status.

And why not? Those sentenced under Georgia's First Offender Act are immediately eligible for parole, and their convictions are removed from their record if they stay out of trouble during probation.

A potential employer, for example, would not see the conviction of a job applicant who had successfully completed the terms of the agreement. The permanent record of the conviction would be seen only by law enforcement agencies.

### Sealed Records

The idea for the investigation came out of our analysis of felony conviction records while working to expose thousands of Georgia public school teachers who failed to disclose arrests on teaching applications and with the state Department of Professional Standards, which licenses educators.

For the prior investigation, we acquired databases from the Department of Corrections listing all convictions on record since the late 1970s. But the first batch of data didn't include Social Security Numbers, which are public record in Georgia, so we had to go back and request they be included.

When we got the second batch of data, however, we quickly noticed thousands upon thousands of records that were populated with S's in the name, Social Security Number and date of birth fields. A quick call to the state Department of Corrections introduced us to the First Offender Act, which they said required them to seal the records.

At a judge's discretion, someone who pleads guilty or nolo contendere to a felony in Georgia may be sentenced under the First Offender Act unless the crime is murder, armed robbery, kidnapping, rape, aggravated child molestation, aggravated sodomy or aggravated sexual battery. The court is required to review a person's criminal record for past first-offender sentencings or felony convictions. Once a first-offender sentence is complete, a person is not considered to have had a criminal conviction for that offense.

That's when we stumbled upon the current investigation. While running queries on the teacher-felon project, we found a teacher who had a prior arrest — yet a subsequent arrest had been sealed. Oops!

Yes, the first batch of data had not been redacted; it just excluded Social Security Numbers. And since both sets contained a unique identifier much like a Social Security Number for each offender, we simply performed an inner join in Microsoft Access to pluck an individual's name and date of birth from the unredacted database.

### Heavy Lifting

Now it was time for the heavy data lifting. All we had to do was apply the law to the data.

Barry Williams, our low-level drug offender, was one of the more than 4,900 individuals who matched one of our criteria. On Williams' fifth second chance, he still got a break even though his felony record went back 14 years.

To identify people like Williams who were improperly afforded first offender status, we carved the master database into separate tables that we later exported to Microsoft Excel. Anyone who had never been afforded first offender status was immediately eliminated from the pool. Those with a single first offender status were placed in one database along with all their arrest history, and those with multiple first offender status in another.

### Coding Offenders

Since neither of us are big fans of writing code unless we absolutely have to, we decided to code all the first offenders with an "X" in the state-provided "FOS" field. We then sorted each spreadsheet by name and conviction date in ascending order.

Now, this may be too simplistic a solution, but it worked fine for us. Since our spreadsheet was properly sorted, all we had to do is create the "evaluate" field and autonumber the individual convictions.

We wrote a simple formula to populate the "evaluate" field that would tell us which conviction was number 1, which was number 2, etc. Our formula assumes the column to be checked is the "unique identifier" field in Column A, and that we wanted the result to appear in the "evaluate" field, or Column E. Here's the one-line formula:

```
=IF(A2<>A1,1,E1+1)
```

We then just copied the formula down as many rows as we had data, and this did all of the counts for us. When the contents of the "unique identifier" field changed, then contents of the "evaluate" column were reset to 1, otherwise "evaluate" was incremented by 1. For those of you who prefer coding, we could have done it as such:

```
set rng = Range(Range("A2"),Range("A2").End(xldown))
Range("E1").value=1
rng.offset(0,1).formula = "=if(A2=A1,E1+1,1)"
```

OK, now here's where it got real simple. We copied the contents of the "evaluate" field and did an Edit | Paste Special | Values command so that we could preserve the auto increments as we further analyzed the data. We then did a quick filter of the "FOS" field for the X's and the "evaluate" field for records with a "1" in them. Those records were deleted.

We then again filtered the "FOS" field, but this time for blank cells, which were deleted.

### Several Second Chances

Altogether, 2,410 individuals since 1986 have been sentenced as first offenders even though they had prior felony convictions. Another 2,504 have received first offender status more than once, according to GBI records.

Among the reasons:

- Not all court systems register their convictions with the state in a timely manner.
- The transition from paper to computer can be slow in many counties, creating gaps in record keeping.
- The criminal histories in the Georgia Bureau of Investigation's "Georgia Crime Information Center" are not accurate or up to date.

Since our investigation, the state has unveiled a new automated system it is piloting in metro Atlanta that officials claim will allow law enforcement and justice officials to access an individual's criminal history in seconds, rather than what court officials said often took months. The state's attorney general has also said the state legislature needs to work to eliminate the loopholes in the system.

David Milliron can be reached by e-mail at dmilliron@ajc.com.
Chris Cantergiani can be reached by e-mail at chris.cantergiani@wsbtv.com.
