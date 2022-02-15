""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.w0qj1.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students
thorin_doc = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield II"
}
thorin_doc_id = students.insert_one(thorin_doc).inserted_id
bilbo_doc = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
}
bilbo_doc_id = students.insert_one(bilbo_doc).inserted_id
frodo_doc = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins"
}
frodo_doc_id = students.insert_one(frodo_doc).inserted_id
# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# test document 
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# insert the test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# call the find_one() method by student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})
#deleted_student_test_doc = students.delete_many({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#clean up
deleted_student_test_doc = students.delete_one({"student_id": "1007"})
deleted_student_test_doc = students.delete_one({"student_id": "1008"})
deleted_student_test_doc = students.delete_one({"student_id": "1009"})
# exit message 
input("\n\n  End of program, press any key to continue...")
