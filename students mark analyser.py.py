import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("students markss.csv")
#print(data)

subjects=["Maths","Physics","Chemistry","English","Biology","Economics","History","Civics"]
data["total"]=data[subjects].sum(axis=1)
data["average"]=data["total"]/len(subjects)
data["results"]=data["average"].apply(lambda x:"pass"if x>59 else "fail")
data=data.sort_values(by="total",ascending=False    )
data["rank"]=range(1,len(data)+1)

print(data)

plt.figure()
plt.plot(data["Name"], data["total"], marker="o")
plt.xlabel("Name")
plt.ylabel("Total")
plt.title("mark distribution")
plt.show()


