import requests
print(requests.post("http://localhost:8000/create/doctor/",data={"username":"022shube","email":"shuvraj1234@gmail.com","password":"shuvrajl"}).json())