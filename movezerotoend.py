def move_zero_atlast(no):
    null = 0  
  
    for i in range(len(no)):
        if no[i] != 0:
            no[null] = no[i]
            null += 1
    
   
    while null < len(no):
        no[null] = 0
        null += 1
    
    return no


num = list(map(int, input('Enter numbers separated by space: ').split()))
print('Original list:', num)

new = move_zero_atlast(num.copy()) 
print('Changed list:', new)
