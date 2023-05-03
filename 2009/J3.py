ottawa = int(input())

victoria = (ottawa - 300) % 2400
edmonton = (ottawa - 200) % 2400
winnipeg = (ottawa - 100) % 2400
halifax = (ottawa + 100) % 2400

minutes = int(str(ottawa + 130)[-2:])
if minutes >= 60:
    st_john = (ottawa - int(str(ottawa)[-2:]) + 200 + minutes - 60) % 2400
else:
    st_john = (ottawa + 130) % 2400

print(ottawa, "in Ottawa")
print(victoria, "in Victoria")
print(edmonton, "in Edmonton")
print(winnipeg, "in Winnipeg")
print(ottawa, "in Toronto")
print(halifax, "in Halifax")
print(st_john, "in St. John's")
