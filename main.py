from cryptcha import CaptchaClient

cli = CaptchaClient()
tk = cli.generate_token()
va = cli.validate(tk)
print("token: %s" % tk)
print("validation: %s" % va)
