# Law creates shortage

**By Russell Clemings**
*Fresno Bee*

With tax revenues rising and a state law requiring a fixed percentage to be spent on education, the California Legislature five years ago reduced class sizes in three primary grades from an average of more than 30 to a maximum of 20.

Almost overnight, California's elementary schools created more than 25,000 new classrooms and hired a like number of new teachers. The result was a statewide teacher shortage that persists to this day and which has burdened low-income and rural schools with large numbers of underqualified teachers.

In December, the *Fresno Bee* analyzed five years of teacher census data. We determined that, for the poorest one-quarter of California schools, the teacher shortage – as measured by the percentage of teachers working without a full credential, the basic teacher license – has grown worse each year since class-size reduction began.

---

**The PAIF data is derived from an annual teacher census. Each record includes details about a single teacher, such as education level, credential status, experience and demographic background.**

---

Throughout the state, schools that have trouble competing in a tight teacher market are relying on ever-larger numbers of teachers on temporary permits, internships and waivers – teachers who, in a normal market, would never be hired.

The data came from the California Department of Education's Professional Assignment Information Form and CalWORKS Children/Meal Programs databases.

The PAIF data is derived from an annual teacher census. Each record includes details about a single teacher, such as education level, credential status, experience and demographic background. Data on teacher assignments is also included. The CalWORKS/Meals database contains demographic information on each school's students, including the percentages on welfare or receiving free or reduced-price lunches.

Personal identifiers are either not collected or purged from the public data releases, so it's not possible, for example, to track an individual teacher's movements. But the data does provide rich detail on populations of teachers and students at the individual school and (for teachers) grade level.

Many states collect similar data, and the National Center for Education Statistics (*http://nces.ed.gov*) has nationwide datasets and surveys covering some of the same subject matter.

Much of the California data was available online at the department's Web site, *www.cde.ca.gov/demographics/files/paif.htm*, for the most recent PAIF data and *www.cde.ca.gov/demographics/files/afdc.htm* for the welfare/meals data. The California Department of Education provided the two earliest years of PAIF data at no charge on nine-track tape.

Collating and analyzing the data was not easy. Midway through the five-year period, the structure of the PAIF data changed from a flat file with room for multiple assignments for each teacher to a relational database with a flat file of teacher records linked to a table with one or more assignment records for each teacher.

Additional reference tables were needed to translate assignment codes into English terms such as "self-contained first-grade classroom." And in determining which assignment codes to use and how to define credentialed and uncredentialed teachers, studies from the state Class Size Reduction Consortium (*www.classize.org/*), the Public Policy Institute of California (*www.ppic.org/*), and the Center for the Future of Teaching and Learning (*www.cftl.org/*) were invaluable.

It took a 290-line FoxPro script and a week of work to reduce the disparate databases, which totaled more than 400 megabytes, to a manageable flat file of 6,295 records, one for each California school that had at least one teacher in a self-contained elementary classroom.

Each record in that table contained five years of data, and for each year there were five data fields: (a) Percentage of students on welfare, (b) Percentage of students on free/reduced price lunches, (c) Total teachers, (d) Fully credentialed teachers, (e) Less-than-fully credentialed teachers, and (f) Teachers for whom no credentialing information was available.

We published tables with the local data, and our Web designers created a searchable interface for the entire state table at *www.fresnobee.com/man/projects/teachers*.

Statewide, a simple line graph told the story. For the wealthiest one-quarter of California schools, the proportion of uncredentialed teachers rose from zero in 1995-96 to 5 percent in 1999-2000. In the poorest schools, the proportion rose from 3 percent to 23 percent over the same five-year span.

### Reaction

"No one intended for the poorest schools to have the least-qualified teachers, but that seems to have been the effect" of class-size reduction, one researcher said.

Class-size reductions have been an undeniable boon for most California schools. Test scores are rising, pupils are getting more individual attention, and parents are pleased. But for those schools that can't compete in the tight teacher market, the data shows a decidedly bleaker situation.

Russell Clemings can be reached by e-mail at Clemings@cris.com
