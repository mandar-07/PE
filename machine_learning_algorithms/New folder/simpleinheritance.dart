class Person{
  String name;
  
  Person(this.name);

  void display() {
    print('Name: $name');
  }
}

class Student extends Person {
  int marks;
  Student(String name, this.marks) : super(name);


  void display() {
    print('Name: $name, Marks: $marks');
  }
}

void main() {
  Student s = Student('mandar', 85);
  s.display();
}

