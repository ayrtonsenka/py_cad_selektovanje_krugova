from pyautocad import Autocad, APoint
import openpyxl

acad = Autocad(create_if_not_exists=True)

try:
    id_layer = acad.doc.Layers.Item("ID")
except Exception:
    id_layer = acad.doc.Layers.Add("ID")
    id_layer.Color = 3 

for obj in acad.iter_objects():  #ako je ovde greska samo ponovo pokrenuti program
    if obj.Layer == "ID":
        obj.Delete()

try:
    acad.doc.SelectionSets.Item("Krugovi").Delete()
except:
    pass

ss = acad.doc.SelectionSets.Add("Krugovi")

print("Selektuj krugove u AutoCAD-u i pritisni Enter...")
ss.SelectOnScreen() 

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Koordinate"
ws.append(["ID", "X", "Y"])

text_height = 1.2

for i, obj in enumerate(ss, start=1):
    if obj.ObjectName == "AcDbCircle":
        x, y, _ = obj.Center
        ws.append([i, x, y])

        point = APoint(x + 0.5, y + 0.5)  
        txt = acad.model.AddText(str(i), point, text_height)
        txt.Layer = "ID"  

wb.save("koordinate_krugova.xlsx")
print("Gotovo!")
