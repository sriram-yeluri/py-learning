class DemoClass:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@mail.com'

    def display(self):
        print(f'Email = {self.email}.')


def example():
    for i in range(1, 10, 2):
        if i == 5:  # skip value 5
            print('I am skipping to print the 5')
            i += i
        print(i)


def swap():
    a = 1
    b = 2
    print(a, b)
    a, b = b, a
    print(a, b)


if __name__ == '__main__':
    student_1 = DemoClass('Test', 'user')
    student_1.display()
    example()
    swap()
