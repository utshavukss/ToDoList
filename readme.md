# A ToDoList application using PyQT5
ToDoList applications are the go to projects while learning any technology. In this project, a ToDoList application is created using Python with PyQt5 as the GUI library and using the SQLite database to store the entries.
## Structure
The app consists of a basic UI containing a textbox to enter text as activity to do. Several buttons are available with self-explainatory names like "Add to List", "Clear List", and "Save to database". A QVBoxLayout widget is placed in the middle area of the UI where the ToDoList can be view as a list of checkboxes. The user can manually check or uncheck the activities mentioned in the list. Furthermore, a QProgressBar widget is present below the list items that indicate the progress based on number of activities completed.
## Functions
The application consists of a base class that contains a number of functions that are triggered when the user intercats with the GUI window. Some of the functions are:
### Add to List:
This function is executed when the user clicks on the "Add to List" button. It adds a CheckBox widget in the List view area with the text written in the TextEditor widget.
### Clear List:
It removes all the checkBox widgets in the list area at once.
### Save to database:
This function saves the data in the List view into an SQLite Database. The contents of the "activities" table is first erased before adding new data, everytime this function is called.
### FetchData from db:
When the app is launched, the data from SQLite database is extracted and based on the data (activity text and status of completion), checkBox Widgets are generated to add to the List area. This ensures that even when the app is closed and re-opened, the To-Do-List created by the user is not lost.
## Database Structure
The list.db is the database file used in this application which consists of an "Activities" table with two fields: "activity" and "status".
The text in the CheckBox widget is stored in the activity field while the checked status (whether the checkbox is ticked or not) is stored in the status field whenever the saveToDb() function is called. 
## How to run
The source code along with the packaged executable file are provided in this repository. One can install python3 and run command **python3 todo.py** to get the app running. Alternatively, the app can be run by simply opening the **dist/todo.exe** file.
