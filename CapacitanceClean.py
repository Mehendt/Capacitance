# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:48:31 2021

@author: ad1t1
"""

##linear equation for discharge decay:     ln V = ln V0 - t/RC


##libraries
import numpy as np
import matplotlib.pyplot as plt


#%% Large Capacitor

##voltage-time data from oscilloscope for large capacitor
Cap1Time, Cap1Voltage = np.loadtxt("Capacitor 1 Method 1.csv", skiprows = 2, delimiter = ",", unpack = True)


##plotting oscilloscope trace
plt.figure()
plt.plot(Cap1Time, Cap1Voltage)
plt.title("Oscilloscope Voltage Trace")
plt.xlabel("time, s")
plt.ylabel("voltage, V")


##creating an array of the log of voltage ln(V)
Cap1VPlot = []
for i in range(len(Cap1Voltage)):
    Cap1VPlot.append(np.log(Cap1Voltage[i]))
    
#%%
##finding index of the beginning of the discharge
temp = []

for i in range(len(Cap1VPlot)):
    if Cap1Voltage[i] > 5:
        temp.append([Cap1Voltage[i], i])
        s = i

#%%
##finding index of the end of the discharge
for i in range(len(Cap1Voltage[s:])):
    if Cap1Voltage[s + i] < 0.000000000001:
        e = s + i
        break
    
    
#%%
##shifting time so that discharge begins at t0 = 0 s
TPlot1 = []
for i in range(e - s):
    TPlot1.append(Cap1Time[s+i] - Cap1Time[s])
    
#%%    
plt.figure()

##plotting ln(V) against time
plt.plot(TPlot1, Cap1VPlot[s:e], "")


##fitting best fit line
fit, cov = np.polyfit(TPlot1, Cap1VPlot[s:e], 1, cov = True, full = False)
line = np.poly1d(fit)

##plotting best fit line
plt.plot(TPlot1, line(TPlot1))
plt.ylabel("Log of Voltage ln(V)")
plt.xlabel("Time, s")
plt.title("Graph showing the relationship between log of voltage V \n and time t during capacitor discharge")
#plt.savefig("Large Capacitor.svg")

#%%
##value of resistor used
R = 10e3
##-1/RC = -0.9 so C = 1/0.9R

##calculating C
grad1 = fit[0]
C = 1/(R*grad1*-1)

##finding error in gradient and C
gradErr1 = np.sqrt(cov[0,0])
capErr1 = gradErr1 * (1/(R * fit[0]**2))


print("For the large capacitor: \n \t Capacitance = ", 1/(R*grad1*-1), " +/- ", capErr1, " F")

#%% Small Capacitor

##voltage-time data from oscilloscope for large capacitor
Cap2Time, Cap2Voltage = np.loadtxt("Capacitor 2 Method 1.csv", skiprows = 2, delimiter = ",", unpack = True)

##plotting oscilloscope trace
plt.figure()
plt.plot(Cap2Time, Cap2Voltage)
plt.title("Oscilloscope Voltage Trace")
plt.xlabel("time, s")
plt.ylabel("voltage, V")


##creating an array of the log of voltage ln(V)
Cap2VPlot = []
for i in range(len(Cap2Voltage)):
    Cap2VPlot.append(np.log(Cap2Voltage[i]))

#%%
##finding index of the beginning and end of one discharge

for i in range(len(Cap2Time)):
    if Cap2Time[i] > 0:
        t0 = i
        break
 
##t0 is beginning of one charging-discharging cycle



for i in range(len(Cap2Voltage[t0:])):
    if Cap2Voltage[t0 + i] > 1.829999:
        start = t0 + i

##start is the beginning of the discharge


for i in range(len(Cap2Voltage[start:])):
    if Cap2Voltage[start + i] < 0.0001:
        end = start+i
        break

##end is the end of the discharge

#%%shifting time so that discharge begins at t0 = 0 s
T2Plot = []

for i in range(end-start):
    minus = Cap2Time[start]
    T2Plot.append(Cap2Time[start+i] - minus )

#%%
plt.figure()

##plotting ln(V) against time
plt.plot(T2Plot, Cap2VPlot[start:end], "")

##fitting best fit line
fit2, cov2 = np.polyfit(T2Plot, Cap2VPlot[start:end], 1, cov=True)
line2 = np.poly1d(fit2)


##plotting best fit line
plt.plot(T2Plot, line2(T2Plot))
plt.ylabel("Log of Voltage ln(V)")
plt.xlabel("Time, s")
plt.title("Graph showing the relationship between log of voltage V \n and time t during capacitor discharge")
#plt.savefig("Small Capacitor.svg")

#%%

##resistor value
R2 = 100e3
##1/RC = 0.9 so C = 1/0.9R

##calculating C
grad2 = fit2[0]
C2 = 1/(R2*grad2*-1)


##calculating error in gradient and capacitance
gradErr2 = np.sqrt(cov2[0,0])
capErr2 = gradErr2 * 1/(R2 * fit2[0]**2)

print("For the small capacitor: \n \t Capacitance = ", C2, " +/- ", capErr2, "F")







