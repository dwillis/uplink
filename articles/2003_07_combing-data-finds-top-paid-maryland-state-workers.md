# Combing through data finds top-paid workers

By Hanah Cho
*Los Angeles Times*

The story was supposed to be simple. My task was to update a 1990 analysis by Capital News Service, a wire service operated by the University of Maryland, examining the highest-paid public employees in the state. The analysis then found that the highest-paid state employees were mostly white and male and came primarily from the academic world, particularly from the public medical schools.

After preliminary research and interviews, I determined that state employee salary data in Maryland would come from two sources – the state Office of Personnel Services and Benefits, and the University System of Maryland. (Looking back, after attending a NICAR Boot Camp this year, I also should have contacted the state comptroller's office for salary information.)

I didn't have much time, maybe about two months, to finish the project. So, after pinpointing the right contact person at each agency, I immediately filed public information act requests with both agencies. I was very specific in my request and asked for a number of items, including the top 100 highest-paid employees, names, salary, job title, department, gender and race, even though I was unsure I would get the latter because race may be considered private information. I also asked for the information in electronic form, such as Excel or Access. If I had had more time, I would have requested the agencies' complete payroll database so I could perform a more extensive analysis.

The university system complied with the request within weeks, providing the information in an Excel spreadsheet at no charge. The state Office of Personnel Services and Benefits wasn't as efficient or quick. The agency's lawyer argued that my request would essentially create new records, since it would require the agency to reprogram its database – something that's not required under the public information act. The lawyer also argued that my request imposed a burden on the agency because it would require extra work.

The lawyer was strict in her interpretation of the law, while I believed the law left room for negotiation. For example, Maryland's open records act ultimately leaves the choice of format up to the agency. However, the law also urges the agencies to voluntarily agree to the requester's choice of format if it does not require much work or significant cost. I knew my request would take a simple query or two, especially since the university system appeared to have no problems with it.

### I found that the database did not tell the complete story.

So the lawyer and I wrangled back and forth on the law's intent. As the last straw, I put our position in writing to the lawyer as well as to the Maryland state attorney.

Meanwhile, I began analyzing the university employees' data, a table that included all the requested fields except race. The seven columns had the last name, first name, salary, title, department, university and gender. The first thing I did was make a copy of the database, a point that was drilled into my head by my computer-assisted reporting professor, who warned of the dangers of working off the original file. And, although the database was fairly clear, I ran an integrity check to see that there were in fact 100 rows representing the 100 highest-paid employees and whether there were any null fields.

I found discrepancies in how the names of departments were entered into the database, a quirk that I had to straighten out. I manually typed in the full name of departments by individually going through the department fields, because at that point my query skills were pretty basic.

After that, I imported the file into Access to run some queries, such as group by department and gender and count. I noticed something immediately. The University of Maryland men's football and basketball team coaches – Ralph Friedgen and Gary Williams, respectively – appeared quite low on the list, even though the media had reported that they make salaries in the millions. So I inquired about the coaches' contracts. But the university's athletic department refused to disclose contract details, arguing that the university was required only to release state-funded salaries.

Yet the state law makes it clear that bonuses and performance awards, which Friedgen and Williams most likely received, are considered public. So I filed a public information request even though I wasn't sure I would get the information before my story deadline. My editors also talked to the lawyer.

About a month before my deadline, the state finally relented and gave me its top 100 highest-paid state employees in the form I requested. After the databases were combined (which I did manually by copying and pasting, since most of the highest-paid employees came from the university), it was easy to see that the highest-paid employees came mostly from the—

*continued on page 16*
