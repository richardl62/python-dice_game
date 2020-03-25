
global_min_val = 1
max_val = 9


# return list of lists
def compute(min_val, target, num_digits):

    if(num_digits == 1):
        if(target>= min_val and target <= max_val):
            return [[target]]
        else:
            return []
    elif (min_val < max_val):
        exclude = compute(min_val+1,target,num_digits)
        include = compute(min_val+1,target-min_val, num_digits-1)

        prepend = lambda x : [min_val] + x
        return exclude + list(map(prepend, include))
    else :
        return []


while (True) :
    target=int(input("target: "))
    digits=int(input("number of digits: "))
    print(sorted(compute(global_min_val, target, digits)))

#for i in range(1,45):
#    print(i,len(compute(global_min_val, i, 5)))




