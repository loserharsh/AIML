import pandas as pd

data = {
    "Name" : ['harsh', 'anya', 'bob'],
    "Age"  : [23 , 32, 32 ],
    "something" : ['this', 223 , True ],
    "something" : ['this', 223 , True ],
    "something1" : ['this', 223 , True ],
    "something2" : ['this', 223 , True ]
}

df = pd.DataFrame(data)
print(df)
