import json

# paths
UserName = "sakura"
DB_path = "../DataSave"
template_path = f"{DB_path}/DB-Base-template.json"
humanity_save_path = f"{DB_path}/User/{UserName}/humanity.json"

with open(template_path,"r",encoding="utf-8")as f:
    data = json.load(f)


# 機械的なやつ
for i in data['questions']:
    answerOverLine = input(f"今回の質問です。\n{i}はなんですか?")
    data['answers'][i] = answerOverLine
    print(f"{i}:{data['answers'][i]}")


# File入力
with open(humanity_save_path,"w")as f:
    json.dump(data,f,ensure_ascii=False,indent=4)