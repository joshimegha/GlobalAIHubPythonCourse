#Question1

username = 'joshimegha200'
password = '1234567'
ip_username = input("Username: ")
ip_password = input("Password: ")
if username == ip_username and password != ip_password:
  print("Invalid Password")
elif username != ip_username and password == ip_password:
  print("Invalid Username")
elif username != ip_username and password != ip_password:
  print("Invalid password and username")
else:
  print("Successfully Login")

# Question 2

user_pass = {"first":"pass1","second": "pass2","third":"pass3","fourth":"pass4"}
ip_username = input("Username: ")
ip_password = input("Password: ")
if ip_username not in user_pass and user_pass.get(ip_username) != ip_password:
  print("Invalid password and username")
elif user_pass.get(ip_username) != ip_password:
  print("Invalid password")
else:
  print("Successfully Login")
