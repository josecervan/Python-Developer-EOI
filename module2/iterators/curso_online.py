class Course:
    def __init__(self):
        self.students = list()
        self.n_students = len(self.students)

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= self.n_students:
            raise StopIteration
        else:
            self.index += 1
            return self.index - 1
    
    def add(self, name):
        self.students.append(name)
        self.n_students = len(self.students)


if __name__ == '__main__':
    # Se crea un objeto para guardar todos los estudiantes
    course = Course()

    # Se añaden cuatro estudiantes
    course.add('Federico')
    course.add('Andrea')
    course.add('Pepe')
    course.add('Manolo')

    # Se realiza el bucle
    for student in course:
        print(course.students[student])

