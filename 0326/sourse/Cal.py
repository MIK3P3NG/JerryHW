
# coding: utf-8

# In[1]:


x=input('number1:')
z1=input('func')
y=input('number2:')
def func(x):
    if z1=="+":
        return(int(x)+int(y))
    elif z1=="-":
        return(int(x)-int(y))
    elif z1=="*":
        return(int(x)*int(y))
    elif z1=="/":
        return(int(x)/int(y))
    else:
        return('404 error')
print(func(x))

