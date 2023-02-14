
son=[]
kv=[]
print("5 ta sonni kirgazing:")
for m in range(10):
    son.append(int(input(f"{m+1}-sonni kirgaing:")))
    print(f"{m+1}-sonning kvadrati {son[(m)]**2}")
    kv.append(f"{son[(m)]**2}")
print(f"siz kirgizgan sonlar:{son}")
print(f"shu sonlarning kvadrati:{kv}")
