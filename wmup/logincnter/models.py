from django.db import models

# Create your models here.
class user_model (models.Model):

	SUCCESS = 1
	ERR_BAD_CREDENTIALS = -1
	ERR_USER_EXISTS = -2
	ERR_BAD_USERNAME = -3
	ERR_BAD_PASSWORD = -4
	MAX_USERNAME_LENGTH = 128
	MAX_PASSWORD_LENGTH = 128

	username = models.CharField(max_length = 128, primary_key = True)
	password = models.CharField(max_length = 128)
	count = models.IntegerField(default=1)

	def __str__(self):
		return self.username

	@classmethod
	def add(self, username, password):
		if user_model.objects.filter(username=username).count() > 0:
			return self.ERR_USER_EXISTS
		if not username or len(username) > self.MAX_PASSWORD_LENGTH:
			return self.ERR_BAD_USERNAME
		if len(password) > self.MAX_PASSWORD_LENGTH:
			return self.ERR_BAD_PASSWORD
		user = user_model()
		user.username = username
		user.password = password
		user.count = 1
		user.save()
		return user.count

	@classmethod
	def login(self, username, password):
		u = user_model.objects.filter(username=username)
		if u.count() == 1 and u[0].password == password:
			u.count += 1
			u.save()
			return u.count
		return self.ERR_BAD_CREDENTIALS

	@classmethod
	def TESTAPI_resetFixture(self):
		user_model.objects.all().delete()
		return self.SUCCESS