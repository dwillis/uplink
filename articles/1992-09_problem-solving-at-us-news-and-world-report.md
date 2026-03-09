# Problem Solving At U.S. News and World Report

**By John Bare**
Ph.D. candidate at the University of North Carolina-Chapel Hill

U.S. News and World Report's summer plunge into computer-assisted reporting illustrated a multi-method approach to problems encountered in working with the Food and Drug Administration's Medical Device Reporting system.

As an intern hired to help develop computer-assisted reporting projects at U.S. News, I worked with section editors, senior writers, associate editors and administrative staff. The magazine's library and its corporate data services division devoted substantial resources to computer-assisted reporting projects.

In addition to the magazine's standard word-processing system, ATEX, I used Oracle version 6.0 with SQL Forms, SPSS/PC+ version 4.01, WordPerfect version 5.1 and Lotus 1-2-3 release 3. An AST 386SX/20 connected to a VAX mainframe by an ethernet network was set aside for computer-assisted projects.

The result was "Danger: Implants" (Aug. 4, 1992), a six-page story in the News You Can Use section. Using the MDR computer tapes, U.S. News examined five medical devices set to undergo regulatory scrutiny next year. U.S. News devoted the most attention to penile implants, combining traditional reporting techniques with more scientific methods.

The magazine's corporate data services division loaded the MDR tapes onto the VAX and created a database using Oracle. From my personal computer, I was able to log on to the VAX in just a few seconds. Using Oracle, I could retrieve selected records, sort by fields and produce reports that could be imported into other software packages for additional analysis.

Soon after obtaining the FDA tapes, however, we discovered a major obstacle. When records were sorted by accession number (the MDR equivalent of identification numbers) and product code, the report revealed several problems, including thousands of duplicate records. An FDA programming error had rendered the tapes virtually useless. More meetings with the FDA were scheduled to resolve the problem.

The one thing we learned from the tapes is that key information contained in a text field cannot be sorted. The MDR's massive "event description" field consists of a text paragraph composed by data entry personnel that describes how and why the medical problem occurred.

**THE ONE THING WE LEARNED FROM THE TAPES IS THAT KEY INFORMATION CONTAINED IN A TEXT FIELD CANNOT BE SORTED.**

With penile implant reports, for instance, the patient's age (if listed at all) is in the event description field, as is the date of the implant operation and the details of the medical device problem. Because this information is buried in a text field, we could not instruct a database program to sort the penile implant records by patient age, implant date or problem type.

Even worse, the form in which the MDR information is archived is inconsistent. The event description field may say that the penile implant patient is 42 years old, or it may say that he was born 8/12/50. One entry might describe the problem as a "leak." Another might say "lost fluid." Still another might say "leakage from reservoir." An implant might protrude, extrude, erode or break the skin. This haphazard style of reporting device problems made it difficult to devise a surefire method of dumping the event description paragraphs into a text analysis or word processing system for more detailed analysis.

So just as social scientists use multiple methods to tackle tough problems, we added another prong to the computer-assisted reporting task. While waiting for a new set of accurate MDR tapes, we completed an old fashioned, hand-coded content analysis of penile implant problem reports, using a sample of 1,196 implant records drawn from microfiche copies of the MDR tapes. We recorded product names, manufacturer names, the report description (death, serious injury or malfunction), report date, date of implant and patient age. In addition, we established nine categories of problems and coded the reports accordingly.

Data from the code sheets were keypunched into Lotus and then imported into an SPSS system file for statistical analysis. With the push of a button, we could find out things such as 8 percent of the penile implants involved infections and the average age of patients with penile implant problems is 56.

By subtracting the implant date from the MDR report date (SPSS "compute" command), we created a variable of the number of years between the implant operation and the problem report. The distribution ranged from zero years (implant and problem in same year) to 16 years but was skewed heavily, with about 62 percent of the problems occurring within three years of the implant date.

By this time, new MDR tapes arrived, and integrity checks indicated that there were no problems. The tapes contained approximately 176,000 medical device problem reports from 1984 through mid-June 1992. Of these, 8,064 records were singled out as penile implant problem reports.

In our continuing effort to cull from the event description field information about why the implant problems occurred, we created separate Oracle reports for each of the 13 penile implant models cited most often in the MDR tapes. The reports contained the full text of the event descriptions.

A macro WordPerfect program was written to search for terms and count frequencies. We counted the number of times such terms as "leak," "lost fluid" and "infection" appeared in the event descriptions. As explained earlier, the FDA's inconsistent reporting style makes this sort of measure imperfect. Here, however, the method served as a backup check to the hand-coded content analysis sample.

Another check came from the FDA, whose analysts are able to sort medical device problems by categories. U.S. News obtained FDA analyses of problem types for the 13 penile implants most often. Because the FDA's system did not always fit our needs, it was not desirable to rely solely on FDA data, but again it was a valuable check.

This multi-method approach produced three sources of information regarding specific types of penile implant problems: the content analysis of 1,196 records, the frequency counts from WordPerfect and the FDA analysis. From this we produced a box that ran at the close of the story listing the most common problems associated with various models of penile implants.

For media such as U.S. News that are just starting to utilize computer-assisted reporting techniques, the road to completing projects is filled with an endless string of potholes. As crucial as it is for reporters to narrow their research question and devise an effective methodology, it is just as important to be able to react positively when glitches occur. Whether or not such projects ultimately succeed depends in large part on the willingness of the news organization to assemble a team of players flexible and creative enough to solve the problems they could not have foreseen. For U.S. News and other media that have moved past discussing computer-assisted reporting ideas and actually produced publishable work, they now face new challenges. They must educate editors and reporters about the advantages of computer-assisted methods, provide year-round in-house training and make computer-assisted reporting techniques part of their daily routine.
