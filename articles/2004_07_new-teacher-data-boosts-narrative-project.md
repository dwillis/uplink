# New-teacher data boosts narrative project

By Tara McLain, *Statesman Journal (Salem, Ore.)*

I was several weeks into my narrative project that involved following a college student through 10 weeks of student teaching.

The student was 54 years old and teaching was his third career. Not a normal situation — so I thought. The data told me otherwise.

After attending an IRE and NICAR Boot Camp this year, I figured I could bolster my story with some statistics about how rare it is for older people to go into teaching. I called the Oregon Teaching and Standards Practices Commission.

Just as I learned in Boot Camp, the spokeswoman didn't know the data and the data guy didn't know policy.

After a lot of conversation and getting a few sets of data with the wrong categories, the data guy e-mailed a Microsoft Excel file containing information about the 10,000 teacher licenses given out last year. The columns of data included the teacher's name, school district, date of birth, date the license was issued and the type of license.

Then I got back on the phone with the spokeswoman and found out just a few of the dozens of types of licenses are given to new classroom teachers. The rest were renewals or went to principals or many other variations.

I used Excel to filter and sort my way to the new teachers. Then I needed to calculate their ages when they got the license.

Here's where a second lesson from Boot Camp came true: The program doesn't know the difference between dates, numbers and text unless you tell it the difference. I wrote a formula for Excel to subtract the date of license from the date of birth. It gave me a huge number. Excel thinks in days, so I divided the number by 365.

Then I noticed there were some doubled, tripled, and even quadrupled, entries. I started deleting a few then scrolled down to see many more.

That's where a third lesson from Boot Camp helped: There's always a shortcut.

This was my first CAR story and I couldn't think of a way to search and destroy the duplicate rows. So I emailed Jeff Porter, the IRE and NICAR Database Library Director. He provided, with lightning speed, the perfect formula. He said he stole it from someone but couldn't remember whom. With apologies to Jeff and to the person he stole it from, here it is:

`=IF(AND(E2=E3,F2=F3,A2=A3,D2=D3),"dup","not")`

The formula tells Excel to compare information in each column by row. If a last name, first name, date of birth and date of license were all the same in one row as the row before, it would answer "dup". Then I filtered and sorted the names by duplicates and deleted them.

So a fourth lesson from boot camp came true: Cleaning the data can take longer than crunching the data.

Now, down to the analysis.

I made a pivot table of the count of teachers by age. I got one count of each teacher. Remember the dividing by 365? Excel was looking at the age of each teacher as a decimal, although I had rounded it up, and created a category for each.

I ran another formula (with the help of the research coordinator in the marketing department of our newspaper) that stripped everything off the number except the first two digits. So 35.4332355 in column H became 35 in column I after I entered the formula `=LEFT(H2,2)`.

I ran the pivot table again. I summed the counts into easy-to-digest age groups: 20 to 29, 30 to 39, and so forth.

Here's where the fifth lesson came in: Editors love pie charts.

The pie chart showed that half of the new teachers in Oregon last year were over 30. Not exactly your fresh-faced college undergrads.

I got the data from five years ago, went through all the cleaning again (much faster the second time) and found that the proportion of older people (30 plus) being hired to teach had grown from to 52 percent last year from 41 percent in 1999. That blew my assumption that all new teachers were young.

The officials said the growth probably was because of the stagnant Oregon economy in the past few years and loads of school budget cuts. Districts had their pick of new hires and were choosing older people with more life experience whom they could pay the same as 23-year-olds, they observed.

I found out that my 54-year-old student teacher isn't as rare in Oregon as I had assumed. My data-driven sidebar complemented my narrative feature.

I also found an 84-year-old teacher in my local district who just had her licensed renewed.

Contact Tara McLain by e-mail at tmclain@statesmanjournal.com.
