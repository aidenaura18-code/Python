students = {
    "id1": {"name": "Sara"},
    "id2": {"name": "David"},
    "id3": {"name": "Sara"},
    "id4": {"name": "Surya"}
}

result = {}
names_seen = []

for student_id, details in students.items():
    if details["name"] in names_seen:
        names_seen.append(details["name"])
        result[student_id] = details

for student_id, details in result.items():
    print(student_id, ":", details)