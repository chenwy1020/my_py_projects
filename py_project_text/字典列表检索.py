students = [
    {"name": "阿土",
     "age": 19,
     "height": 1.78,
     "weight":70},
    {"name": "小美",
     "age": 18,
     "height": 1.65,
     "weight":45}
]
find_name = "小美"
for stu_dict in students:
    if stu_dict["name"] == find_name:
        print(stu_dict)
        break
else:
    print("没找到")

