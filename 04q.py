#highest_scorer
def highest_scorer(o_dict):
    a=max(o_dict.values())
    for k,v in o_dict.items():
        if v==a:
            return k,v
o={"Abhi":800,"Kalki":1000,"Priya":400}
print(highest_scorer(o))
