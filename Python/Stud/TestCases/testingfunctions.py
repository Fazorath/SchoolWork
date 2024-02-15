import unittest

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
    
# print ("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == "q":
#         break
#     last = input("Please give me a last name: ")
#     if last == "q":
#         break

#     formatted_name = get_formatted_name(first,last)
#     print(f"\tNeatly Formatted name: {formatted_name}")

class NamesTestCase(unittest.TestCase):
    """Tests for 'testingfunctions.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        # instance of the function we want to test
        # formatted_name = get_formatted_name("Joplin","JANIS")
        formatted_name = get_formatted_name("janis","joplin")
        valuestest = formatted_name
        self.assertEqual(valuestest, "Janis Joplin")


if __name__ == "__main__":
    unittest.main()
