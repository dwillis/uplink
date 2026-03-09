# Fun with the *dir* Command

**By Richard Mullins**
*University of Missouri*

There really is something useful that a DOS command can do for you, even if you use Windows all the time because you hate typing DOS commands.

Computer hard drives can quickly become like attics or neglected closets. They fill up with so much stuff that we forget what's there and waste a lot of space with things we don't need any more or files that are duplicated unknown times in subdirectories all over the place.

What if we could inventory all the files on a hard drive into one sorted text file that could be viewed with a text editor or printed?

The DIR command, plus a few options, will do it.

Many DOS users are familiar with the use of /p or /w after a DIR command. These switches, as they're called, pause the output of the DIR list every screenful or arrange the output horizontally. The following disk inventory command will use three options you may not have used before.

Here's the command. Change to the root directory first (cd/), then type:

```
dir /on /s /a-d > disklist.txt
```

It may take a minute to finish, and you won't see anything on your screen while it's working, but that's it.

Here's the explanation:

The first option — `/on` — orders the directory output by name. Use `/oe` if you want to order files by extension, `/od` by date, `/os` by size.

The second option — `/s` — gets the directory output for all subdirectories. That's why you have to do the command from the root directory of the drive.

The third option — `/a-d` — means show only files, not directory names, which you normally see in a DIR output. We exclude them here because they would be redundant. Every subdirectory in the output will have a full path heading.

To understand this one, remember that DOS considers directories as a special kind of file. Translated more exactly, this option means: include files that don't have the directory attribute. "Slash A" (/a) introduces the attribute option; "Minus d" (-d) means "not directory."

The greater-than sign (>) is the redirect sign. If you leave this part off, you'll see the directory output rush by on the screen without stopping. Redirecting the output from the screen to a file (here called disklist.txt) gives you something a little more permanent you can view or print.

One more tip: If you want a quick reminder on any DOS command, don't fumble for your manual; the answer is already on your computer if you have DOS 5.0 or higher. You can find the short documentation on any DOS command by typing the command word, followed by `/?`

For example: `copy /?`

*Richard Mullins can be reached at (314) 882-2127.*
