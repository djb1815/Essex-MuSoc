import datetime, re, calendar

class MuSocDiary():
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
	'Sep', 'Oct', 'Nov', 'Dec']
	today = datetime.datetime.date(datetime.datetime.now())
	now = re.split('-', str(today))
	current = int(now[1])
	current_month = months[current-1]
	current_year = today.year