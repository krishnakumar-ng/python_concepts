
import re

st = "hello world"
print(f"st :{st}")

res = re.search(r'world$', st)
print(res)

if res:
    print("Match Found.....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found.....")