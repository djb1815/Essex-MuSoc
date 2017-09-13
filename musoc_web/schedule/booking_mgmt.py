import datetime, re, calendar

class MuSocDiary():
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
	'Sep', 'Oct', 'Nov', 'Dec']
	now = datetime.datetime.now()
	today = datetime.datetime.date(now)
	todayName = now.strftime("%a")
	nowStr = re.split('-', str(today))
	current = int(nowStr[1])
	current_month = months[current-1]
	current_year = today.year
	bookingHours = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

	
	def daysInWeek():
		daysInWeek = []
		for i in range(7):
			dayNum = MuSocDiary.today + datetime.timedelta(days=i)
			daysInWeek.append(dayNum.day)
		return daysInWeek

	def daysInWeek2():
		daysInWeek2 = []
		for i in range(7,14):
			dayNum = MuSocDiary.today + datetime.timedelta(days=i)
			daysInWeek2.append(dayNum.day)
		return daysInWeek2

	def dayNameIter():
		dayNamesFromNow = []
		for i in range(7):
			dayToFormat = MuSocDiary.now + datetime.timedelta(days=i)
			dayName = dayToFormat.strftime("%a")
			dayNamesFromNow.append(dayName)
		return dayNamesFromNow

