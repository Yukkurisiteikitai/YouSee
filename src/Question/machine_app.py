import json
import os

# paths
UserName = "ketetou"
DB_path = "./DataSave"
template_path = f"{DB_path}/DB-Base-template.json"
humanity_save_path = f"{DB_path}/User/{UserName}/humanity.json"

def ensure_humanity_file(path):
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)  # ディレクトリを作成（既に存在する場合はスキップ）
    
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({}, f)  # 空のJSONオブジェクトを作成
        print(f"Created: {path}")
    else:
        print(f"Already exists: {path}")

ensure_humanity_file(humanity_save_path)

with open(template_path,"r",encoding="utf-8")as f:
    data = json.load(f)


def ssk_base():
    # 機械的なやつ
    for i in data['questions']:
        answerOverLine = input(f"今回の質問です。\n{i}はなんですか?")
        data['answers'][i] = answerOverLine
        print(f"{i}:{data['answers'][i]}")


    # File入力
    with open(humanity_save_path,"w",encoding="utf-8")as f:
        json.dump(data,f,ensure_ascii=False,indent=4)