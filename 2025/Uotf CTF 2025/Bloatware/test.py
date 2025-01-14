import itertools
import subprocess
from concurrent.futures import ThreadPoolExecutor
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_char = []
for i in range(1, 4):
    for j in itertools.product(char, repeat=i):
        list_char.append("".join(j))
        if len(list_char) > 1950:
            break

list_char = list(set(list_char))[0:1950]

with open("list_char.txt", "w") as f:
    for item in list_char:
        f.write("%s\n" % item)

conds = open("./chall2.js", "r").read()
for i in range(0, len(list_char)):
    conds = conds.replace(f"array[{hex(i)}]", list_char[i])

conds = conds.split(",")
condition = []
for cond in conds:
    cons = cond.split("==")
    condition.append(cons[0].strip())
    condition.append(cons[1].strip())

def simplify_condition(cond):
    try:
        output = subprocess.run(
            f'python ./simplify.py "{cond}"',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        result = output.stdout.decode("utf-8").strip().split("simplified to")[-1]
        return result.strip()
    except Exception as e:
        return f"Error: {e}"

simplified_conditions = []
with ThreadPoolExecutor(max_workers=8) as executor:  
    results = list(executor.map(simplify_condition, condition))

with open("simplified_conditions.txt", "w") as f:
    for res in results:
        f.write(f"{res}\n")

print("Đã đơn giản hóa tất cả điều kiện và lưu kết quả vào simplified_conditions.txt.")
