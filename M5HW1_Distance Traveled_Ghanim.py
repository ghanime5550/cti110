# CIS-110
# Eihab Ghanim
# Distance Traveled
# 10/9/2017

#Get Speed and Hours
speed = input('Enter the speed in mph: ')
print (speed)
hours = int(input('How many hours traveled? '))
print (hours)
print
print ('Hours \t Distance Traveled')

#Calculate Distance Traveled
for time in range(1, hours + 1):
	DistanceTraveled = speed * time
	print (time, '\t' ,DistanceTraveled, 'miles')
    
#End
