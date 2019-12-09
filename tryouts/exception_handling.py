# import random


# class InvalidGreetingException(Exception):
#     """
#     Raised when a string does not imply greeting
#     """
#     pass


# def main():
#     """
#       Doc string.Girish
#     """
#     greeting_messages = ["Hello", "Welcome", "Hey", "Hi"]
#     choices = greeting_messages + ["Bye", "Thanks", "GoodBye"]

#     greeting_choice = random.choice(choices)
#     print("Selected choice: {0!s}".format(greeting_choice))

#     if (greeting_choice not in greeting_messages):
#         raise InvalidGreetingException(
#             "Not a valid word for greeting", greeting_choice)


# if __name__ == "__main__":
#     try:
#         main()
#     except InvalidGreetingException as ex:
#         for arg in ex.args:
#             print(arg)

# class Phone:
#     def __init__(self, name, color):
#         self._name = name
#         self._color = color

#     # name not changeable once set
#     @property
#     def name(self):
#         return self._name

#     @property
#     def color(self):
#         """
#           Color of the phone
#         """
#         return self._color

#     # property returns an object
#     # which is the same as getter method
#     #
#     @color.setter
#     def color(self, color):
#         self._color = color


# phone = Phone("Motorola onepower", "black")
# print("Name: {0!s}, Color: {1!s}".format(phone.name, phone.color))

# phone.color = "red"
# print("Name: {0!s}, Color: {1!s}".format(phone.name, phone.color))

# class Sample:
#   def print_message(self, message):
#     print("Inside: print_message, message:{}".format(message))


# def fake_print_message(message):
#   print("Inside: fake_print_message, message:{}".format(message))


# sample = Sample()
# sample.print_message("Hello")
# print(sample.__dict__)

# # think of this like replacing the __dict__ of the object with key "print_message", updating its value to point to a different function object.
# sample.print_message = fake_print_message
# sample.print_message("Hello")
# print(sample.__dict__)


class CallableObject:
    def __call__(self, message):
        print("message: {}".format(message))


obj = CallableObject()
obj("This is a callable object behaving like a function")
CallableObject()("Hello")
