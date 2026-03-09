# Nursing Homes: Going Beyond OSCAR

**By Dave Gulliver**
*Dayton Daily News*

Grace Blankenship was getting some of the best care money could buy, making friends, talking about her favorite players on the Cincinnati Reds. Then her money ran out and everything changed.

She was moved from a facility's assisted living wing to a standard nursing home unit. There, a younger, demented male resident attacked her, threw her against a wall and broke three of her ribs.

Two weeks later, late one night, she began vomiting and went into shock from severe dehydration. By dawn, she died, with her doctor and family not notified until the last hour of her life.

Mrs. Blankenship's story exemplified two main flaws in Ohio's system of caring for the elderly: If you don't have the money, or if it runs out, your only choice is nursing homes that regularly violate standards, with virtually nothing to fear from the state.

But you need data, not anecdotes, to prove system-wide problems exist, and even more data to explain why.

### Starting out

In early 1999, the *Dayton Daily News* decided to look at how Ohio was prepared to handle the booming elderly population. That eventually focused on the available choices for long-term care, and nursing homes are by far the biggest player.

Nursing home projects typically use federal OSCAR data, the findings of health and safety inspections, to search for problem nursing homes. For us, that was just the start.

We used the state's own inspection data, which is used to create OSCAR. We wanted to undercut any "one–bad–year" arguments, so we used all the existing data.

Inspection data lets you look at types of problems – from dirty silverware to resident abuse – and whether they're widespread or rare, dangerous or mostly harmless. By tallying the citations, you can develop a crude ranking.

But that alone can be deceptive. For example, a home with one of the highest citations totals was solely for Alzheimer's patients. Advocates argue that such homes should have more staff and better training to ensure better care.

In the end, you need to know more to make valid comparisons. Demographics data was the answer. We used another Health Department data set, the annual survey of long-term care facilities. That allowed us to link citations totals with other key fields. The most important was a nine-category breakdown of ownership type, such as for-profit partnership or church-related non-profit. We also used variables such as age, race and gender breakdowns, dedicated Alzheimer's units, nursing staff per resident, owner and operator, and so on.

We linked the tables in FoxPro, then imported the result into SPSS for the serious number-crunching. We filtered the data for "apples-to-apples" comparisons of similar types of facilities, and used medians and trimmed means where appropriate to account for skewed data. SPSS's crosstabs and nifty scatterplots and histograms made the job infinitely easier, but (as we learned the hard way on a redlining story years ago) you could get to the same results with database and spreadsheet software.

### Follow the process

The inspections data – the beginning and end for many projects – was just half the picture. The most surprising findings came from the state's enforcement database.

We found that even when state inspectors found problems, they gave homes little reason to clean up their acts.

The enforcement data was far more complicated to use than the inspections data. It was drawn from a system designed for quick look-ups and case management, not aggregate analysis. That later became apparent when I asked the enforcement chief if the basic numbers were correct: 1,261 enforcement cases, 334 penalties imposed. "I have no idea," he replied. The state couldn't readily compile its results, so it just didn't. (They later did their own analysis and confirmed the numbers.)

Because of the database design, the enforcement data had even more pitfalls than the inspections data. There were multiple records for each case, one for each type of penalty proposed, and most homes had multiple cases. Typically a few penalties stuck but most were dropped.

The key was to break the table down and rebuild it several ways. For example, to see how the state handled "repeat offenders":

- Add a field to the original table to flag when a penalty stuck.
- Group the facilities by ID and case number to identify how many cases the state launched against a particular home, and order them by date of case.
- Copy the result to a new table.
- Add and fill an "action number" field. We used a FoxPro SQL program.
- Then join to the original table to add the flag field. Result: How many "strikes" a home received before the state would call it "out."

### Dealing with dirt

Like the enforcement data, most of what we used wasn't meant to be used that way.

The Health Department assigns each nursing home an ID number, which is supposed to be the standard way of identifying a home. But the inspections data is tailored for inclusion in OSCAR data, so the quality assurance bureau uses the home's Medicare number as the unique – and only – identifier. Meanwhile, another bureau maintains the demographics table. It uses the department ID field as the identifier. It also has the Medicare ID number, but frequently fills it with a dummy number. We eventually decided to capture as many homes as possible, and to play it safe: We recoded ID numbers by hand.

But simple dirt in the data wasn't the biggest problem. We had to understand how the system had changed over time. For example, in mid-1995, the feds and the state changed what counts as a serious health or safety violation, "substandard care" in health-speak.

If we didn't account for the differences, our analysis would have been garbage. We wrote another SQL program to recode the citations in different ways – to grade them by their respective rulebooks and to grade them by current and former standards.

### Use "golden" databases

Inspections, demographics and enforcement were our workhorses, but several other databases chipped in to the project.

Perhaps the best was a little in-house Excel worksheet from the Attorney General's office that summed up abuse prosecutions.

The state's deaths database essentially identified seven cases of nursing home fatalities. Victims' names are redacted from incident reports, but provide dates, locations, and sometimes gender and age – enough to find the death certificate and the name.

We also drew on the state's complaints hotline database; inspections data for assisted living facilities and group homes; and demographic data for home health agencies. Late in the process, when we'd almost given up, the state provided Medicaid Cost Reports data, which we used to check other findings.

In short, getting the data was relatively simple – but understanding it well enough to run the numbers took months. By the end, we could talk Medicaid-speak with the best of the bureaucrats.

So what did we learn?

- **Search for data where you don't expect it.** The project started with a Health Department flak saying they didn't keep an inspections database, but could provide paper summaries (sound familiar, anyone?). We went straight to inspectors to see what really existed. We never expected the Attorney General to have abuse cases in electronic form, but there they were. We didn't expect to get complaints data, but after agreeing to redact names, there it was.
- **Know when to stop searching.** We probably gathered more than we need. Several databases made only a cameo appearance in the final project. When you have enough to answer your questions, stop there and dig in.
- **Learn everything about the data.** CAR 101: Know the definitions of every field in the database, and every code in the data.

*The Dayton Daily News series is available online at www.activedayton.com/partners/ddn/projects/1999/Elder_Care/*
*The story is also available in the IRE Resource Center, story #15917.*
