class Blaise:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Hi {self.name}. How are you feeling at {self.age} years old"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


me = Blaise("Blaise", 23)
print(me)


class Student:
    """
    A class of students
    """

    def __init__(self, name: str, age: int, course: str, likes: list) -> None:
        """
        An initialization function
        Args:
            name: name of student
            age: age of student
            course: main course taken by student
            likes: a list of things the student likes
        """
        self.name = name
        self.age = age
        self.course = course
        self.likes = likes

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return self.course

    def get_likes(self):
        return self.likes

    def __repr__(self):
        return f"Hello {self.name}. You are {self.age} years old. " \
               f"You are taking {self.course} and likes {self.likes[0]}"

    def show_info(self):
        info = {
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "likes": self.likes
        }
        return info

    def __getitem__(self, item):
        return self.show_info()[item]


moi = Student("Blaise", 23, "Mathematics", ["Math", "Food"])
print(moi['likes'])
