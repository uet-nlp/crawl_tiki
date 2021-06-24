import requests

link = "https://docs.google.com/forms/d/e/1FAIpQLSeM1v9q9D77i_tx0R_RMdxPwSiu6vAY7fTQt-KjcB4ysNxMlQ/formResponse"

d = {'entry.1167970414': 'Tùy chọn 1',
    'entry.1167970414': 'Tùy chọn 2',
    'entry.1167970414': 'Tùy chọn 3'
    }
dd = """entry.1167970414=T%C3%B9y+ch%E1%BB%8Dn+1&entry.1167970414=T%C3%B9y+ch%E1%BB%8Dn+2&entry.1167970414=T%C3%B9y+ch%E1%BB%8Dn+3"""
# j = json.dumps(d)
# print(j)
r = requests.post(link, data=dd)
print(r.content)

# for i in range(100):
#     print(i)