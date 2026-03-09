# Separate and equal?

**By Doug Haddix and Bill Bush**
*The Columbus Dispatch*

Like many government offices, the Columbus school district maintains its electronic records in a mainframe computer system that makes it nearly impossible for outsiders to analyze.

Information is kept on separate tables that can be linked only by a confidential field such as student identification number or teacher Social Security number.

The moment we saw the record layouts for the district's master student file and master employee file, we saw red flags. Those databases, we realized, would play a pivotal role in the newspaper's investigation into whether the return to racially segregated schools in Columbus had produced unequal opportunities for poor and minority students.

### Glaring inequities

The four-day "Dividing Lines" series, published in June 2000, uncovered glaring inequities among the district's 88 elementary schools. Those findings came despite a school board policy approved four years earlier, promising that the end of cross-town busing would not produce separate and unequal schools.

Seven weeks after our request for the district's master files, we finally obtained the electronic data in a usable format – but only after finding a smoking gun in Ohio law.

At four separate meetings with the school district's data crunchers, we repeated our request that programmers randomly generate a unique identifier for each of the 65,000 students and 11,000 employees. We assured district officials that we had no interest in identifying particular students or obtaining Social Security numbers of any teachers, principals or administrators. We simply wanted to be able to link the district's 19 separate data tables.

Without a link, for instance, we had a table that included teacher salaries but not their names, which were kept in a separate file.

Six weeks after our initial data request, the district provided its master student and employee tables on a CD-ROM, complete with a nifty jewel case cover. The only problem: no unique identifiers. The tables were useless.

We scheduled a fifth meeting with top district officials to press our case. The day before the meeting, we discovered through a source in the Ohio Department of Education that all public school districts are required by law to generate a unique student identifier when they submit data to the state.

Armed with that ammunition, we met with the district's top brass. Immediately, they agreed to provide the data with a randomly generated identifier created just for *The Dispatch* – the missing link we needed. Without that discovery, we might have been forced into taking legal action. Ohio's public record law sets no firm deadline for completing requests; it merely requires public bodies to make records available in a "reasonable" period. It took the district another week, however, to turn over data that it had maintained all along.

---

**Seven weeks after our request for the district's master files, we finally obtained the electronic data in a usable format - but only after finding a smoking gun in Ohio law.**

---

Once the district's usable master student and employee tables arrived on a new CD-ROM, we did a bit of tedious work to move the 57 MB of data into a Microsoft Access database. The 19 tables had an unfamiliar ".JUN" extension, so we saved them as flat text files, then moved them into Access.

We used the advanced import function to save the import specifications. That saved a lot of time because we had requested master files for the last year of cross-town busing (1995-96) and the most current data for the return to neighborhood schools (1998-99). It took about 20 minutes to type in the import specs for each table for 1995-96, so saving them slashed the import time for the 1998-99 tables. In addition, the saved specs will make it faster to import data for subsequent years, provided that the data fields don't change.

Because the Columbus district moves slowly on requests for information, we filed simultaneous data requests with the Ohio Department of Education, which maintains information on the more than 3,600 public schools across the state data.

---

**The judge who originally ordered desegregation of Columbus schools in the 1970s termed the new zones "curious."**

---

While not as extensive as the Columbus district's master files, the state data gave the project team helpful information on enrollment, per-pupil spending, proficiency test scores, median teacher salaries and other topics that we could query by individual schools and by district.

Unlike the Columbus district, the Education Department responded with amazing speed, sometimes e-mailing Microsoft Excel spreadsheet files to us within hours of a request. The school district maintained it didn't have the staffing to provide information that quickly.

To get the fullest picture possible of changes in Columbus elementary schools since the end of busing for integration, we obtained from the district and analyzed several other types of data:

- **Student school assignment records.** We received one of those "you can't get there from here" responses from the district when we first asked for records showing Elementary Attendance Zones, which are geographic boundaries that determine each student's "home school."

First, the district provided a huge paper file that included an elementary-zone breakdown of the number of students living in each assignment area, their race, their gender and the school they attend. In Columbus, students can attend their home school or try to transfer to another school through a lottery.

With 65,000 students to track, the paper files were useless for analysis because of their size. In a bizarre twist, the school district official who created the paper report maintained that he did not keep it electronically; rather, he insisted, he printed the report and then deleted the electronic version from his PC. (Don't ask.)

After some wrangling, we were able to obtain the underlying records to recreate a version of this report ourselves using a Microsoft Access database. We obtained an electronic database in which each record represented a student; each record contained demographic information, as well as that student's "home school" and the school the student actually attended.

Because we had data for the last year of cross-town busing and for the most recent year of neighborhood schools, we were able to analyze changes in the assignment boundaries for elementary schools. Those attendance zones, it turned out, were being grouped together in many cases along racial lines.

The judge who originally ordered desegregation of Columbus schools in the 1970s termed the new zones "curious." One school assignment plan formed a sideways L, picking up predominantly white neighborhoods while avoiding minority neighborhoods. Another linked white neighborhoods that were separated by a railroad switchyard and a freeway, again avoiding adjacent black neighborhoods.

- **Uniform school accounting system database.** This huge district database tracked dollars by various expenditure codes by building. That allowed us to analyze how much money was actually flowing to schools with different racial and economic compositions, and how those funds were being spent. Among other uses, we were able to gauge a school's ability to raise money through parent-teacher groups.

- **Free and reduced-price lunch program participation by school.** For whatever reason, neither the state nor the district kept this information in computer form. The district's food services office maintained paper records, which we entered into a Microsoft Excel spreadsheet. We linked that table using the school building identification number to other data tables so that we could explore the relationship between student poverty and items such as test scores, per-pupil spending and teacher experience.

In addition to basic spreadsheet and database analysis, the newspaper used GIS mapping software to look for geographic patterns involving the 88 elementary schools. Seeing the data on a map helped us spot several important changes, most notably the concentration of less-experienced teachers in certain schools.
