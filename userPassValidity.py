"""Wap to check whether a username matches the password.
If username doesn't exist then print invalid username.
If password is incorrect then print invalid password.
"""

stored_data={
    "user1@123":"xyz123",
    "user2@234":"cyv124"
}

username=input("enter username: ")
password=input("enter password: ")

if username not in stored_data:
    print("Invalid username")

elif stored_data[username] != password:
    print("Invalid password")
else:
    print("Successful Login!")