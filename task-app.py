import sqlite3


class DB:
    db_path = "db.sqlite3"

    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                deadline  TEXT,
                status TEXT CHECK(status IN ('pending', 'completed')) DEFAULT 'pending'
            )
        ''')
        self.conn.commit()
    
    def add_task(self, description, deadline, status):
        self.cursor.execute("INSERT INTO tasks (description, deadline, status) VALUES (?, ?, ?)", (description, deadline, status))
        self.conn.commit()
        print("Task created successfully")
    
    def view_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found")

    def update_task(self, id, description, status):
        self.cursor.execute("UPDATE tasks SET description = ?, status = ? WHERE id = ?", (description, status, id))
        self.conn.commit()
        print("Task updated successfully")
    
    def delete_task(self, id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.conn.commit()
        print("Task deleted successfully")
    
    def filter_by_status(self, status):
        self.cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
        tasks = self.cursor.fetchall()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found")
    
    def search_tasks(self, pattern):
        self.cursor.execute("SELECT * FROM tasks WHERE description LIKE ?", ("%" + pattern + "%",))
        tasks = self.cursor.fetchall()
        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found")     

    def __del__(self):
        self.conn.close()


def main():
    db = DB()
    while True:
        print("\n\n1. Add a task\n2. View all tasks\n3. View Pending tasks\n4. View Completed tasks\n5.Update task\n6. Delete task\n7. Search task\n8. Exit\n")
        choice = int(input("Make your choice: "))
        if choice == 1:
            description = input("Enter the description: ")
            deadline = input("Enter the deadline: ")
            status = input("Enter the status (pending/completed): ")
            db.add_task(description, deadline, status)
        
        elif choice == 2:
            db.view_tasks()
        
        elif choice == 3:
            db.filter_by_status("pending")
        
        elif choice == 4:
            db.filter_by_status("completed")
        
        elif choice == 5:
            id = input("Enter the id of the task: ")
            description = input("Enter the new description: ")
            status = input("Enter the new status (pending/completed): ")
            db.update_task(id, description, status)
        
        elif choice == 6:
            id = input("Enter the id of the task: ")            
            db.delete_task(id)
        
        elif choice == 7:
            pattern = input("Enter the search string: ")
            db.search_tasks(pattern)
        
        elif choice == 8:
            del db
            exit()
        else:
            print("Invalid choice, try again")
    del db
            

main()