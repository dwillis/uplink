# Tech Tips

By Elliot Jaspin

**Subject:** Extracting information from a tape.

**Problem:** The Toxic Release Inventory uses what is called either a "submission number" in its 1987 documentation or a "document control number" in 1989. The number, which is 15 bytes long, occurs at position 5 in each of the different record types that make up the TRI file. The information in this field is crucial for a number of reasons.

The document control number is used to identify a specific source of pollution such as a plant, and is included in the various documents that are filed by the polluter. Using this number you can tie together all related bits of information on one site that are scattered throughout the TRI file. The number also contains the state where the plant is located. This information occurs as the last two bytes of the number.

Most people who use TRI are interested in information on polluters in one state or at most a small group of states. How then do you extract only those records for a specific state while keeping the all important document number intact during the transfer.

**Solution:** It is possible using NineTrack Express to define a field in two different ways. Thus, you can first define a field called "DocNo" that begins at position 5 for a length of 15. When you transfer information from the TRI file, you would make sure to import this field.

At the same time, you can also define the last two bytes of the document control number as the field. This field begins at position 18 for a length of 2.

Assuming that you only want those records where state equals "KY", there is no need to import the field. A state field that only contains "KY" would only take up valuable space on the hard disk.

However, you can still filter on this field even though you will not be importing. As each record is read from the tape, NineTrack Express will check to see if the state field contains "KY" and import the rest of the fields including the 15 byte document control number.
