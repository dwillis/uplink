# Adding Numbers: Minority Teachers Missing

**By Griffin Palmer**
*The Daily Oklahoman*

Data analysis doesn't have to drive an education story. Sometimes it can be a nice augment.

When reporters Susan Parrott and Melissa Nelson-Varela began preparing a feature about the State Education Department's efforts to recruit minority educators, I reached for two data sets I already had. One was a racial breakdown of Oklahoma's student body. The other was a racial breakdown of certified educators.

The analysis turned up some surprising numbers that helped shape the story: The greatest discrepancy in numbers between student body and educators was not among blacks, but among Hispanics and Native Americans. Before the analysis, Susan and Melissa had instinctively been focusing mostly on black students and efforts to recruit more black teachers. Our analysis showed them they needed to focus more on other racial minorities.

The analysis wasn't terribly complex, but we did have to be careful to select comparable groups from both databases. The State Education Department's student racial breakdown includes students enrolled at private schools, while the educators' database does not include those working at private schools.

The enrollment data documentation warned that students enrolled in bilingual programs were counted twice, a fact that we also had to account for before we could do our analysis correctly. Unlike the U.S. Census, the state data counted Hispanics as a distinct ethnic group and not as a subset of other racial groups.

To make sure we were comparing like groups, we needed to select only those cases from the student enrollment file that contained data for districts included in the educators' file. The tables' design made this challenging.

In the student file, each record indicated a grade in a particular school. Each record contained columns listing number of class members by race and by gender. The educators' file contained a single record for each teacher or administrator, with a field denoting the individual's race.

Each of the files listed district numbers many times. In the enrollment file, district number occurred in each grade. In the educators' file, district number occurred in each individual's record. Doing a straight relational join in this situation would result in thousands of duplicate matches. A simple nested query, in FoxPro, allowed us to find only those districts appearing in the educators' file and to filter out the duplicate numbers from bilingual enrollments.

The tables were called enroll96.dbf and edcert96.dbf. The join field was called district. Any time the grade field in the enrollment table contained the string 'BI', it was duplicate information that had to be eliminated. Here's how the query looked:

```
select * from enroll96 where grade <> 'BI';
and district in (select district from edcert96);
into table public96
```

We now had a table giving us enrollments only for public school districts, and could make meaningful comparisons between the racial distribution among certified educators and the racial makeup of the student body.

We knew that Oklahoma City and Tulsa, the state's two largest, most urbanized districts, would have sharply different racial makeups than the rest of the state, so we analyzed them separately. In fact, we broke the data into four separate groups, based on size of enrollment. Our analysis showed, however, that only Oklahoma City's and Tulsa's racial makeup differed significantly from the makeup of other districts.

Our analysis showed that blacks made up 36.6 percent of students in Oklahoma City and Tulsa, while blacks comprised 21 percent of the two cities' educators.

In the rest of the state, blacks made up 6.6 percent of students; less than 2 percent of teachers.

American Indians comprised 6.4 percent of the urban student bodies and 2.3 percent of the urban districts' educators. In the balance of the state, the discrepancy was more stark: 16.3 percent of students and 3 percent of educators were American Indian.

Similar discrepancies showed up for Hispanics. The ratio of Hispanic students to educators was 9.2-to-1 in the urban districts.

The data analysis contributed only a few paragraphs to a 85-column-inch story. It lent authority to the story, though, and helped shape its lead.

*Griffin Palmer can be reached at (405) 475-3311 or send e-mail to palmer@qns.com.*

*Attending NICAR's bootcamps can help you add weight to deadline stories or to do investigative series. The bootcamps offer one week of intensive training. For more information, call Wendy Charron at (573) 882-0684.*
