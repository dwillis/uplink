## Correction

In last month's Tech Tips, Elliot Jaspin made some suggestions for dealing with various spellings of a company, such as "Amalgamated Zoot Suits," within a database called BADSPELL. But Uplink printed one command incorrectly.

The correct command is:

```
Update BADSPELL
Set NewName = "Amalagated"
Where Xleft(name, 11) =
"Amalgamated"
```

Our apologies.
