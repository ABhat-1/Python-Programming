class snake:
    def intro(self):
        print("There are many types of snakes")
    def poi(self):
        print("Most of the snakes are poisonous but some are not")

class cobra(snake):
    def poi(self):
        print("Cobra is poisonous")

class garter(snake):
    def poi(self):
        print("Garter is non-poisonous")

sna=snake()
gar=garter()
cob=cobra()
sna.intro()
sna.poi()
cob.intro()
cob.poi()
gar.intro()
gar.poi()
