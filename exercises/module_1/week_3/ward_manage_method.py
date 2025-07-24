class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__ward = []

    def add_person(self, person):
        self.__ward.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for item in self.__ward:
            item.describe()

    def count_doctor(self):
        count = 0
        for item in self.__ward:
            if item.__class__.__name__ == "Doctor":
                count += 1

        return count

    def sort_age(self):
        self.__ward.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        result = 0
        count = 0

        for item in self.__ward:
            if item.__class__.__name__ == "Teacher":
                count += 1
                result += item.get_yob()

        return result/count


if __name__ == "__main__":
    # Write classes: Student, Doctor, Teacher and describe() method
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    # Write add_person(person) and describe() method
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # Count doctor
    print(f"\nNumber of doctors: {ward1.count_doctor()}")

    # Sort age
    print()
    ward1.sort_age()
    ward1.describe()

    # Average YoB
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
