
# command-line-python-task-application

The goal of this project is to develop a Python-based command-line application for managing tasks using an SQLite database.


## Features

- **Add tasks**: Users can create new notes.
- **View all tasks**: Users can view all the tasks.
- **View pending tasks**: Users can view all the tasks with status=pending.
- **View completed tasks**: Users can view all the tasks with status=completed.
- **Update tasks**: Users can update the description and status of any task.
- **Delete tasks**: Users can delete any tasks.



## Run Locally

Clone the project

```bash
  git clone https://github.com/kjlenish/command-line-python-task-application.git
```


Open a terminal or command prompt and navigate to the project directory


Run the script using the following command:
```bash
  python task-app.py
  ```



## Assumptions and Design Decisions

- **Database**: sqlite was chosen over json for easier, faster and optimised handling of data.
- **CLI Interface**: The interface is designed to stay running until it is explicitly closed.