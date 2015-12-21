#!/usr/bin/python
# read the name of the poem, the name of the author then read the poem line by line. In each loop, add a new line and end the poem with a EOF (Ctrl-D)

from time import strftime
import anydbm

class pyt():
    def __init__(self, dbname="pytry.db"):
        self.dbname = dbname

    def addpoem(self, title, poem):
        self.title = title
        self.poem = title
        db = anydbm.open(self.dbname, "c")
        db[self.title] = poem
        print "Poem added successfully\n"
        db.close()

    def listpoem(self):
        db = anydbm.open(self.dbname, "c")
        if len(db) < 1:
            print "No poems available at the moment. Add them before you list them\n"
        else:
            print "\n"
            x = 1
            for poem in db:
                print "{} : {}".format(str(x), poem)
                x = x+1

        db.close()

    def readpoem(self, poemtitle):
        db = anydbm.open(self.dbname, "c")
        self.poemtitle = poemtitle
        status = False
        for poem in db:
            if poem == self.poemtitle:
                status = True
                found_title = poem
                found_poem = db[poem]
        if status == False:
            print "The poem was not found. Did you enter the name correctly?\n"
        else :
            print "\n__{}\n__{}\n\n".format(found_title, found_poem)
        db.close()


pytry = pyt("poems.db")
try:
    choice  = int(raw_input("""Welcome to Pytry\n
>>>Ensure that you don't use double quotes, just single quotes<<<\n
Enter your choice\n
1: Add a poem\n
2: Read a poem\n
3: List poems\n
0: Quit\n_ """))

except KeyboardInterrupt:
    print "\nNo keyboard interrupt was required\n"
except EOFError:
    print "\nEOF Error detected\n"
else :
    while choice:
        if choice == 1:
            poet = str(raw_input("\nEnter your name : "))
            title = str(raw_input("Enter the title of the poem : "))
            moment = strftime("%d/%m/%Y  %H:%M:%S")
            print "Now enter the poem line by line (!!! to stop)"
            p = "\nTitle : {}\nPoet: {}\nWritten : {}\n_____\n".format(title, poet, moment)
            poem = str(raw_input(": "))
            while poem != '!!!':
                p = p+poem+"\n"
                poem = str(raw_input(": "))
            p = p+"\n"
            pytry.addpoem(title, p)

        elif choice == 2:
            title = str(raw_input("\nEnter the name of the poem : "))
            pytry.readpoem(title )

        elif choice == 3:
            pytry.listpoem()

        else :
            print "wrong choice"
        choice  = int(raw_input("""\n
    Enter your choice\n
    1: Add a poem\n
    2: Read a poem\n
    3: List poems
    0: Quit\n_ """))

print "\nThanks\n"
