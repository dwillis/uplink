# Excel & VB help crack school finances

By Duane Schrag
*The Salina (Kan.) Journal*

All across the United States lawsuits have been filed in recent years accusing state governments of failing to provide a suitable education for their citizens. Many – perhaps most – of the cases turn on the question of adequate financing: Are schools being given enough money to educate students most at risk?

Kansas is one of those states. More than two years ago, a county district judge ruled that too little money was being spent to educate low-income, bilingual and special education students. During the litigation the State Board of Education – the principal defendant – commissioned a study to find out whether the Kansas school finance formula was appropriate and, if not, how much it would cost to implement one that was.

The study by consultants Augenblick & Myers proposed a new formula for school spending. The study's findings were presented as evidence in the case, along with the state's estimate of the financial impact of the formula. In ruling for the plaintiffs, the judge repeatedly said the cost of fixing school finance in Kansas would be at least $1 billion. However, the state had submitted a figure of $853 million. And the study estimated it at $236 million.

My story set out to answer the question: How much would it really cost to implement the findings? And how would it affect the 75 school districts in our readership area? I used Microsoft Excel, Access and Visual Basic programming to answer the questions.

Earlier, when I had asked the gurus at the state education department about that, they were dismissive. "Augenblick & Myers got it wrong," they said. I have worked with these people for years, and I took their word for it. If I had listened more closely to my instincts, we would have had this story earlier.

The Kansas Supreme Court later upheld the lower court's ruling, so the funding was in the news again. I requested figures on how the ruling would affect the 302 school districts in Kansas. The Kansas Department of Education sent me the information, with the stipulation that I not attribute it. "Even the school districts haven't seen this," I was told. That was a red flag.

Initially, the thought of calculating the cost on my own was too intimidating. But after looking closely at the formulas, I realized it was not out of the question. It required algebra, not rocket science. Calculating the cost involved:

- formulas to compute weighting factors for district size, low-income, bilingual, and special education. These factors assign more "weight" to low-income students, for instance, which increases state aid for them.
- enrollment figures for each school district, and the subgroups within each district.

The enrollment information was relatively easy to get. The state does a fairly good job of posting it and many other key tables online. Most importantly, the data is usually available as Microsoft Excel spreadsheets, so rekeying is not necessary. If possible, get this data in electronic, not paper, format. Transcription errors are too easy to make.

In my calculations, I had to make sure I was using full-time equivalents when those were required, headcounts when headcounts were required. I had to re-run the data after learning the special education figures posted online were incomplete – they excluded children in gifted programs.

The formulas themselves are straightforward – a series of If/Then statements, with assorted multiplication and division operations. Excel has a built-in If() function that I found too limited for my purposes. Instead, I wrote custom functions in Visual Basic.

Example 1 examines the adjustment for school size. This is how the consultant presented the formula for a base budget per pupil of $4,550.

**Example 1:**
```
Fewer than 430 students = {[(430 - Enroll)/10 X .01] X 4,550} + $5,852
For 430 - 1,300 students = {[(1,300 - Enroll)/80 X .01] X 4,550} + $5,358
For 1,300 - 11,200 students = {[(11,200 - Enroll)/600 X .01] X 4,550} + $4,550
More than 11,200 students = $4,550
```

Example 2 is the equivalent in Visual Basic. I named the function size_weight(), which takes as arguments the base budget per pupil (b) and the district's enrollment (e).

**Example 2:**
```
Function size_weight(b As Long, e As Long) As Long

If e < 430 Then
    size_weight = (((430 - e) / 10 * 0.01) * b) + (b * 1.2862)
Else
    If e < 1300 Then
        size_weight = (((1300 - e) / 80 * 0.01) * b) + (b * 1.178)
    Else
        If e < 11200 Then
            size_weight = (((11200 - e) / 600 * 0.01) * b) + b
        Else
            size_weight = b
        End If
    End If
End If

End Function
```

You may notice the base budget per pupil is a variable, not a constant – this made it possible to compute the cost for any base figure. For our story, we used $5,000, which was the study's original figure adjusted for inflation.

With the formulas in hand, and the raw numbers in spreadsheet format, it was a breeze to compute the weightings, and thereby create the exact budget figure for each school district. At this point, I knew how much the proposal would cost, but that was only half the problem.

The other half of the problem was comparing the proposal to the status quo. Again, finding the raw data was not difficult – every school district's budget is posted online, in sufficient detail to extract the information needed for the story.

Extracting the correct figures required some work. In order to compare apples and apples, I needed to deduct expenses for transportation, capital outlay, food service and adult education. The budget is a massive spreadsheet – it consists of 14 separate sheets, each with 302 rows (one for each school district) and as many as 20 columns of figures. Spending for the services in question were scattered across those sheets.

First, I sought help from the local school district. I sat down with the business manager and made certain I knew which columns had to be deducted to account for the necessary change. There were dozens.

Once again, I wrote a Visual Basic function to systematically extract the necessary information. While it is possible to do this by hand, the number of operations (about 10,000) makes it highly likely a mistake will be made.

Now I could make the proper comparison. I had the true cost of applying the proposal, district by district. And I had the actual comparable cost under the existing formula. I used Microsoft's Excel and Access to manage the data, although relying solely on Excel would be possible.

A&M's model was never adopted, so it is impossible to say what it would have ended up costing. But in January 2006, an exhaustive study by the Kansas Legislative Division of Post Audit on the "true" cost of providing an education said an additional $400 million is required; this comes on top of an extra $143 million added last year. That put the additional spending right where we said A&M would have put it.

Perhaps the most important lesson this story reinforced for me is that journalists must do a tricky balancing act – know when to ask for information, know when to do the work yourself.

Sources for this story gave wildly different interpretations of what the A&M study said. Some who should have known it backwards and forwards were dead wrong. Only by reading it, re-reading it, discussing it, and re-reading it further was I able to offer the story's conclusions with confidence.

Contact Duane Schrag by e-mail at dschrag@saljournal.com
