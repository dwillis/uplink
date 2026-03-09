# Diagnosing Troop Mental-Health Ills

By Matthew Kauffman
*The Hartford Courant*

When reporter Lisa Chedekel and I set out to examine the adequacy of mental health screening and treatment for troops in Iraq and Afghanistan, we found powerful stories of soldiers and Marines who killed themselves after their mental problems were ignored by commanders. We could have built a series on just those tales, but we were determined to supplement our anecdotal reporting with a statistical analysis in an effort to determine whether there were systemic failures in the military's treatment of troubled soldiers.

We found a possible window in Defense Department Form 2795, the two-page pre-deployment health questionnaire that is supposed to be filled out by every deploying service member. The form asks whether service members have sought counseling in the past year, and that single question is the foundation of the military's mental health screening process. The form also indicates whether a referral to a mental health professional was made, and whether the service member was ultimately deemed deployable.

Three million of those questionnaires have been filled out since 1993, most – unfortunately – on paper. But we discovered that every one of those pre-deployment forms gets sent to an office in suburban Washington and entered into a database.

It is all stored in something called the Defense Medical Surveillance System, a massive database – 300 million rows – chock full of data protected under the federal Health Insurance Portability and Accountability Act. But, for researchers, the military maintains a separate database that has been stripped of identifying information.

It's all available to registered users at *http://amsa.army.mil/DMED_Items/DMEDOverview.htm*.

It was a gold mine. But getting access to it wasn't going to be that easy.

My application for online access was rejected. And when I contacted an official at the U.S. Army Center for Health Promotion and Preventive Medicine, which oversees the database, I was told the data is available only to Defense Department personnel.

Citing the online user's manual for the database, I noted that it was supposed to be "available to all military and civilian researchers, policy makers and others with a need to evaluate the health of active duty service members."

Surely that applied to me, I argued. But my definition of "need" apparently differed from the military's. The answer was no.

But they also made an unexpected offer: While they were still refusing to give me unfettered access, they agreed to query the data and give me the results.

I still believed I was entitled to the raw database, and I wasn't thrilled about tipping my hand, fearing that making it obvious I was focusing on mental health might lead to the sudden withdrawal of their offer. But I was quickly seduced by the prospect of getting some numbers without an endless court battle that undoubtedly would have dragged on well past our publication date.

So I took them up on the offer, asking for data, aggregated by month, which would provide counts of the various permutations of three yes-or-no questions: had service members marked that they had sought counseling, were they referred to a mental-health professional, and were they ultimately deployed. I asked for data going back to March 2003 – the launch of Operation Iraqi Freedom – though I later came to wish I had gone back farther.

There were other data I would have liked, which would have allowed us to analyze any statistical differences among the branches of service, or among different military ranks. But in the end, I decided to stick with what amounted to a single, short line of SQL code that would yield a table with fewer than 400 records, hopeful that that simple request would be impossible for them to refuse.

I made the request in September 2005, two months after I began negotiating for access to the data. Had I been able to query the data online, I would have had it in seconds. I figured it would take the military a couple days to get around to running the query.

Six weeks (and a lot of prodding phone calls later), I was still waiting, and began to assume I would never see the numbers. But I kept pushing, and one day in November, a modest Microsoft Excel spreadsheet arrived by e-mail, offering a first-ever window into the military's pre-deployment mental health screening.

It took four months of wrangling – not too bad when negotiating with the military – and it was definitely worth the wait. Although the file was small, I imported it into Microsoft FoxPro database manager so I could work with the data more easily. Every way I viewed the data, the results were astounding.

We found that since the start of the war, fewer than 1 in 300 service members was referred to mental health professional, despite a 1997 law requiring that the military assess the mental health of all deploying troops.

Even among troops who said they had sought mental health care in the past year, just 6.5 percent were sent for an evaluation before being deemed mentally fit for war.

In addition, despite the military's promises to pay closer attention to the mental health of service members following a spate of suicides in 2003, we found that soldiers who reported psychological issues were more likely to be deployed in 2005 than at the start of the war.

The numbers ratcheted up our comfort level that we had found systemic problems and not simply a cache of compelling anecdotes. And the statistics were widely cited in post-publication reporting on the series and were picked up by legislators pressing for reforms.

"The law is not being followed as it was intended," Senator Joe Lieberman testified in support of a bill that would expand pre-deployment screening. "Alarmingly, the *Hartford Courant's* investigation found that only 6.5 percent of those indicating mental health problems were referred for mental health evaluations from March 2003 to October 2005. This is unacceptable."

The legislation, added to the Defense Authorization Bill, requires the military to go beyond a single screening question and also assess a service member's mental health history and any current symptoms, treatment or psychotropic drug use. The bill also mandates that service members who show signs of a mental health disorder must be referred to a qualified health professional before they are deemed deployable.

Getting these numbers did not require any heavy-duty analysis or sophisticated programming; it only took simple queries to evaluate the relationships (and the relationships over time) between three fields. But there are basic lessons worth repeating for those who do computer-assisted reporting.

Routinely look for data – the government's got loads of it, as do other institutions – to add a broader statistical element to your stories. And don't listen to the voice that says an agency will never, ever cough up the data you're seeking. Pursue it – creatively, doggedly. If you get it one time in 10, it's worth it.

Contact Matthew Kauffman by e-mail at MKauffman@courant.com.
