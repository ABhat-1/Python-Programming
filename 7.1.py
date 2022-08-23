def display(h):
    while True:
        try:
            h=h+1
            if h>=10:
                raise StopIteration
        except StopIteration:
            break
        finally:
            print(h,end=' ')
k=0
display(k)
    
