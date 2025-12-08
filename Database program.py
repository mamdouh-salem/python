name = []
age = [ ]
email = [ ]
database = { 'name': name, 'age': age, 'email': email }
print(' welcome to my database program ')
print ( " select an option :")
print ( " 1. add student ")
print ( " 2. view students ")
print ( " 3. update student info ")
print ( " 4. delete student ")
print ( " 5. exit ")
option = input ( " enter option number: " )
def add_student ():
    name = input(' enter student name: ')
    age = input (' enter student age: ')
    email = input (' enter student email: ')
    database['name'].append(name)
    database['age'].append(age) 
    database['email'].append(email)
    print(' student added successfully ')
def view_students ():
    for i in range(len(database['name'])):
        print(f" Student {i+1}: Name: {database['name'][i]}, Age: {database['age'][i]}, Email: {database['email'][i]}") 
def update_student ():
    student_index = int(input(' enter student number to update: ')) - 1
    if 0 <= student_index < len(database['name']):
        name = input(' enter new name: ')
        age = input(' enter new age: ')
        email = input(' enter new email: ')
        database['name'][student_index] = name
        database['age'][student_index] = age
        database['email'][student_index] = email
        print(' student info updated successfully ')
    else:
        print(' invalid student number ')           
def delete_student ():
    student_index = int(input(' enter student number to delete: ')) - 1
    if 0 <= student_index < len(database['name']):
        database['name'].pop(student_index)
        database['age'].pop(student_index)
        database['email'].pop(student_index)
        print(' student deleted successfully ')
    else:
        print(' invalid student number ')   
while True : 
    if option == '1':
        add_student ()
        option = input ( " enter option number: " )
    elif option == '2':
        view_students ()
        option = input ( " enter option number: " )
    elif option == '3':
        update_student ()
        option = input ( " enter option number: " )
    elif option == '4':
        delete_student ()   
        option = input ( " enter option number: " )
    elif option == '5':
        print(' exiting program ')
        break
    



                