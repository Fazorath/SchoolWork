# class SocialMedia:
#     def __init__(self, name, profilePicture, background, friends):
#         self.name = name
#         self.profilePicture = profilePicture
#         self.background = background
#         self.friends = friends

#     def changePicture(self, picture):
#         self.profilePicture = picture
#         if(picture.endswith(".jpg")):
#             print("1")
#         elif(picture.endswith(".png")):
#             print("2")
#         else:
#             print("3")

#     def changeBackground(self, background):
#         self.background = background
#         print("Background change.")

#     def printInformation(self):
#         print(self.name + " " + self.profilePicture + " " + self.background)

# james = SocialMedia("James", "picture.jpg", "Instructor", ["Ryan", "Allison", "Blanca", "Omar"])
# james.printInformation()
# james.changePicture("Classroom.gif")
# james.printInformation()
# james.changeBackground("Python Programmer")
# james.printInformation()

# hello = 15

# hello -= 5

# print(hello)

class Room:

     """Modeling a room in a building."""

     def __init__(self, name, furniture, length, width):

          self.name=name

          self.furniture=furniture

          self.length=length

          self.width=width

     def addFurniture(self, newFurniture):

          self.furniture=self.furniture.append(newFurniture)

     def changeDimensions(self, length, width):

          self.length=length

          self.width=width
