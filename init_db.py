import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
)
''')

sample_employees = [
    ('Tharun Iyer', 'Finance', 'tharun.iyer@example.com'),
('Deepa Rao', 'IT', 'deepa.rao@example.com'),
('Ramya Subramanian', 'IT', 'ramya.subramanian@example.com'),
('Lavanya Shetty', 'IT', 'lavanya.shetty@example.com'),
('Ishaan Subramanian', 'HR', 'ishaan.subramanian@example.com'),
('Sathish Rao', 'HR', 'sathish.rao@example.com'),
('Charan Reddy', 'IT', 'charan.reddy@example.com'),
('Harini Subramanian', 'IT', 'harini.subramanian@example.com'),
('Bhavana Srinivasan', 'IT', 'bhavana.srinivasan@example.com'),
('Deepa Iyer', 'HR', 'deepa.iyer@example.com'),
('Vignesh Reddy', 'IT', 'vignesh.reddy@example.com'),
('Yamini Krishnan', 'Finance', 'yamini.krishnan@example.com'),
('Manoj Pillai', 'IT', 'manoj.pillai@example.com'),
('Bhavana Rao', 'HR', 'bhavana.rao@example.com'),
('Tharun Naidu', 'Finance', 'tharun.naidu@example.com'),
('Sathish Krishnan', 'Finance', 'sathish.krishnan@example.com'),
('Vignesh Gopal', 'HR', 'vignesh.gopal@example.com'),
('Yamini Das', 'IT', 'yamini.das@example.com'),
('Usha Menon', 'HR', 'usha.menon@example.com'),
('Pranav Reddy', 'HR', 'pranav.reddy@example.com'),
('Oviya Ilango', 'HR', 'oviya.ilango@example.com'),
('Bhargavi Natarajan', 'IT', 'bhargavi.natarajan@example.com'),
('Ulaganathan Eashwaran', 'HR', 'ulaganathan.eashwaran@example.com'),
('Nandhini Loganathan', 'Finance', 'nandhini.loganathan@example.com'),
('Yugendran Ilango', 'HR', 'yugendran.ilango@example.com'),
('Dinesh Jagadeesh', 'Finance', 'dinesh.jagadeesh@example.com'),
('Sharanya Natarajan', 'HR', 'sharanya.natarajan@example.com'),
('Sharanya Zachariah', 'HR', 'sharanya.zachariah@example.com'),
('Lakshmi Ranganathan', 'HR', 'lakshmi.ranganathan@example.com'),
('Ulaganathan Jagadeesh', 'IT', 'ulaganathan.jagadeesh@example.com'),
('Lakshmi Thangaraj', 'Finance', 'lakshmi.thangaraj@example.com'),
('Revansh Hariharan', 'HR', 'revansh.hariharan@example.com'),
('Ajay Zachariah', 'Finance', 'ajay.zachariah@example.com'),
('Ulaganathan Balaji', 'Finance', 'ulaganathan.balaji@example.com'),
('Ulaganathan Loganathan', 'IT', 'ulaganathan.loganathan@example.com'),
('Thamizh Ranganathan', 'Finance', 'thamizh.ranganathan@example.com'),
('Mahesh Natarajan', 'HR', 'mahesh.natarajan@example.com'),
('Bhargavi Darshan', 'Finance', 'bhargavi.darshan@example.com'),
('Oviya Sekhar', 'IT', 'oviya.sekhar@example.com'),
('Varun Yegneswaran', 'Finance', 'varun.yegneswaran@example.com'),
('Oviya Udhayakumar', 'IT', 'oviya.udhayakumar@example.com'),
('Keerthi Muthuraj', 'IT', 'keerthi.muthuraj@example.com'),
('Jayanth Natarajan', 'HR', 'jayanth.natarajan@example.com')
]

cursor.executemany(
    "INSERT OR IGNORE INTO Employees (Name, Department, Email) VALUES (?, ?, ?)",
    sample_employees
)

conn.commit()
conn.close() 