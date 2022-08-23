class bittergourd:
    def healthy(self):
        print("Bitter gourd is good for health")
    def taste(self):
        print("Tastes bitter")
class sweets:
    def healthy(self):
        print("Sweets are not good for health")
    def taste(self):
        print("very tasty")

def checking(item):
    item.healthy()

b=bittergourd()
s=sweets()
checking(b)
checking(s)
    
        
