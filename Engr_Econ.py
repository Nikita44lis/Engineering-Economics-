
# coding: utf-8

# In[ ]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="whitegrid")
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
cf.go_offline()




class Engr_Econ:
    def __init__(self, i, n):
        self.i = i
        self.n = n 
        
    def find_F_given_P(self, P):        
        F_given_P = (P * (1 + self.i)**self.n)        
        x = []
        for i in range(self.n + 1):
            x.append(i)            
        y = []
        for i in range(self.n - 1):
            y.append(0)
        y.insert(0, -P)
        y.append(F_given_P)           
        df = pd.DataFrame({'x' : x ,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('F_given_P =',F_given_P)
    
    
    
    def find_P_given_F(self, F):        
        P_given_F = (F * (1/(1 + self.i)**self.n))                 
        x = []
        for i in range(self.n + 1):
            x.append(i)            
        y = []
        for i in range(self.n - 1):
            y.append(0)
        y.insert(0, -P_given_F)
        y.append(F)                           
        df = pd.DataFrame({'x' : x,'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('P_given_F =',P_given_F)
    
    def find_P_given_A(self, A):        
        P_given_A = (A*(((1+self.i)**self.n - 1)/(self.i*(1+self.i)**self.n)))        
        x = []
        for i in range(self.n + 1):
            x.append(i)            
        y = []
        for i in range(self.n):
            y.append(A)
        y.insert(0, -P_given_A)                                 
        df = pd.DataFrame({'x' : x,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('P_given_A =',P_given_A)    
    
    
    def find_A_given_P(self, P):        
        A_given_P = (P*((self.i*(1+self.i)**self.n)/((1+self.i)**self.n - 1)))                
        x = []
        for i in range(self.n + 1):
            x.append(i)                   
        y = []
        for i in range(self.n):
            y.append(A_given_P)
        y.insert(0, -P)                 
        df = pd.DataFrame({'x' : x,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('A_given_P =',A_given_P) 
    
    
    def find_F_given_A(self, A):        
        F_given_A = A*(((1+self.i)**self.n - 1)/self.i)        
        x = []
        for i in range(self.n + 1):
            x.append(i)            
        y = []
        for i in range(self.n - 1):
            y.append(A)
        y.insert(0,0)    
        y.append(-F_given_A)                
        df = pd.DataFrame({'x' : x,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('F_given_A =',F_given_A)
    
    
    def find_A_given_F(self, F):        
        A_given_F = F*((self.i)/((1+self.i)**self.n - 1))        
        x = []
        for i in range(self.n + 1):
            x.append(i)             
        y = []
        for i in range(self.n - 1):
            y.append(-A_given_F)
        y.append(F)
        y.insert(0,0)                    
        df = pd.DataFrame({'x' : x,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('A_given_F =',A_given_F)
        
        
        
    def find_P_given_A_arithmetic(self, A, G):        
        P_given_A = (A*(((1+self.i)**self.n - 1)/(self.i*(1+self.i)**self.n)))
        P_given_G = (G/self.i*((((1+self.i)**self.n - 1)/(self.i*(1+self.i)**self.n)) - (self.n/(1+self.i)**self.n)))
        P_given_A_arithmetic = P_given_A + P_given_G
        x = []
        for i in range(self.n + 1):
            x.append(i)            
        y = []
        for i in range(self.n):
            y.append(A + i * G)
        y.insert(0, -P_given_A_arithmetic)                                 
        df = pd.DataFrame({'x' : x,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('P_given_A =',P_given_A_arithmetic)         
            
        
    def find_P_given_A_geometric(self, A1, g):        
        if self.i == g:
            P_given_A_geometric = A1*(self.n/(1+self.i))
        else:
            P_given_A_geometric = (A1*((1-((1+g)/(1+self.i))**self.n)/(self.i-g)))
        x = []
        for i in range(self.n + 1):
            x.append(i)                        
        y = []
        A = A1
        for i in range(self.n-1):
            A = A * (1+g)
            y.append(A)
        y.insert(0, A1)    
        y.insert(0, -P_given_A_geometric)                                 
        df = pd.DataFrame({'x' : x,
                           'y' : y})
        bar_plot = df.iplot(kind='bar',x='x',y='y')        
        return bar_plot, print('P_given_A =',P_given_A_geometric)

