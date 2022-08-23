class MaxLimit(Exception):
    pass
def main():
    num=int(input("Enter a number:"))
    if __name__=='__main__':
        main()
    class MaxLimit(Exception):
        pass

def main():
    num=int(input("Enter a number:"))
    try:
        if num>500:
            raise MaxLimit("Enter a number below 500")
    except MaxLimit as ML:
        print(ML)        
if __name__=='__main__':
       main()  
