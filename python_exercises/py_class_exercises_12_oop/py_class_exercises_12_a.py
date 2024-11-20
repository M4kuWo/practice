class Student:
    def __init__(self, age, email) -> None:
        self.age = age
        self.email = email

    @property
    def age(self):
        print("Getting age")
        return self._age

    @age.setter
    def age(self, value):
        print("Setting age")
        if not isinstance(value, int) or not (18 < value < 120):
            raise ValueError("Age must be an integer greater than 18 and less than 120.")
        self._age = value

    @property
    def email(self):
        print("Getting email")
        return self._email

    @email.setter
    def email(self, value):
        print("Setting email")
        if (not isinstance(value, str) or len(value) <= 4 or '@' not in value 
            or '.' not in value):
            raise ValueError("Email must be a string with more than 4 characters, "
                             "containing an '@' and a '.' symbol.")
        self._email = value

# Example usage
s1 = Student(33, "Mathias@domain.com")
s2 = Student(20, "Kaladin@domain.com")

print(s1.age, s1.email)
print(s2.age, s2.email)
