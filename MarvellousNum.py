def CheckPrime(num1):
    v_flag=0
    
    if num1 == 0 or num1 == 1:
        return False
    elif num1 ==2 or num1 ==3 or num1 ==5 or num1 ==7:
        return True
    elif num1 %2 ==0 or num1 % 3 ==0 or num1 % 5 ==0 or num1 % 7 ==0:
        return False
    else:
        return True

def Add_list(v_list):

    v_sum=0
    for i in range(len(v_list)):
        v_sum=v_sum+v_list[i]
    return v_sum
