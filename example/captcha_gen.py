from cryptcha import CaptchaClient

cli = CaptchaClient()
tkn = cli.generate_token()
print(tkn)
