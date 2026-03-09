# Databases add depth to pool stories

**By Mike Sherry, *IRE and NICAR***

It's a good bet your news organization will soon be doing the quick-hit pool opening story. Why not add depth to an otherwise shallow story?

You can do that – and many other stories – with U.S. Consumer Product Safety Commission (CPSC) death and injury data. The data should be manageable for anybody with a basic knowledge of software such as Microsoft Access, and you can get a decade's worth for free.

Along with swimming pools, the data include incidents involving thousands of other consumer products – from air conditioners to vacuum cleaners.

## Pool problems

Many of your readers, viewers or listeners might not realize how dangerous swimming can be.

Of the more than 44,000 deaths included in CPSC data running from January 1990 to October 2001, more than 5,300 records cited swimming pools as the main product involved with the death. Other oft-cited products include bathtubs and showers and stairs and steps.

Swimming deaths increase when slides and other related products are taken into account. One entry in the database – which is compiled from state health department records – details the September 1998 death of a 3-year-old girl in Tampa, Fla. She died after tumbling from a pool slide, hitting her head and falling into the water. The table's four narrative fields provide a detailed account of the incident.

CPSC's codes even get as specific as categorizing deaths related to pool chemicals (product code 938). The death database includes eight instances – in states as diverse as California, New York and Wisconsin – where pool chemicals contributed to a death. In one incident, a 66-year-old Cocoa Beach, Fla., woman died after inhaling chlorine fumes.

> From January 1990 to October 2001, more than 5,300 records cited swimming pools as the main product involved with the death.

## More than death data

The death database is just one of four CPSC provides with data compiled in the 1990s. (Data going further back is available, but it is likely to cost you and take longer for CPSC to provide). Also available are:

**National Electronic Injury Surveillance System (NEISS).** Record Count: 3,228,474. Conducted for nearly 30 years, the survey currently collects reports from 100 hospitals nationwide. This survey is considered a representative sample of emergency rooms, allowing the CPSC to estimate the number of injuries caused each year nationwide by products. The commission makes these estimates available – in paper format – through its annual "Product Summary Reports." For example, the 2000 summary estimates there were 80,110 swimming pool-related injuries that year. The 2001 summary report should be available from the commission in June or July.

CPSC periodically alters its sample to account for hospital closures and other similar changes. The last change was in 1997. Yet, CPSC statistician Tom Schroeder said the commission's annual estimates could be added together for a historical account of injuries caused by a particular product. For instance, it would be OK to add up the CPSC estimates for swimming pool injuries for each of 10 years and report the number of injuries for the entire decade.

One caution, however; CPSC explicitly warns against saying these products "caused" the injuries. The commission says emergency room information only tells the products that were "related" to the injury.

**Injury/Potential Injury Incident File (IPII).** Record Count: 222,396. This file contains summaries of reports to the agency's hotline, newspaper accounts, reports from medical examiners and letters to CPSC. Helpful fields in the database include whether the injury was work-related, a general description of the cause (such as an explosion or fall), and the outcome of the hospital visit (such as if the person was treated and released, or dead on arrival).

**In-depth Investigations (INDP).** Record Count: 46,420. This file contains summaries of investigations into product-related injuries or incidents. According to the CPSC, these investigations are prompted by information gathered for the NEISS or incident tables or through a separate initiative by the commission. Helpful fields in this database include the body part injured and injury diagnosis (such as poisoning or drowning).

Like the death data, the narrative fields are one of the best features of these three datasets. Additionally, the IPII and INDP tables include the city and state where the incident occurred. Given that the NEISS is just a sample, it does not include state or city fields.

The incident and NEISS tables can be linked with the investigation table through a unique identifier known as the task number.

## Data documentation

Some of the key documents for these datasets are readily available on the Web. Those include an overview of the NEISS database (www.cpsc.gov/cpscpub/pubs/3002.html) and information about obtaining the databases (www.cpsc.gov/about/clrnghse.html).

Also available is the very useful "Product Code Comparability Table" (www.cpsc.gov/Neiss/jove-asp/default.htm), which documents changes in product codes throughout the years. For instance, from 1972-1978 the CPSC used code "1220" for swimming and water sports equipment. But, from 1978 on, it split that code into three more-specific codes – such as "3276" for water polo.

However, the record layouts sent with the data were not great.

Problems included field names that were out of order or were not in the database at all. When Investigative Reporters and Editors and the National Institute for Computer-Assisted Reporting obtained the data, we had to call the CPSC for a code sheet called "Interpretive Sheet for Computer Printouts of Reported Incidents." You should make sure you request this with the data, since it contains codes that help decipher some of the fields.

Finally, the CPSC agreed to resend us the data with updated record layouts and code sheets.

The CPSC originally sent the databases in a text format (delimited by "|") that imported easily into Access. If you ask, you should be able to get the data as an Access database or as a .dbf. The NEISS dataset came as four separate text files; the other three databases came as three individual text files.

## Data come with caveats

When dealing with the age fields, keep in mind that CPSC uses a three-digit convention for children under the age of 2. For example, a child that is 23 months old is listed in the data as "223." Obviously, you'll want to keep this mind if you're calculating average or median ages, since the age cited in the example would be read as a person who is 223 years old.

Each of the four databases includes multiple product fields. For instance, the NEISS has "Prod1," "Prod2" and "Prod3" fields. This *does not* mean that Prod1 was the main product involved with the injury and that the other two were involved to a lesser extent. The fields just tell which products were involved with the injury or death.

*Mike Sherry can be reached by e-mail at mikes@nicar.org*

---

### For more information

*The IRE Journal* May-June 2002 edition offers detailed articles about consumer affairs reporting.

**Resources**

Tipsheets and stories from the IRE Resource Center can assist journalists working on similar stories.

**Story #9182**
Inside Edition (New York) shows how the swimming pool industry's own minimum standards do not prevent paralyzing injuries when an adult dives from a diving board into a backyard swimming pool.

**Tipsheet #1122**
This tipsheet, by Arnold Diaz of ABC News *20/20*, lists sources and Internet addresses for consumer groups, medical sites, journalists' tools, and consumer law and government agencies.

To order, call 573-882-3364 or go to www.ire.org/resourcecenter and search with the keywords "consumer affairs."

**Ordering data**

The U.S. Consumer Product Safety Commission (CPSC) databases are available from:

U.S. Consumer Product Safety Commission
Clearinghouse, Room 504
Washington, D.C. 20207
Telephone: 301-504-0424
Fax: 301-504-0025

**Web address**

You can search the CPSC's National Electronic Injury Surveillance System (NEISS) database at www.cpsc.gov/neiss/default.html
