import random
def func_maker(func,depth,max_depth):
    func_dict={1:'x',2:'y',3:'cos',4:'sin',5:'neg',6:'prod',7:'ave',8:'dif'}
    depth+=1
    if depth<max_depth:
        f=random.randint(3,6)
        if 3<=f<=5:
            return [func_dict[f],func_maker(func,depth,max_depth)]
        elif 6<=f<=8:
            return [func_dict[f],func_maker(func,depth,max_depth),func_maker(func,depth,max_depth)]
    else:    
        return [func_dict[random.randint(1,2)]]

print func_maker([],0,3)