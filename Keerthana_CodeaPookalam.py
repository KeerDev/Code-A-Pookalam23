#!/usr/bin/env python
# coding: utf-8

# In[17]:


from joy import *

def flower():
    c1=circle(r=6.25, fill="orange",stroke="green")
    e1=ellipse(0,15,w=5,h=18, fill="white") | repeat(15,rotate(angle=30))
    return c1+e1

#inner pookalam
c2= circle(r=25, fill="green",stroke="purple")
r1 = rectangle(w=50, h=50,fill="purple",stroke="yellow")| repeat (2,rotate(angle=45))
r2 = rectangle(w=60.5, h=60.5,fill="yellow",stroke="orange")| repeat(2,rotate(angle=45))
r3 = rectangle(w=70, h=70, fill="orange",stroke="red")| repeat(2,rotate(angle=45))
r4 = rectangle(w=80, h=80, fill="#ff4d00",stroke="#ff4d00")| repeat(2,rotate(angle=45))


#inner shade circles
c3 = circle(r=55, fill="#FFBF00",stroke="#ff7400")
c4 =circle(r=60, fill="#ff7400",stroke="#ff4d00")
c5 =circle(r=69, fill="#ff4d00",stroke="red")
c6 =circle(r=73, fill="black",stroke="black")


#outer design
c7= circle(10,75,8,fill="purple", stroke="yellow")
shape1 = c7 | repeat(30, rotate(20))
c8 = circle(10,75,15,fill="white", stroke="green")
shape2 = c8 | repeat(20, rotate(20))
c9 = circle(10,75,25,fill="green",stroke="yellow")
shape3 = c9 | repeat(20, rotate(20))
c10 = circle(10,75,35,fill="yellow",stroke="orange")
shape4 = c10 | repeat(20, rotate(20))
c11 = circle(10,75,45, fill="orange",stroke="red")
shape5 = c11 | repeat(20, rotate(20))
c12 = circle(10,75,55,fill="#ff4d00",stroke="red")
shape6 = c12 | repeat(20, rotate(20))
c_final=circle(r=137, fill="black",stroke="black")


#output
show(c_final,shape6,shape5,shape4,shape3,shape2,shape1,c6,c5,c4,c3,r4,r3,r2,r1,c2,flower())


# In[ ]:




