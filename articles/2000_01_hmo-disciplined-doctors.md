# HMOs and Disciplined Doctors: The Broken Promise

**By Richard J. Dalton, Jr.**
*Newsday*

A landmark lawsuit, a monstrous database and rigorous searching using healthcare Web site search engines lie behind a recent Newsday series on disciplined doctors working in managed care.

*Newsday's* series, reported over a 10-month period, revealed that doctors who have been punished for serious or even fatal wrongdoing often continue to work for managed-care companies despite the healthcare industry's promise to screen their doctors and offer the best care to patients.

While many papers have examined HMOs' denial of treatment, this series broke ground by demonstrating that managed-care companies employ disciplined doctors, effectively breaking their promise of quality care.

Staff writer Thomas Maier reported and wrote the series, with computer analysis by this reporter and Dave Ewalt and assistance by Bob Fresco.

**The Health Department regularly releases information from the database to researchers and reporters but removes data identifying doctors to preserve their privacy.**

Before starting on the series, *Newsday* and *The New York Times* put its lawyers to work, suing the New York State Department of Health to obtain a database of information about the performance of doctors in treating patients in New York hospitals.

The Health Department regularly releases information from the database to researchers and reporters but removes data identifying doctors to preserve their privacy. That meant key information remained secret, including the license numbers of attending and operating physicians working on the patient, the admission date, payor identification number and the hospital name.

The omission of such information made it impossible to determine the quality of care by individual doctors and hospitals.

The newspapers argued that physicians had no such right to privacy but agreed that the data about individual patients should remain private. In June 1998, a state appeals court agreed with a lower-court ruling siding with the media, allowing access to the database of millions of hospital admissions.

**Web sites**

When the legal battles subsided, the scene of action turned to the World Wide Web for a Health Department Web site listing disciplined doctors, managed-care company sites listing doctors in the networks and the American Board of Medical Specialties' site revealing doctors with board certification.

The healthcare companies and agencies probably never envisioned their Web sites being scrutinized in the manner Maier examined them. From the board-certification site, he found doctors who erroneously claimed board certification in managed-care listings.

From the HMO sites, he didn't find a new doctor, he uncovered disciplined doctors – 132 of them disciplined in New York state in the 1990s.

Using brief descriptions of the disciplinary actions from the Health Department Web site, we created a database of disciplined doctors, including their names, license numbers, addresses, discipline dates and whether the doctors were board certified. We also noted the doctors' offenses, such as patient mistreatment, sexual misconduct or billing errors, and the disciplinary actions, such as suspension, probation or license revocation.

Next, we began to quantify how many procedures these doctors oversaw after they were disciplined, and how much money patients or insurers paid for care overseen by these disciplined doctors.

**Data work**

The hospital admission data contained millions of procedures performed from 1990 through 1998. Using SPSS, we extracted the procedures overseen by doctors disciplined anytime in the 1990s.

That database contained 130,000 records, but only some procedures were performed after the attending or operating physicians were disciplined. We then matched the database with the list of disciplined doctors to uncover procedures performed after the discipline date.

The discipline date field was straightforward. But, as is common with most government data, the database of hospital procedures from the Statewide Planning and Research Cooperative System, which contained the hospital admission date, was quite quirky.

The admission date in the database was divided into three fields: a year, a month, and a day – not a day of the month, but a day of the week.

We wanted to ensure that we only counted patient visits and hospital charges that occurred after the doctor was punished to demonstrate that taxpayer money was being spent on medical care overseen by disciplined doctors. But the unusual format of the admission date presented a problem when a patient visited a doctor in the same month the doctor was disciplined.

So we decided to turn every admission date into the first of the month. If a patient was admitted in November 1998, we turned that into Nov. 1, 1998, using a module written in Microsoft Access and an update query.

Suppose the patient had been treated in November 1998 and the attending physician was disciplined on Nov. 20 of that month. Using Nov. 1, the visit would have preceded the discipline date and wouldn't be counted. We gave the doctor the benefit of the doubt because it was impossible to be more specific about the admission date.

Once we cleared up the date dilemma, we began to calculate the amount of money that the state had spent on managed-care doctors through Medicare and Medicaid.

At first, the task seemed easy – a field indicated the charges. Then came the caveats. The field represented the total cost of the hospital visit, including the room, surgery and payments to the attending and operating physicians and others.

Furthermore, Maier discovered the actual charges to Medicare and Medicaid turned out to be about 60 percent of the total cost.

So we discounted the figures by 40 percent, and could only say that the disciplined doctors "oversaw" the hospital visit, explaining why the data prevented us from determining how much each doctor actually received.

**License problem**

Each procedure record also contained three licenses of doctors associated with the treatment, listing the licenses for the attending, operating and "other" physician.

We chose to use only the attending and operating physicians. Still, multiple licenses for each record presented a quandary.

It's impossible to link the two licenses – one from the attending physician and one from the operating physician – to the one license field in the doctor table.

To explain why, here's an analogy. Suppose I have a lookup table named States that translates U.S. Postal state abbreviations (e.g., State.code contains "NY," "NJ," etc.) into state names, and State.name contains "New York," "New Jersey," etc.

Suppose I have an address book that lists someone's work address and home address, and I want to link that to the lookup table of state names. Suppose further that a friend lives in New Jersey and works in New York.

That state code for the work address, "NY," and home address, "NJ," cannot simultaneously point to the state code in the lookup table for state names. If it did, then what would the field State.name represent: New York or New Jersey?

To resolve that dilemma, add the doctor table to the query twice by clicking twice on the "add" option in the query/show table window. That adds another table called State_2.

To use it, link the home address to the state table and the work address to the State_2 table. Now State.name is "New York" and State_2.name is "New Jersey."

By the way, Access doesn't really create another table. It merely creates another pointer to the same table.

Richard J. Dalton Jr., can be reached by e-mail at rdalton@newsday.com

---

**Following is the Microsoft Access module. To use it, run an update query, replacing the admitdate field with the following: firstdate([admitmo], [admityr]), where admitmo and admityr are the fields representing the month and year of the admission.**

```
Option Compare Database
Option Explicit

Public Function
FirstDate(mCnt As Long, yCnt As Long)
As Date
Dim dCnt As Byte
Dim y2Cnt As Integer
Dim NewDate As Date
y2Cnt = yCnt - 1900
NewDate = #1/1/1900#
NewDate =
DateAdd("yyyy",
(y2Cnt), NewDate)
FirstDate =
DateAdd("m", (mCnt -
1), NewDate)
End Function
```

---

The *Newsday* series, "Managed Care and Doctors: The Broken Promise," is available online at
www.newsday.com/news/doctors/edocs14.htm

The story, and other investigative stories, can also be accessed through the IRE and NICAR Web site list of online investigative projects at
www.ire.org/datalibrary/online.html
