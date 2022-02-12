with open('file.txt') as f:
    st = list(f.readlines())
for i in st:
    st[st.index(i)] = i.replace('\n', '')
st1 = []
st2 = []
for a in st:
    if a.isdigit():
        st1.append(a)
    else:
        st2.append(a)
st1.sort()
st2.sort(key= len)
print(st1 + st2)
