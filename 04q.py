#highest scorer
def highest_scorer(o_dict):
    a=max(o_dict.values())
    for k,v in o_dict.items():
        if v==a:
            return k,v
d={"Ramesh":900,"Vicky":800,"Ritish":1900}
print(highest_scorer(d))