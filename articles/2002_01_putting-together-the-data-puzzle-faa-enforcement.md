# Putting Together the Data Puzzle

**By John Perry, *The Oklahoman***

The Federal Aviation Administration probably deserves an award for creativity in thwarting public access to information. The agency's Enforcement Information System database, which includes information about airport security violations, is publicly available. But the FAA releases only sketchy documentation.

Among the information you can't get: an explanation of the security violation codes. Explaining what those codes mean could endanger airport security, the FAA argues.

After the Sept. 11 terrorist attack, that left newspaper data-crunchers scratching their heads, trying to make sense enough from the enforcement data to evaluate security at their local airports. What exactly is the difference, for example, between security violation code C130, cryptically described in the documentation as "FAIL DETECT – GENERAL" and violation code M140, described as "DETECT – X-RAY." And more importantly, which records represent security failures.

### Data Revelation

The enforcement data is split into four interconnected tables. For those of us looking at security violations, two tables are of primary interest: the main table that contains one record with general information for each case and a secondary table that usually includes several records with security violation codes for each case number.

Another table connects cases to the specific regulation violated, and another gives the action taken by the FAA in response to the violation.

The first thing I did with the files was to run a series of cross tabulations to see which codes in the violator name, violation source, operation type, certification type and employer type fields matched with each other and with the security violation codes.

The first revelation, at least for me, was that the data included not just security lapses by airlines and airports, but also violations by members of the general public — the data recorded not only security lapses, but also security successes.

With only a few exceptions, when the operator type was either passenger or non-passenger, the certification type was "NONE," the violator name was expunged, the violation source was "LOCAL/ST GOVT" and there was an entry in the sex field.

Security codes that matched with the passenger and non-passenger operator type records tended to come from one group of codes, all beginning with an M, that seemed to include things people would get in trouble for: "FIREARM," "EXPLOSIVE," "DETECT – X-RAY," "WEAPON LOADED," "FAILURE TO SUBMIT TO SCREENING."

Crosstabs looking at records where the operation type was "AIR CARRIER" and the violation source was "SURVEILLANCE" or "SPECIAL SURVEILLANCE/INSPECTION" tended to match with security violation codes such as "FAIL DETECT – HAND GRENADE." These were apparently the incidents where FAA inspectors succeeded in sneaking things past screening stations.

But just to confuse things, in almost every case where the operator type was passenger or non-passenger, there was also the name of an airline in the employer field. So were these airline employees?

The FAA wasn't explaining. But the description of the field in the documentation said it included "violator employer *if applicable, or responsible air operator*." Since airlines are responsible for passenger screening, the employer field entries made sense.

### Filling in Blanks

To confirm which records recorded security lapses and which were security successes, I took a clue from the violation source code "LOCAL/ST GOVT" and tried to match the records where the operation type was passenger or non-passenger with our database of local crime incidents.

Our crime incident database goes back to 1992 and is updated monthly by e-mail. The airport is a separate police reporting district to itself, so I pulled all the incident records from that reporting district and matched it with the FAA violation data by date.

In every case, the FAA violations matched with a crime incident record that seemed to match the security violation descriptions.

Our cop reporter pulled the full narrative police reports for the matching incidents, and when we compare the incident narratives with the FAA security violation codes, the data started to make more sense.

For example, a March 26, 2000, security violation in the main FAA table connected with four records in the security code table with the following codes: "DETECT – X-RAY," "FIREARM – HANDGUN," "WEAPON – LOADED" and "WEAPON – CONFISCATED."

The police narrative report said that the X-ray operator detected a handgun in a purse and called airport police. The purse was owned by a Fletcher, Okla., reserve police officer who had forgotten her handgun was in her purse when she came to meet her son-in-law. After a discussion with the FBI, she was released, but the police kept her gun.

The most entertaining incident, however, was coded only as "MISC OTHER" in the FAA data. When asked at the ticket counter if anyone had given him anything to carry on the plane, one man replied, "Just the bomb."

That quip got him a visit with the police and the FBI. He was released to catch a later flight.

John Perry can be reached by e-mail at jperry@oklahoman.com
