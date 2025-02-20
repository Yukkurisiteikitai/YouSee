import json

# paths
User_Name = "iz"
DB_path = "../DataSave"
template_path = f"{DB_path}/DB-sample.json"
humanity_save_path = f"{DB_path}/User/{User_Name}/humanity.json"



sample_data = ""
with open(template_path,"r",encoding="utf-8")as f:
    for i in f.readlines():
        sample_data += i 

prompt = f"""

```sample-user.json
{sample_data}
```

`sample-user.json`はUserの人生情報です。


"""
print(prompt)

#これじゃなくて

# for i in data['questions']:

#     answerOverLine = input(f"今回の質問です。\n{i}はなんですか?")
#     data['answers'][i] = answerOverLine
#     print(f"{i}:{data['answers'][i]}")



# File入力
# with open(humanity_save_path,"w")as f:
#     json.dump(data,f,ensure_ascii=False,indent=4)