# Atlas GIS has site: Get mapping data on-line

**By Dan Keating**
Miami Herald

Even after you spend hundreds of dollars, you won't find detailed local maps in your brand new mapping program.

Most of the mapping companies will be glad to sell them to you for hundreds of dollars more.

Atlas GIS users are in luck, because there's an online repository that has tons of detailed maps and matching data. It's called CIESIN (pronounced see'-son), Consortium for International Earth Science Information Network.

(Unfortunately, MapInfo doesn't import the mapfile format used at CIESIN).

For your area, you can find census tract maps, block group maps, block maps, county maps, municipal boundaries and Zip code boundaries. You can also find 1990 Census data broken into the same groupings with ID labels already matched up to the maps. It has the 225 most-requested variables.

### How to get information

Here's a detailed breakdown on how to get this free information into your system.

Log onto the CIESIN file transfer site at ftp://ftp.ciesin.org. (You can check out the Web page, also, at http://www.ciesin.org, but the data is on the ftp site.)

Go to pub/ and then census/ and then USA/ You need to pick up map files and then get matching data files.

Go to tiger/ and then pick your state from the two-letter abbreviation. If you do not know the Census code for your Metropolitan Statistical Area, you should pick up msacodes.txt from the tiger/ directory before moving on.

Once in your state, take bna_st/ to get local area maps files. The "bg" files are block group maps — these are the smallest detail area that also has vast demographic information. If you're working with large areas, you can use the "t" tract or "c" county files for the state. I find the block group files extremely useful. Download the file for your MSA. You'll get a PKZipped file. We'll get back to that file in a minute.

If you want the smallest geographic level, take the bnablk/ directory instead of bna_st/. Download the "b" block file for your MSA. These are for very small areas, for which you can get population and household counts, but no detailed demographic data.

Now you have to get the matching data. Back up through the ftp site back to pub/ census/USA/. Now take stf/ and pick your state. Then get the "CONTENTS.XX" file, in which "XX" is the two-letter abbreviation for your state. It will help guide you to get the correct data files. There are "bg" block group data files, "tr" tract data files, "zip" Zip code area files, "pl" files with data for cities and other places and more. If you need the population counts for blocks, go to the csvblk/ directory and get the file matching the map file you got.

Download whatever files you need to match the geographic files you got. These will be PKZipped csv files — meaning the data is separated by commas. Most spreadsheets and databases can import these files, as can Atlas GIS.

Now you can sign off the Internet.

### One special tool

You'll need one special tool to be able to import the maps. It's called Import/Export or I/E and costs about $250 from Strategic Mapping. That's expensive, but it's a lot cheaper than buying the maps. It also allows you to import many other map formats, which you might come across if you try to get data from your county GIS department or other agencies.

Put the PKZipped files into a directory. Unzip them. You'll have *.csv data files and *.bna map files. BNA is the Atlas transfer format.

At a DOS command line prompt, go to the directory where you have Atlas GIS and use the command line "ie mapfile.bna mymap.agf/na 4".

Import/Export will create the geographic maps for Atlas GIS. You can then open the maps in the program and then open the .csv files. The program will ask if the data files can be linked to the maps, and ask which field in the data file to use for matching. Select the "POLID" field except for the block groups, which should be linked with the "_Name3" field.

Now you've got detailed local maps for whatever geographic area you want, along with a mountain of demographic data.

Dan Keating can be reached at (954) 985-4571, or send e-mail to dtkeats@ibm.net
