from openpyxl import Workbook, load_workbook
import os

def write_excel(filename):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["name", "age"])
    sheet.append(["A", 22])
    sheet.append(["B", 22])
    workbook.save(filename)

def read_csv(filename):
    workbook = load_workbook(filename)
    sheet = workbook.active
    for row in sheet.iter_rows(values_only=True):
            print(f"Name: {row[0]}, Age : {row [1]}")


def delete_csv(filename):
    workbook = load_workbook(filename)
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


filename = "myfile.xlsx"
write_excel(filename)
print("Data reaf from csv file : ")
read_csv(filename)
#delete_csv(filename)
