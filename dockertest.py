#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import json
data=pd.read_csv("../tcdata/num_list.csv",header=None)

#Q1
result1="Hello world"

#Q2
result2=0
for i,num in enumerate(data[0]):
    result2+=num

print(result2)
#Q3
data.sort_values(by=0,ascending=False,inplace=True)
result3=data[0][:10]
result3=list(result3)

result={"Q1":result1,
        "Q2":result2,
        "Q3":result3
       }
with open('result.json', 'w', encoding='utf-8') as f:
		json.dump(result, f)
