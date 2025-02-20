import subprocess
import sys
subprocess.call(['git','add','.'])
temp = input('コミットメッセージ')
while temp == "":
    print("ERROR-NottingERROR")
    temp = input('コミットメッセージ')   
    

print("do")

subprocess.call(['git','commit','-m',('"'+temp+'"')])
subprocess.call(['git','push','origin','main'])