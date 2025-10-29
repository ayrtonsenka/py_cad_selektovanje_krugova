# AutoCAD – Selektovanje i numerisanje krugova

Python alat koji omogućava brzo selektovanje, numerisanje i izvoz koordinata krugova iz AutoCAD crteža.  
Nakon selekcije krugova, skripta dodaje ID oznake direktno u crtež i automatski snima sve koordinate u Excel fajl.

---

## Funkcionalnosti

- Selektovanje krugova u aktivnom AutoCAD crtežu  
- Automatsko dodeljivanje ID brojeva (1, 2, 3, ...)  
- Dodavanje oznaka u AutoCAD na posebnom sloju „ID“  
- Izvoz koordinata svih selektovanih krugova u Excel fajl `koordinate_krugova.xlsx`

---

## Korišćene biblioteke

- `pyautocad`  
- `openpyxl`

Instalacija potrebnih biblioteka:

```bash
pip install pyautocad openpyxl pywin32
