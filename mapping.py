from operator import methodcaller
### 1 ###
## mapping the strip function over the list below.
## using methodcaller to map strip() function

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

humpty_stripped = map(methodcaller('strip'), humpty_dumpty)
for i in humpty_stripped:
	print(i)

### 2 ###

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
