import json
from dataclasses import dataclass, field
from typing import Optional
import datetime

# paths
User_Name = "iz"
DB_path = "../DataSave"
template_path = f"{DB_path}/DB-sample.json"
humanity_save_path = f"{DB_path}/User/{User_Name}/humanity.json"

sample_data = ""
with open(template_path, "r", encoding="utf-8") as f:
    for i in f.readlines():
        sample_data += i

set_prompt = f"""
```sample-user.json
{sample_data}
"""


# IDs 
from enum import Enum
class PromptMode(Enum):
    TALK = "[Talk]"
    CHECK = "[Check]"
    END = "[END]"
    SET = "[SET]"
    MAD = "[Mad]"

    @staticmethod
    def NowDo(mode, action):
        return f"{mode.value} {action}"

print(PromptMode.TALK.value)  # [Talk]
print(PromptMode.NowDo(PromptMode.TALK, "is running"))  # [Talk] is running


# Log
log_data = []
log_path = "../DataSave/log/log.jsonl"
class LogType(Enum):
    ERROR = "[ERROR]"
    CHECK = "[MESSAGE]"
    CREATE = "[CREATE]"
    ROAD = "[ROAD]"
    DELETE = "[DELETE]"
    UPDATE = "[UPDATA]"
    

    @staticmethod
    def NowDo(mode, action:str):
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp = datetime.datetime.now() #みり秒で欲しいので
        # return f"[{timestamp}] -- {mode.value} {action}"
        return {"timestamp":str(timestamp),"logType":mode.value,"action":action}



def logAdd(mode,action):
    log_input_data = LogType.NowDo(mode=mode,action=action)
    log_data.append(log_input_data)
    # print(log_input_data)
def log_Save():
    with open(log_path,"a",encoding="utf-8")as f:
        # json.dump(log_data,f,ensure_ascii=False,indent=4)
        for entry in log_data:
            f.write(json.dumps(entry,ensure_ascii=False)+ "\n")


# logAdd(LogType.CREATE,"Start analysis agent")
# logAdd(LogType.CREATE,"Clear Boot AI Agent")

log_Save()