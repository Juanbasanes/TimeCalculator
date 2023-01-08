# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
print(add_time("10:06 AM", "204:02"))
print(add_time("8:06 AM", "19:02", "Thursday"))


# Run unit tests automatically
main(module='test_module', exit=False)