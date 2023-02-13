from cryptcha import CaptchaClient

cli = CaptchaClient()
va = cli.validate("token")
print(va)
