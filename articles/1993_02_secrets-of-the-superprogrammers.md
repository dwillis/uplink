# Secrets of the Superprogrammers

**By Dan Woods
The News & Observer
Raleigh, N.C.**

Decades ago, in the datazoic era of the 1960s and 1970s, huge mainframes ruled the earth. Behemoths they were, cared for by a priesthood of superprogrammers, who loved to compress every field of every record into the smallest number of bits.

After the personal computer enlightenment in the early 1980s, memory became cheap and processors exploded with power. In this era, ease of use became more important than efficient storage.

The relational database revolution sprang from the premise that the method for asking questions should be independent of the way the data is stored. Structured Query Language was born to help people ask questions of data in an organized way. Instead of the compressed and Byzantine ways superprogrammers stored data, relational databases are stored in flat files, most of it in character form.

With a relational database, asking a new question means writing a new SQL statement. In a dBASE-type database, asking a new question meant asking the superprogrammer to write a new program. Superprogrammers loved this.

For the most part, the superprogrammers have fossilized, and no longer are able to make life difficult for the rest of us. They still exist, though, and frequently surface in state government bureaucracies, which have resisted for years competitive pressures that drove businesses to modernize. In this environment, data tends to be crammed together in wonderfully creative ways.

Superprogrammers must be given their due. Their methods stored the most data in the least space. One of the favorite techniques used by superprogrammers is using bit flags to store Boolean or logical variables. This is elegant because logical variables are those that can be either true or false, bits can be 0 or 1 — a perfect match. It is efficient because one byte can store 8 bit flags. In the era of P.C. enlightenment, one logical variable takes up one byte, which is no problem because storage abounds.

Superprogrammers would also store numbers such as dates in portions of integers. I recently encountered a two-byte date field that had the following format:

- Bits 0 through 7 were the year
- Bits 7 through 10 were the month
- Bits 11 through 15 were the day
(The bits are numbered from 0 to 15 starting at the right.)

This is a super-compact way to store dates. Each date is stored in a two-byte integer, rather than in a six-byte string of characters, like most dates (i.e., YYMMDD).

Despite their efficiency, these fields are an unholy nuisance! Unless you write Assembly Language code, the lingua franca of the superprogrammer, (or its modern equivalent, C) it seems that bit flags or two-byte dates will be impossible to use with a language like FoxPro, Paradox or XDB.

Fear not, however. Such fields are accessible to those unskilled in the ways of the superprogrammers. For even though superprogrammers can squish data together in ingenious ways, they cannot stop numbers from being numbers, and therein lies the solution.

A byte that contains 8 bit flags, for example, is a number from 0 to 255. If we look at the first 16 values in binary, hexadecimal and decimal notation, we can see a way out of our dilemma.

| Binary | Hex. | Dec. | Bit 7 on | Bit 6 on | Bit 5 on |
|--------|------|------|----------|----------|----------|
| 0000 0000 | 00 | 0 | | | |
| 0000 0001 | 01 | 1 | x | | |
| 0000 0010 | 02 | 2 | | | |
| 0000 0011 | 03 | 3 | x | | |
| 0000 0100 | 04 | 4 | | | x |
| 0000 0101 | 05 | 5 | x | | x |
| 0000 0110 | 06 | 6 | | x | x |
| 0000 0111 | 07 | 7 | x | x | x |
| 0000 1000 | 08 | 8 | | | |
| 0000 1001 | 09 | 9 | x | | |
| 0000 1010 | 0A | 10 | | x | |
| 0000 1011 | 0B | 11 | x | x | |
| 0000 1100 | 0C | 12 | | | x |
| 0000 1101 | 0D | 13 | x | | x |
| 0000 1110 | 0E | 14 | | x | x |
| 0000 1111 | 0F | 15 | x | x | x |

(Remember the bits are numbered from 0 to 7, starting at the left. Also, in hexadecimal A = 10, B = 11 etc. up to F = 15.)

