# test_keys = ["dipaa", "jayshri", "renu"]
# test_values = [20, 17, 5]
# dic = {}
#  for key in test_keys:
#     for value in test_values:
#         dic[key] = value
#         test_values.remove(value)
#         break  
# print ("dictionary: " +  str(dic))



import json
with open("task_5.json","r")as file:
    data=json.load(file)
def anlyse_movie_genre():
    dict1={}
    for i in data:
        dic={}
        c=0
        if "Genre" in i:
            for j in i["Genre"]:
                genre=j
                for g in data:
                    if "Genre" in g:
                        for gen in g["Genre"]:
                            if genre==gen: 
                                c+=1 
            dic[genre]=c
            dict1.update(dic)
    with open("task11.json","w")as f:
        json.dump(dict1,f,indent=4)
anlyse_movie_genre()
