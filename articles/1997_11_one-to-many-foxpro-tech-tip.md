### Tech Tip
## One-to-many how-to

**By Jo Craven**
*The Washington Post*

Recently, I had a large Home Mortgage Disclosure Act table called master.dbf that included a field with Census tract numbers. The various tract numbers appeared repeatedly, indicating the numerous loan applications that came from each area.

I wanted to identify these tracts by their common neighborhood names.

To do this, with information provided by a local Census Bureau, I created a table called lookup.dbf with two fields: one called "tract" with the tract numbers, and the second called "hood" with the neighborhood names. Master.dbf already contained a tract field; I added a second corresponding field called "hood."

My task was to use lookup.dbf to fill in neighborhood names in the newly created and blank "hood" field in master.dbf.

To do this, I wrote the following FoxPro program, which works by advancing through each table, plucking neighborhood names from lookup.dbf and dropping them into master.dbf when the tract numbers from the two tables match.

### Getting technical

In geek speak, this is known as a one-to-many relationship: One record in lookup.dbf corresponded to many records in master.dbf.

Here is the program; an explanation follows:

```
clear
clear all
close all

use c:\master in 1
use c:\lookup in 2
select lookup

do while not eof('lookup')
   scan
      select master
      replace master.hood with
lookup.hood for
master.tract=lookup.tract
      endscan
   select lookup
   skip 1
enddo
```

### Explanation

```
clear
clear all
close all
```

These introductory commands make sure that you are working with a clean slate — everything is cleared or closed before the program begins.

```
use c:\master in 1
use c:\lookup in 2
select lookup
```

The two tables are opened with the "use c:\master in 1" and "use c:\lookup in 2" lines. You must still tell the computer which of these files to use first. "Select lookup" takes care of this.

```
do while not eof('lookup')
```

This acts like a scan loop. It steps through lookup.dbf. The "not eof" means "not end of file" and instructs the computer to continue working as long as it has not reached the end of lookup.dbf.

```
scan
      select master
      replace master.hood with
lookup.hood for
master.tract=lookup.tract
   endscan
```

This nested scan loop then selects the second table, master.dbf, and issues the replace command, which fills in the empty "hood" field in master.dbf with a neighborhood name drawn from the "hood" field in lookup.dbf when master.tract matches lookup.tract.

```
select lookup
skip 1
```

The computer has looked at the first entry in lookup.dbf, then scanned through every record in master.dbf and made the appropriate changes. But the computer still needs to advance to the next record in lookup.dbf and perform the same job. "Select lookup" and "skip 1" tells the machine to return to lookup.dbf, skip one record, and repeat the procedure. It does this until the computer reaches the end of lookup.dbf.

```
enddo
```

"Enddo" concludes the "do while" command.

*Jo Craven can be reached at (202) 334-6259 or by e-mail at cravenja@washpost.com.*
