
import re

st = "hello23432&world"

res = re.search(r"\w+", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")