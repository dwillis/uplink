# Fitted for publication

**By Carl Neiburger**
*San Jose Mercury News*

It's great to be able to use a GIS program to turn data into a map that you can display on your computer screen, but it's much nicer to be able to share the results with your readers.

Unfortunately, the process of turning a viewable GIS map into a publishable map is anything but easy. It is possible, though, using ArcView 3.0 and Freehand version 7.0 or 8.0, plus a small Mac shareware program called epsConverter.

### Before exporting

Before I export ArcView maps, I make sure that:

- Only the themes I need are turned on. Otherwise, ArcView will export unnecessary – and possibly confusing – data. I'll have to spend a lot of time later deleting it.
- Every feature is a unique color or color blend – either line color or fill color. It doesn't matter which color is which as long as it is unique. After I export the file, I can change the colors to whatever I want.
- Objects shown as lines, such as rivers and roads, are simple (single) lines, not filled lines, dotted lines or patterned lines.
- If the map uses symbols, they are made with simple geographic shapes, such as circles or squares.
- All text labels are deleted. If they are not, ArcView will convert them on export to *paths* that will have to be deleted.
- A suitable map projection is chosen. To do this, I pull down View | Properties and select the Projection button. I can select from at least one projection for every state or from several projections of the continental United States.

After this, I use File | Export and select NEW EPS to save the view. (While ArcView has an option to export to Adobe Illustrator format, it has a bug that renders it useless.) I use a network drive to move it to a Mac, but I could also export it by copying the file to a PC diskette and then inserting the diskette into a Macintosh.

### After exporting

Neither Freehand nor Illustrator can directly open the EPS file created by ArcView. But epsConverter, a $25 Macintosh shareware program, will convert it into a form that both programs can use. epsConverter is available from http://users.aol.com/ArtAge or ftp://users.aol.com/ArtAge.

To use epsConverter, I drag the EPS file onto the epsConverter icon. If my original file was called MYMAP.EPS, epsConverter creates a new file in the same directory called MYMAP.EPS.art.

Freehand requires lots of memory to handle an EPS file from ArcView, so I generally quit all other Mac applications, select the Freehand program icon and hit Control-I. I then boost the memory up as far as I can – to about 50 megs. (If you can't do this, and if Freehand gives you out-of-memory errors when opening the file, try opening it first in Adobe Illustrator and saving it in Illustrator 5.0 format. Freehand should be able to open the Illustrator file.)

Once I open the file in Freehand, I have to alternately ungroup the map and cut its contents twice before all the pieces are free. Then I go to the Xtras menu and Colors | Name All Colors. Naming all the colors lets me do two things:

- I can use the graphic search function to select groups of items by color. If I made all the roads red before exporting them from ArcView, I can now select all the red items, change them to the correct road color and add road line styles.
