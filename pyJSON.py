#access json library
import json

#create the dictionary
data1= {
    'name': 'Taniya Butler',
    'age': 21,
    'city': 'Seattle, Washington',
    'interests': ['Reading', 'Music', 'Braiding', 'Nature'],
    'is_student': False

}

#creating a Json and writing the python object contents to the json
with open('data1.json','w') as json_file:

    #dump data dictionary into the JSON file
    json.dump(data1,json_file,indent=4)

    print("You have sucessfully written to data1.json")