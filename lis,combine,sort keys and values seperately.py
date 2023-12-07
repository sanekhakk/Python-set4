d1=input("data1: ")
d2=input("data2: ")
k_l=d1.split(",")
v_l=d2.split(",")

md=dict(zip(k_l,v_l))
sd=sorted(md.items())

ele=sorted(md.items(),key=lambda x: x[0])
sk=sorted(md.keys())
sv=sorted(md.values())

print("elements:",ele)

print("sorted keys:",sk)
print("sorted values:",sv)
