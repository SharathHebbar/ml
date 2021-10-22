# class Father():
#     def garden(self):
#         print("Enjoys Gardening")


# class Mother():
#     def cook(self):
#         print("Enjoys Cooking")


# class Child(Father, Mother):
#     def sports(self):
#         print("Enjoys sports")


# c = Child()
# c.garden()
# c.cook()
# c.sports()

# class Father():
#     def skills(self):
#         print("Enjoys Gardening")


# class Mother():
#     def skills(self):
#         print("Enjoys Cooking")


# class Child(Father, Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("Enjoys sports")


# c = Child()
# c.skills()

class Father():
    def skills(self):
        print("Enjoys Gardening")


class Mother():
    def skills(self):
        print("Enjoys Cooking")


class Child(Father, Mother):
    def skill(self):
        # Father.skills(self)
        # Mother.skills(self)
        print("Enjoys sports")


c = Child()
c.skills()
c.skill()
