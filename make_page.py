#!python
def divtag(tag):
    print("<div " + "\"" + tag + "\">")
# print("<div id=\"page_box">)
#
def divend():
    print("</div>")
#
def divclass(tag):
    print("<div class=" + "\"" + tag + "\">")
#
def spanclass(tag):
    print("<span class=" + "\"" + tag + "\">")
#
def spanid(tag):
    print("<span id=" + "\"" + tag + "\">")
#
def spanend():
    print("</span>")
#
def hreftag(tag):
    print("<a href=" + "\"" + tag + "\">")
#
def hrefend():
    print("</a>")
#
def imgtag(tag, wid, hspc, vspc):
    print("<img src=\"" + tag + "\"", end='')
    print(" alt=\"\"", end='')
    print(" width=\"" + str(wid) + "\"", end='')
    print(" hspace=\"" + str(hspc)  + "\"", end='')
    print(" vspace=\"" + str(vspc) + "\"", end='')
    print("/>")
#
def printsup(tag):
    print("<sup>" + tag + "</sup>")
#
def printverse(num,tag):
    printsup(num)
    print(tag)
#
#
#
#



divtag("id=page_box")
#
spanclass("newsletter_scripture_left")
print("\"This weeks theme:\"")
spanend()
#
spanid("newsletter_scripture_right")
print("\"Defiance\"")
spanend()
#
spanclass("newsletter_scripture_left")
print("\"Focus Scripture:\"")
spanend()
#
spanid("newsletter_scripture_right")
hreftag("https://www.biblegateway.com/passage/?search=Exodus+1%3A8-2%3A10&amp;version=NIV")
hrefend()
spanend()
#
spanclass("newsletter_scripture_left")
print("Other Readings:")
spanend()
#
spanid("newsletter_scripture_right")
hreftag("https://www.biblegateway.com/passage/?search=Psalm+12&amp;version=NIV")
print("Psalm 12")
hrefend()
#
hreftag("https://www.biblegateway.com/passage/?search=Romans+12%3A1-8&amp;version=NIV")
print("Romans 12:1-8")
hrefend()
#
hreftag("https://www.biblegateway.com/passage/?search=Matthew+16%3A13-20&amp;version=NIV")
print("Matthew 16:13-20")
hrefend()
#
spanend()
#
divclass("column one-half")
wid = 350
hspc = 4
vspc = 4
imgtag("Newsletters/images/newsletter-image-27-08-2017.jpg", wid, hspc, vspc)
divend()
divclass("column one-half")
print("Exodus 1:8-22")
printverse("8", "Then a new king, to whom Joseph meant nothing, came to power in Egypt")
printverse("9", "&ldquo;Look,&rdquo; he said to his people, &ldquo;the Israelites have become far too numerous for us.")
printverse("10", " Come, we must deal shrewdly with them or they will become even more numerous and, if war breaks out, will join our enemies, fight against us and leave the country.&rdquo;")
printverse("11", "So they put slave masters over them to oppress them with forced labour, and they built Pithom and Rameses as store cities for Pharaoh.")
printverse("12", "But the more they were oppressed, the more they multiplied and spread; so the Egyptians came to dread the Israelites")
printverse("13", "and worked them ruthlessly.")
printverse("14", "They made their lives bitter with harsh labour in brick and mortar and with all kinds of work in the fields; in all their harsh labour the Egyptians worked them ruthlessly")
printverse("15", "The king of Egypt said to the Hebrew midwives, whose names were Shiphrah and Puah,")
printverse("14", "")







divend()
