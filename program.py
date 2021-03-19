def fibonacci(n):
    a = 0
    b = 1
    no =[]
    if n <=0:
        # if user enters number less than and equal to 0 then it should return "can't calculate the fibonacci series"
        return "can't calculate the fibonacci series"
        
    else:
        # n indicates the number till the series should be continued
        for i in range(n):
            no.append(a)
            
            '''
            here we are adding two subsequent and storing in a and first number is storing in b
            and here we are using tuple unpacking concept.
            '''
            a,b  = a+b,a  
        return no
            

# handling user input exception
try:
    n = int(input('Enter the number : '))
    x = fibonacci(n)
    print(x)
# if user enters the string then it should raise an exception
except Exception as e:
    print("can't convert string to integer")
    
    

    
