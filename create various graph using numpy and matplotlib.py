import numpy as np
import matplotlib.pyplot as plt

student=np.array(["jaya","sumithra","sreesha","shayna"])
sub=np.array(["Python lan","C lan","Java lan","C++ lan","R lan"])
per=np.array([20,20,10,25,25])
#plt.figure()
#plt.pie(per,labels=sub)
#plt.title("pie chart")

#plt.show()
marks=np.array([[90,98,98,99,100],
                [90,89,98,97,96],
                [70,80,98,98,98],
                [50,70,80,90,90]])
total=np.sum(marks,axis=1)
avg=np.average(marks,axis=0)
plt.figure()
plt.bar(student,total)
plt.xlabel("Student_name")
plt.ylabel("Total_marks")
plt.show()
plt.figure()
plt.pie(per,labels=sub)
plt.title("PIE CHART")
plt.show()
plt.figure()
plt.plot(sub,avg,marker="o")
plt.xlabel("Student_name")
plt.ylabel("Total_marks")
plt.show()
#plt.figure()
#plt.bar(student,total)
#plt.xlabel("Student_name")
#plt.ylabel("Total_marks")
#plt.show()
