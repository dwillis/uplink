# Will early version woes hurt XDB?

**David Raziq**
**MICAR**

For two weeks in July 1989, Bob Paynter was supposed to be on vacation. But during his stay at a North Carolina beach, he frequently found himself on the phone. The problem: his software. Paynter specializes in computer-assisted reporting for the Akron Beacon-Journal, and he says his database program of choice, XDB, was giving him major problems.

"I was very concerned," says Paynter. "I was involved in a project involving campaign finances that required me to move a large database back and forth between XDB and Dbase."

Paynter says his troubles began when he tried to import the information back into XDB. The program wouldn't accept it. So he placed the first of many calls to the software company.

"There were people joking in our department that suggested I demand a development fee from XDB," Paynter says.

In the last few months the staff of MICAR has heard a number of complaints from XDB users. Bob Paynter's story is representative.

For example, Paynter himself finally ended up shipping his entire database to XDB. During his break, XDB's technical support eventually solved his difficulty with a new import engine.

It wasn't long before he experienced another set of problems — indexing a large file.

"It would take a split second to index a file of almost two million records so I knew something was screwed up," he says.

When Paynter queried about the values within the file, his computer came up blank.

So after another month trouble-shooting with XDB's technical support staff, Paynter got the file to index. But he found a new bug: Given the exact same query, the program would return different answers.

And that, he explained, was the last straw.

"I said 'I just can't trust this,'" he says. "And I talked to other database managers, and nobody had ever heard of XDB." So after consulting friends, Paynter switched to the Paradox database system.

Ed Foldessy of the **Wall Street Journal** has also abandoned XDB for his record analysis. "XDB is not graceful with numbers," he says. "I encountered every conceivable problem working with it."

According to Foldessy, one of those problems included sorting fields. "It wasn't giving a good sort," he said. "You might have .01, .02, but then you'd have a number that was out of order."

Like Paynter, Foldessy says he "will never use XDB again," and instead relies on Dataease, his corporation's recommended program.

However, many reporters stand by the XDB product. Elliot Jaspin, the director of the Missouri Institute for Computer-Assisted Reporting, is one of the pioneers in this reporting technique. He has had a long standing relationship with XDB.

"When I was teaching at Columbia University, I began searching for a database program," says Jaspin. "So I went down to **PC Magazine**'s software library and tried them all. And XDB was the winner, hands down."

Jaspin lists speed, flexibility and ease of use as some of the product's strong points. Because he also uses XDB in his computer-assisted reporting seminar, he says the program has some other advantages. "It's a good teaching tool," he says. "It has a simple interface, and it has good implementation of structured query language."

But Jaspin also readily admits that the program has had an "unacceptably high number" of problems. Specifically, Jaspin mentioned problems indexing large files, and he has noticed an "unevenness" in XDB's support staff.

According to Mike Waters, XDB's Director of Sales, most of the problems were found on an earlier version of the software.

For example, Waters explained that Paynter's indexing problem was due to the index pointer being defined as a small integer. "So once you got up to a little over 31,000 unique indexes, you ran out of numbers," he says.

Waters said his company corrected those types of problems with the 2.4 version of XDB and currently markets a 2.41 version of the software.

Waters also explained that the once-limited indexing function of the 2.3 software could have caused Paynter to get different answers for the same query. "When you do the query, the optimizer inside is actually building indexes on a slide," he said. "So if he was dealing with a lot of records with the 2.3 version, he could have gotten inconsistent results if he got more than 31,000 on an index scheme."

However, Waters said he was unaware of any complaints about sorting fields of numbers, as was the problem Ed Foldessy experienced.

"As a matter of fact," he says, "I offer free products to any of these guys that made a comment to you. I'd love for them to try them again."

---

*David Raziq is a staff member at MICAR.*
