

# An exception flew by!
# Traceback(most recent call last):
#     File "<stdin>", line 2, in < module >
# NameError: HiThere

try:
    raise NameError("Hi There")
except NameError:
    print("An exception flew by!")
    raise
