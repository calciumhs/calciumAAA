while True:
    try:
        a = eval(input())
        b = int(input())
        c = a/b
        print('%d/%d = %.2f'%(a,b,c))
        break
    except ValueError:
        print('ValueError')
    except NameError:
        print('NameError')
    except ZeroDivisionError:
        print('ZeroDivisionError')    
            

        
        

