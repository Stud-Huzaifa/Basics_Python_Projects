email = input("Enter Your Email: ")

username = email[:email.index ("@")]
domain = email[email.index("@"):]

print(f"Your Username is {username} amd Domain is {domain} ")

#EMAIL SLICER