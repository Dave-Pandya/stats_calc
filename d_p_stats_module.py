def mean(numbers):
    if len(numbers) == 0:
        return "N/A"
    
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def variance(numbers):
    
    mean = sum(numbers) / len(numbers)
    
    variance = sum((i - mean)**2 for i in numbers) / len(numbers)
    
    return variance

def st(numbers):
    
    mean = sum(numbers) / len(numbers)
    
    sqa = sum((i - mean)**2 for i in numbers)
    
    div = sqa / len(numbers)
    
    st = div ** 0.5
    
    return st

def se(numbers):
    
    mean = sum(numbers) / len(numbers)
    sqa = sum((i - mean)**2 for i in numbers)
    div = sqa / len(numbers)
    st = div ** 0.5
    
    n = len(numbers) ** 0.5
    
    se = st / n 
    
    return se

def z(numbers, obs):
    
  
    mean = sum(numbers) / len(numbers)

    sqa = sum((i - mean)**2 for i in numbers)
    div = sqa / len(numbers)
    st = div ** 0.5
    if st == 0 :
        print('''
            Standard Deviation of 0. Z-score cannot be performed''')
    else:
        z = (obs - mean) / st
    
        return z

