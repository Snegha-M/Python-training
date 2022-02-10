'''
    Loop Control Statements:
        Loop control statements change execution from its normal sequence.
        When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
        Python supports continue,break and pass statement.

    Break:
        It brings control out of the loop.
'''
print("#Break example")
for letter in 'snegha':
    if letter=='e':
        break
    print(letter)

'''
    Continue:
        It returns the control to the beginning of the loop.
'''
print("#Continue example")
for letter in 'snegha':
    if letter=='e':
        continue
    print(letter)

'''
    Pass:
        The pass statement is a null statement.ss
'''
print("#Pass example")
for letter in 'snegha':
    if letter=='e':
        pass
    else:
        print(letter)







