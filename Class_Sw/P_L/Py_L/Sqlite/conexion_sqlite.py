import sqlite3

conexion= sqlite3.connect('Base1.db')
print(type(conexion))

cursor01= conexion.cursor()
print(type(cursor01))
# cursor01.execute(''' CREATE TABLE usuarios(
#                 nombre VARCHAR(20),
#                 edad INT,
#                 direccion VARCHAR(50),
#                 telefono NUMERIC(19)) ''')

# cursor01.execute('INSERT INTO usuarios values("Jose",33,"Calle 1ra",3223424487)')

# mas_usuarios =[
#     ('Pedro',34,'Calle 4',3343535674),
#     ('Liz',28,'Calle 5',3343535677),
#     ('Tomas',32,'Calle 6',3343535671)
# ]

# cursor01.executemany('insert into usuarios values(?,?,?,?)',mas_usuarios)
# conexion.commit()

cursor01.close()
conexion.close()
