import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
            )
        """
        self.cur.execute(sql)
        self.con.commit()


    def insert(self, name, age, doj, email, gender, contact, address):

        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",(name, age, doj, email, gender, contact, address))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()
o=Database("Employee.db")
#o.insert("Gokul","24","13-03-2020","saran2004@gmail.com","Male","1234567890","Surampatti valasu")
#o.fetch()
#o.remove("3")
#o.update("2","Pratosh","20","4-4-2003","pratosh44@gmail.com","Male","7653489101","Tirupur")