How do we determine if an individual bit of this character is 0 or 1? First, treat the byte as a number. In FoxPro that means reading the byte in as a one-character field, then using the ASC function to translate it to a number. The number field will have to be 3 bytes long in FoxPro, because 8 bits can store a number from 0 to 255.

If we look at the byte as a number we can see some interesting things. Bit 7, the rightmost bit, is on — meaning 1 — when the number is odd, and off — meaning 0 — when the number is even. Bit 6, the second from the right, is on when the remainder after dividing the number by 4 is greater than 1. Bit 5 the third from the right, is on when the remainder after dividing by 8 is greater than 3. Bit 4 is on when the remainder after dividing by 16 is greater than 7.

Another way of talking about the remainder of number y is to use the term modulus. Number x modulus y is the remainder of x after dividing the number by y. If x is less than y then x is the same as its modulus with respect to y. In FoxPro this function is written MOD(x,y). MOD(7,4) = 3 because 7 has a remainder of 3 after being divided by 4. MOD(8,16) = 8 because 8 has a remainder of 8 when divided by 16. MOD(4,2) = 0 because 2 divides evenly into 4.

We can then write the following FoxPro IF THEN statements to decode the bit flags in a single byte field called BITFLAG:

```
IF MOD(BITFLAG, 2) > 0     THEN Bit 7 is on
IF MOD(BITFLAG, 4) > 1     THEN Bit 6 is on
IF MOD(BITFLAG, 8) > 3     THEN Bit 5 is on
IF MOD(BITFLAG, 16) > 7    THEN Bit 4 is on
IF MOD(BITFLAG, 32) > 15   THEN Bit 3 is on
IF MOD(BITFLAG, 64) > 31   THEN Bit 2 is on
IF MOD(BITFLAG, 128) > 63  THEN Bit 1 is on
IF MOD(BITFLAG, 256) > 127 THEN Bit 0 is on
```

This code will leave any number of bit flags smoking ruin. We use the same technique to decode the compact dates, which are stored as follows in a two-byte, unsigned binary integer we'll call TWOBDATE. When stored as a binary number, TWOBDATE has the following structure:

**yyyyyyyymmmmddddd**

where y are bits indicating the year, m indicate the month, and d the day.

TWOBDATE is converted from a two-byte integer to a FoxPro decimal number using NineTrack Express or some other tape conversion utility. The FoxPro number would have to be five bytes wide because two bytes, or 16 bits, can store a number from 0 to 65535.

The year field is stored in bits 0 through 7. That leaves 9 bits of the 16-bit number remaining. Nine bits can store a number from 0 to 511. The year bits, in essence, are storing the number of 512's in the 16-bit number. (That's equivalent to the three leftmost digits of a 9-digit decimal number storing the number of millions.) To find out the number of 512's in the number we take the number, subtract its remainder with respect to 512, and then divide by 512. Thinking of this in millions rather than 512's may make it clearer. The number of millions in a number is the number minus the first 6 digits, divided by a million. This formula extracts the year from the first 7 bits:

**year = (TWOBDATE - MOD(TWOBDATE,512))/512**

We handle the next two fields in a similar fashion. For the month, bits number 8 to 11, we note that there are 5 bits to the right, which can store from 0 to 31. That means the 8th to 11th bits are counting the number of 32's in the number. We eliminate bits 0 to 7 by taking the number modulus 512. The formula to extract the month is therefore:

**month = (MOD(TWOBDATE,512) - MOD(TWOBDATE,32))/32**

The day is easy. We simply take the number modulus 32.

**day = MOD(TWOBDATE,32)**

Putting this all together with other FoxPro functions to convert the entire two-byte date into a FoxPro date, we come up with the following command:

```
REPLACE ALL FOXDATE WITH
    CTOD(STR((MOD(TWOBDATE,512)-
    MOD(TWOBDATE,32))/32) + "/" +
    STR((TWOBDATE-MOD(TWOBDATE,512))/
    512,2,0))
```

Take that, superprogrammers!
