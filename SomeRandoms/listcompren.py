# number = [1,2,3,4,5,6,7,8,9,10]
# result = [a**2 for a in number if a%2 == 0]
# print(number)
# print(result)

# without using any extra variables

# result = [a**2 for a in range(1,11) if a%2 == 0]
# print(result)

# questiiom
# Create a list of passed students’ marks (marks ≥ 50) and add 5 grace marks to each,
# but the final marks must not exceed 100.

# marks = [45, 67, 89, 34, 56, 78, 92, 98]

# marks_final = [mark+5 if mark+5<100 else mark for mark in marks]
# print(marks_final)

# Create a list of only Gmail users, but store only the username part
# (example: "user@gmail.com" → "user").
emails = [
    "user@gmail.com",
    "admin@yahoo.com",
    "test@gmail.com",
    "hello@outlook.com",
    "info@gmail.com"
]
# # user_name = [unam for unam in emails for word in unam if word == "@"]
# user_name = [uname for email in emails ]
# print(user_name)

# Create a list of prices where:
# Price is greater than 500
# Apply 10% discount
# Final price should be rounded to nearest integer
# prices = [1200, 450, 3000, 800, 1500, 200, 5000]
# final_price = [round(pric-(pric*10/100)) if pric > 500 else pric for pric in prices]
# print(final_price)
# print(type(final_price))

# gmail_users = [email.split("@")[0] for email in emails if email.endswith("@gmail.com")]
gmail_users = [email.split("@")[0] for email in emails if email.lower().endswith("@gmail.com")]

print(gmail_users)