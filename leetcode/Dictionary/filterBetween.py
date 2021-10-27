

if __name__ == '__main__':
    # Python3 code to demonstrate working of 
    # Dictionary items in value range
    # Using filter() + lambda + dictionary comprehension 
    
    # initializing dictionary
    test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9, 'for' : 8, 'geeks' : 11} 
    
    # printing original dictionary
    print("The original dictionary is : " + str(test_dict))
    
    # initializing range 
    i, j = 8, 12
    
    # using dictionary comprehension to compile result in one 
    print(test_dict.items())
    lam = lambda sub: int(sub[1]) >= i and int(sub[1]) <= j
    
    res = {key: val for key, val in filter(lambda sub: int(sub[1]) >= i and
                                    int(sub[1]) <= j, test_dict.items())}
    
    # printing result 
    print("The extracted dictionary : " + str(res)) 