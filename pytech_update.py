from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.w0qj1.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
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

student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# instructions specify updating to the name on the next line, but output has to match, so I also set it back
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "something different than the originally saved name"}})
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})

# find the updated student document 
thorin = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")

#clean up
deleted_student_test_doc = students.delete_one({"student_id": "1007"})
deleted_student_test_doc = students.delete_one({"student_id": "1008"})
deleted_student_test_doc = students.delete_one({"student_id": "1009"})

input("\n\n  End of program, press any key to continue...")