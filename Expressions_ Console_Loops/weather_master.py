"""
File: weather_master.py
Name: Chris Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
"""

EXIT = -100


def main():
	"""
	When enters a set of temperature data, the computer will tell you
	the highest, lowest, and average temperatures, and how many days below 16
	degrees in this data set
	"""
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input('Next Temperature: (or -100 to quit)?'))
	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		high = temperature
		low = temperature
		num = 1
		total = temperature
		avg = total / num
		if temperature < 16:
			cold = 1
		else:
			cold = 0
		while True:
			temperature = int(input('Next Temperature: (or -100 to quit)?'))
			if temperature == EXIT:
				break
			if temperature > high:
				high = temperature
			elif temperature < low:
				low = temperature
			num = num + 1
			total = total + temperature
			avg = total / num
			if temperature < 16:
				cold = cold + 1
		print('Highest Temperature = '+str(high))
		print('Lowest Temperature = '+str(low))
		print('Average = '+str(avg))
		print(str(cold)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
