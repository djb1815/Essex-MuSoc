import datetime, re, calendar

class MuSocDiary():
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
	'Sep', 'Oct', 'Nov', 'Dec']

	def Main():
		today = datetime.datetime.date(datetime.datetime.now())
		now = re.split('-', str(today))
		current = int(now[1])
		current_month = MuSocDiary.months[current-1]
		current_date_num = int(re.sub('\A0', '', now[2]))
		current_year = int(now[0])

