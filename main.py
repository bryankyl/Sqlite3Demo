import sqlite3

conn = sqlite3.connect("student.db")

c = conn.cursor()
c = conn.execute("""
        SELECT rowid,* FROM students WHERE student_no>20211003        
""")
record_number = 1
for student in c.fetchall():
    # print("%2d." % record_number, end='')
    print("%10s" % student[0], end='')
    print("%10s" % student[1], end='')
    print("%30s" % student[2], end='')
    print()
    record_number += 1



conn.commit()

conn.close()