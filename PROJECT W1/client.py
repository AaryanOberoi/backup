import requests

r = requests.get('http://localhost:8000')
print(r.text)
s = requests.post('http://localhost:8000', json={'Aaryan Oberoi': 'Intern'})
# print(s.status_code,s.reason)
print(s)
