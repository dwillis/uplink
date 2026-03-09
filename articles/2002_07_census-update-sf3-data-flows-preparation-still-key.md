# Census Update: As SF3 data flows, preparation still key

**By Jeff Porter, *IRE and NICAR***

The U.S. Census Bureau's early missteps in the summer release of data show that even the agency itself can have trouble with the numbers.

So journalists, beware.

On June 25, the agency began releasing state-by-state Summary File 3 data — from the 2000 Census long form filled out by one of six households — starting with Vermont.

It became clear, though, that the data didn't correspond with a series of specifications or structure tables provided by the Census Bureau for users of Microsoft Visual FoxPro or Access database software. So the information didn't flow in correctly, creating angst for Census reporters. The bureau pulled back the data files, edited the specifications and structure tables then re-released the data on July 5.

Then it happened again. On the day the bureau's embargo was lifted, July 10, the agency reported:

> "We have identified a *potential* problem with the Summary File 3 (SF-3) data files for the state of Vermont that the Census Bureau planned to release July 10, 2002. In accordance with our long-standing commitment to quality, we are postponing the release of all SF-3 files until we know whether any corrections or revisions are required. As we continue our review of these files, we will establish and issue a revised schedule for their release that allows us sufficient time to ensure the data's accuracy."

## A data primer

The data files, finally released and a schedule that now might stretch later in the year than first intended, are massive. All told, the Summary File 3 release includes 813 detailed tables of Census 2000 social, economic and housing characteristics. A total of 484 tables address population; 329 address housing information. Then there's one more: a geography table, simply identifying for each record the level of geography, the name and codes of those geographic areas. For example, it might identify one record as the state of Vermont with the code "50." So that makes 814 tables.

An impossible task? Not at all, in part because of the Access database specifications and the FoxPro and other structure tables that were problematic in the first release but were lifesavers when they were corrected.

First, the Census Bureau combined many of the tables down to a much more manageable collection of 76 data files, plus the geography table. So instead of 814 files to deal with, a journalist can take 77 files and find story after story, either national or local in scope.

## Data, stories galore

Journalists can go back to the Census trough time after time to find or strengthen stories. The Census, after all, is simply counting people, their houses, their dollars. More than just Census stories live in the data. (For specific examples, see the related story in the *Uplink* May-June 2002 edition.)

But before one can pursue a story, one must pick up the data. Since most of the computer-assisted reporting world operates on Microsoft Access, let's focus on that.

To find a Summary File 3 Access 97 database with the corrected specifications, go to *www.census.gov/support/SF3ASCII.html* and download the Access file. If you're using a newer version, you can simply tell your computer to convert the Access database to the correct version.

Now, where's the data? Assuming you have a media password (or if your state's embargo is already lifted) go to *ftp://ftp2.census.gov/census_2000/datasets/Summary_File_3/* for the FTP version or *www2.census.gov/census_2000/datasets/Summary_File_3/* for an only slightly prettier Web interface to download the data.

With a caveat: Even on the late July data release, the bureau erred on the structure of the geography table, which is needed to tie specific Census numbers to a geographic area. Luckily, the geography table structure is the same item used in the earlier releases of Census data, so you can simply download the geography table specifications from the earlier release of Summary File 1 from *www.census.gov/support/SF1ASCII.html*.

## Census files into Access

You'll need to unzip all those compressed files and, if you're an Access user, you might need to rename the text files. They all end with the suffix ".uf3." To change that suffix into ".txt" so that the software will recognize the files, visit the same Web page, where you can review the DOS procedure using the rename command.

Once that's accomplished, you can use the Access database you downloaded earlier with these simple steps (found at *www.census.gov/support/SF1ASCII.html#Microsoft Access procedures*, complete with screenshots).

- Click "File," "Get External Data," then "Import" from menu
- Select text file and click on the "Import" button
- Click on the "Advanced" button
- Click on the "Specs" button
- Select matching import specification and click on the "Open" button
- Click on the "OK" button
- Select option to store data in a new table or in an existing table (then select matching table), then click on the "Next" or "Finish" button. If you choose an existing table, you're finished. That's highly recommended.
- If not, highlight updated table and then click on the Design button
- Right click on field LOGRECNO and then select "Primary Key"

## Finding the geography

The field LOGRECNO is the key way to link to the geography table. That table is important not only because it identifies by name the state, county or tract, but it helps you decide which places to examine and how to add them up. For example, there's a field called GEOCOMP. That stands for "Geographic Component," a number code, which includes not only entire areas such as counties, but smaller areas within a county — the urban area, the rural area, and so on. So if you want to count all the people in a specific county, then you'll want to filter the records to only include GEOCOMP number "00." That's the code to include everything, not specific geographic component types.

To find detailed information on each of those geographic table fields, go to *www.census.gov/support/GeoFile.html* for general information then dive into details at *http://www2.census.gov/census_2000/datasets/Summary_File_3* to download the file "0SF3_geo_header.doc." While you're there, also download and read, if you haven't already, the file "0README_SF3.doc," "0SF3_File_Structure.doc" and "0SF3_table_matrix.doc."

*Jeff Porter can be reached by e-mail at jeff@nicar.org*

---

### readme.txt — Web addresses

In addition to the Web pages listed in the accompanying article, these can help a journalist to understand and use the Census data:

**www.2000census.org**
Investigative Reporters and Editors offers training opportunities, tipsheets and helpful links.

**http://cronkite.pp.asu.edu/census/**
Created by Steve Doig, Knight Chair in Journalism for Arizona State University, who specializes in computer-assisted reporting. The Web site helps journalists and others make good use of Census data.

**www.censusscope.org**
An easy-to-use tool for investigating U.S. demographic trends, from the Social Science Data Analysis Network at the University of Michigan.
