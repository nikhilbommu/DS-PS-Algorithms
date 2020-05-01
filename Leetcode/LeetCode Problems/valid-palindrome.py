s="race a car"
st = ""
for i in s:
    if i.isalpha():
        st += i
print(st)
if st == st[::-1]:
    print(True)
else:
    print(False)