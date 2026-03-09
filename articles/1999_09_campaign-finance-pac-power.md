# Campaign Finance: PAC Power

**By Jeff Porter**
*Arkansas Democrat-Gazette*

Most political action committees are – literally – big business. In our case, the best way to make use of PAC data is "joining" – that is, using a computer to match up material in separate data files. Staff Writer Noel Oman alerted us that for the first time, the Arkansas secretary of state's office could provide electronic data for PAC contributions. The General Assembly was in session — perfect timing for a story. The result was a fairly quick-hit story, written by Oman and accompanied by graphics, for *Arkansas Democrat-Gazette* readers with more details than ever reported about PAC contributions to Arkansas lawmakers.

### Free data

But we needed more information. We obtained data kept by legislative staff, including information on lawmakers and their committee assignments. To their credit, both arms of state government – the secretary of state's office with PAC data and the Arkansas Bureau of Legislative Research with lawmaker information – had no problem handing over the data tables on diskettes. Cost: nothing.

Getting the files was just the beginning. We had to put things together, wanting to accomplish several things. First, we wanted to identify the biggest PAC contributors, so we asked Visual FoxPro to show a total of contributions from each PAC. Instantly, we saw the biggest players. We also examined the top recipients. Thanks to Oman's experience and an electronic file from the secretary of state's office, we could identify PACs related to one another, representing the same companies or business interests.

Now the fun began: trying to match up lawmakers who got PAC money and their committee assignments. This year's legislative session had issues including electric utility deregulation, telemarketing restrictions and highway spending and tax plans. So we wanted to look at both contributors and recipients on key committees.

### Matching PACs to committees

Here's a list of things we did:

First, in both PAC data and legislative membership data, we broke the files in two, creating separate files for each legislative chamber. Why? Because we planned later to match PAC contributions with committee membership tables, using two factors to make the match: the lawmaker's last name and the district number the lawmaker represents. In just a few cases, Senate and House members might have the same last name and the same district number, even though they serve in different chambers.

Next, we took three tables to match up committee assignments to members, using two sets of unique identification numbers – one assigned to committees and the other assigned to legislators.

Finally, we joined the committee files and the candidate files. The committee files identify which legislators are on what committee, and the candidate files identified all contributions to each candidate. Matching both files with last names and district numbers for state senators, we created another file, naming it "sensbig.dbf" – OK, so I'm lousy with file names – that included a listing of each PAC contribution to each Senate committee member. We created another file of House committee assignments and contributions.

That gave us a list showing how much PAC money legislative committee members received from PACs with an interest in that committee's work.

*Jeff Porter can be reached at the Arkansas Democrat-Gazette.*
