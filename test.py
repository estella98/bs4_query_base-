import json
import ast
with open('result.json', 'r') as fp:
    data = json.load(fp)

code1 = "train=pd.read_csv('train.csv')\ntest=pd.read_csv('test.csv')"
# print(data["pandas.read_csv"])
code2 = "train.head()"

code3 = "pd.get_dummies(all_data)"

def query_based_annotation(code):
    code_parse = ast.parse(code)
   
    tree = ast.dump(code_parse)
    comment = set()
    for child in ast.walk(code_parse):
        if isinstance(child, ast.Call):
            func_attr = str(child.func.attr)
            
            # can further detect whether it belongs to pandas or numpy library here
            if func_attr in data:
                for _comment in data[func_attr]:
                    comment.add(_comment)
    return comment

comment1 = query_based_annotation(code1)
print(comment1)

comment2 = query_based_annotation(code2)
print(comment2)
        
comment3 = query_based_annotation(code3)
print(comment3)
        



#traverse to find all function call


