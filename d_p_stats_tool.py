import d_p_stats_module

numbers = []

while True :
    num_input = input("Give me numbers, type DONE when finished.")
    
    if num_input.lower() == "done" : 
        print(f"These are the numbers you put in: {numbers}")
        break
    
    try :
        num = float(num_input) 
        numbers.append(num)
        
    except ValueError:
        print("ERROR. Invaild Input. Please type in numbers or type 'done'")
        


while True:
    
    print("1. Mean")
    print("2. Variance")
    print("3. Standard Deviation")
    print("4. Standard Error")
    print("5. Z-score of a new observation")
    print("6. Summary of the statistics")
    print("7. QUIT")


    operation = input('''Above are stat computational options you can pick from. 
PLEASE SELECT THE NUBMER OF THE OPERATION YOU WANT''')
    
    if operation == "5" or operation == "6":
        while True:
            try:
                obs = float(input("What new observation would you like to look at?"))
                break
            except ValueError:
                print("System error, play type a number you would like to observe")
    
    elif operation == "7" :
        print("End of stats calculator")
        break
    
    
    if operation == "1":
        print(f'''
        Mean: {d_p_stats_module.mean(numbers)}
        ''')

    elif operation == "2":
        print(f'''
        Variance: {d_p_stats_module.variance(numbers)}
        ''')

    elif operation == "3":
        print(f'''
        Standard Deviation: {d_p_stats_module.st(numbers)}
        ''')

    elif operation == "4":
        print(f'''
        Standard Error: {d_p_stats_module.se(numbers)}
        ''')   

    elif operation == "5":
        print(f'''
        Z-Score: {d_p_stats_module.z(numbers, obs)}
        ''')

    elif operation == "6":
        print(f'''Summary:
        Mean: {d_p_stats_module.mean(numbers)} 
        Variance: {d_p_stats_module.variance(numbers)}
        Standard Deviation: {d_p_stats_module.st(numbers)}
        Standard Error: {d_p_stats_module.se(numbers)}
        Z-Score: {d_p_stats_module.z(numbers, obs)}
        ''')

    else :
        print('''
        ERROR. Please follow directions
        ''')       