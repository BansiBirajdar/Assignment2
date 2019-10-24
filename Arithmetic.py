def Add(no1,no2):
    return no1+no2;

def Sub(no1,no2):
    return no1-no2;

def Mult(no1,no2):
    return no1*no2;

def Div(no1,no2):
    if(no2==0):
        print("enter no2 value is positive number");
        return 0;
    else:
        return no1//no2;