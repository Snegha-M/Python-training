import pandas as pd
from pandas import DataFrame
import json
raw_data ="""{"city":["Tripoli","Tripoli","Rome","Rome","Sydney","Sydney"],
        "rank":["1st","2nd","1st","2nd","1st","2nd"],
        "name":["Noureddin","Adam","Kevin","Raihana","Raghad","Mahdi"],
        "score1":[44,48,39,41,38,44],
        "score2":[67,63,55,70,64,77]
        }"""
data = json.loads(raw_data)
with open('json_data.txt', 'w') as f:
  json.dump(data, f, ensure_ascii=False)

print(data)
df=DataFrame(data)
print(df)

#read
with open('json_data.txt') as file:
  data = json.load(file)

print(data['city'][2])

for i in range(0,len(data['name'])):
  print(data['name'][i])

#write
detail = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }
    ],

        'color' : 'red'

}
json_string = json.dumps(detail)
print(json_string)


with open('json_detail.txt', 'w') as outfile:
  json.dump(json_string, outfile)


with open('json_detail.txt', 'w') as outfile:
  outfile.write(json_string)

#indexing:
print("selecting single column")
df = pd.DataFrame("json_data.txt", index="city")
first = data["rank"]
print(first)






