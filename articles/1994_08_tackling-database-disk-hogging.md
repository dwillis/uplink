### Tech Tips
## Tackling database disk-hogging

**By Chris Feola**
*Waterbury Republican-American*

Computer hardware tends to run a couple of generations ahead of software. This is sort of natural for programmers; there's not a lot of sense in writing a program for equipment that doesn't exist.

It can be a royal pain for users, though, when your screaming high-tech machine won't work because your software was designed for the latest and greatest hardware — of 1988.

A case in point: many database management programs have notorious problems with free disk space.

The problem lies in the need for large stretches of open disk space for temporary tables. Although this article deals with the problem in Paradox, the theories apply to FoxPro, Access, and other database management programs as well.

As a rule of thumb, Paradox needs free disk space equal to three times the size of the tables you want to use. If you want to sort a 30 megabyte table, for example, you need 120 megabytes of disk space: 30 for the table, and 90 for the temporary tables.

The temporary tables are built by Paradox as it reformats a table. It's the digital equivalent of running off 10 copies of a 50-page report on a copier, then spreading everything out on a table to assemble 10 sets of reports with the pages in the right order.

Knowing that database management programs tend to be disk pigs, I keep a 550-megabyte drive empty for database work.

So imagine my surprise one day when Paradox gave me an "Out of disk space" error message while rekeying a 12-megabyte table. Even if Paradox needed open disk space equal to 10 times the table, I was still good to go with 550 megabytes of free space.

Being geniuses, we did what we always do: We tried it again, on the always-popular theory that computers are odd and will sometimes not work for no particular reason.

No go. We got the same message: "Out of disk space."

We still needed the table sorted, however, so we thought we'd try a different tack. Instead of rekeying the table (keys are fields used to automatically sort a database table), we decided to try manually sorting the table with the SORT command.

This proved unsuccessful, but provided a solution. The sort failed, producing an "Out of disk space" error message. However, unlike the error messages that came up while trying to rekey the table using the table restructure command, the SORT error message offered the name of the offending table: C:TEMP$$$AF123.TMP.

Now we were getting somewhere. Paradox, in its infinite wisdom, was trying to shoehorn its temporary tables into my jammed C: drive, rather than my wide-open I: drive.

This is a throwback to the early days of DOS and PCs. A decade ago, you could plunk down several hundred dollars and get an enormous 10-megabyte hard drive.

DOS was built to treat the drive as a single object — after all, who could need more than one drive or partition?

But as far back as DOS 3.3 — around 1988 — DOS started to provide the ability to handle multiple partitions for large drives. And when your system gets up into the gigabyte range, dividing your drives up into partitions is a basic rule of disk management.

Many large systems are now using a separate partition for the operating system — an arrangement I favor. Modern system design reserves drive letters A: and B: for floppy drives; C: is usually the boot partition on the hard drive.

Setting up a separate C: partition has lots of advantages. This arrangement makes it easy to switch operating systems, for one; a switch I make about once a month it seems lately.

My setup uses a 150-megabyte C: partition. My work drive for Paradox is the empty 550 megabyte I: drive. But instead of working on I:, Paradox was putting the temp files on C:.

Paradox is putting its temp files on C: because that is where the system pointer is set. But the system pointer is supposed to be for system files, rather than program files. WordPerfect, for example, lets you set the pointer for that programs temp and backup files; if you don't set anything, the program defaults to its home directory.

Once we knew what Paradox was up to, the problem was easy to solve. We reset the system pointer to the I: drive, and Paradox cranked happily away.

---

### Tips for conquering the disk problem

- Set up a temp directory. Pick a drive with lots of open space and make sure you don't let it fill up. Make a temp directory using the Make Directory command.
- "MD TEMP" will make a directory called "TEMP."
- Set the system pointer to your new temp directory by putting the following line in your temp directory: "SET TEMP=C:TEMP". That line points to the TEMP directory on the C drive; obviously, substitute the correct drive and directory.
- Periodically clean out your temp directory. There are lots of ill-behaved programs that don't clean up their temp files. You can run out of disk space real quick — and for no reason — if you have a program leaving around large temp files.
- Never clean out your directory when windows is running!! If you shell out to a DOS prompt and erase temp files while Windows is running, you will crash your system and lose data from any programs that are running. Always exit to DOS and exit all programs before cleaning out the temp directory.
