def high_low(vals):
    a=max(vals)
    b=min(vals)
    return(a,b)

vals=(20,30,75,44,33,99,62,34,56,85)
(high_value,low_value)=high_low(vals)
print("Highest Value=",high_value)
print("Lowest Value=",low_value)
