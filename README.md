# Todo List Project

## 1. Introduction
The Todo List project is a web-based application designed to help users manage their tasks efficiently. It provides a simple interface for adding, updating, marking tasks as completed, and deleting tasks. This application is ideal for individuals or teams looking to stay organized and productive by tracking their tasks in a structured manner.

## 2. Problem Domain
Managing tasks in today’s fast-paced world can be overwhelming, especially when relying on traditional methods like paper lists or unorganized digital notes. Key issues include:
- **Lack of centralization**: Tasks are scattered across various platforms or mediums.
- **Difficulty in tracking progress**: No clear indication of completed or pending tasks.
- **Lack of prioritization**: Tasks are not systematically organized.

These challenges often lead to missed deadlines, decreased productivity, and unnecessary stress.

## 3. Solution Domain
The Todo List application addresses these problems by providing a centralized platform to manage tasks effectively. It offers the following features:

- **Task Creation**: Add new tasks with ease.
- ![Screenshot 2025-01-10 124959](https://github.com/user-attachments/assets/fc3e0dcb-e193-46ad-9cd6-86d19442848f)
- **Task Completion**: Mark tasks as completed to track progress.
- ![Screenshot 2025-01-10 125041](https://github.com/user-attachments/assets/ccf493f6-35e4-4b35-a0c3-77d788edffbd)
-  **Task Unmarking**: Reopen tasks if needed.
-  ![Screenshot 2025-01-10 125255](https://github.com/user-attachments/assets/3a951f3a-0ac6-48b1-8f01-95f5bf79aa6a)
- **Task Deletion**: Remove tasks that are no longer relevant.
- ![Screenshot 2025-01-10 125308](https://github.com/user-attachments/assets/556c4595-3176-4dac-a738-bf2846c70ea4)
- **User-Friendly Interface**: A clean and intuitive design ensures seamless navigation.

The application focuses on simplicity and functionality, making it accessible for users with varying technical expertise.

## 4. Software Used
The project utilizes the following software and frameworks:
- **Programming Language**: Python
- **Web Framework**: Django
- **Database**: SQLite (default Django database) for data persistence
- **Frontend**: HTML, CSS, and Bootstrap for styling
- **Development Environment**: VS Code 
- **Version Control**: Git for source code management and GitHub for repository hosting

## 5. Data Structure Used
The primary data structure used in the project is the Model-View-Template (MVT) architecture provided by Django:

Key Data Structures:

List: Tasks are stored as a collection in the database and retrieved as a list for display and processing.

Boolean: Used to track the completion status of tasks (e.g., completed = True/False).

Dictionary: Used to pass context data (e.g., tasks) from views to templates.

Stack-Like Behavior: Undo actions such as unmarking completed tasks can be thought of as stack-like operations, although not explicitly implemented as a stack.

In addition, the application employs Django’s ORM (Object-Relational Mapping) to interact with the database efficiently.

## 6. Methodology
The project development follows an iterative approach:

### Step 1: Requirement Analysis
Identify the core functionalities required for a task management system, such as task creation, completion, and deletion. Establish user needs and create a workflow.

### Step 2: Design
Define the database schema for tasks. Create wireframes for the UI and design the application's layout to ensure user-friendly navigation.

### Step 3: Development
- Set up the Django project and create an app for the Todo List.
- Develop models for task management, including attributes like title, description, and completion status.
- Create views for handling user requests, including rendering the task list, adding tasks, and marking tasks as completed.
- Implement templates for a responsive UI using HTML, CSS, and Bootstrap.

### Step 4: Testing
Perform unit testing and integration testing to ensure the application meets functional requirements. Address bugs or issues identified during testing.

### Step 5: Deployment
Deploy the application on a local server for testing and later on a cloud platform (e.g., Heroku) for public access.

### Step 6: Maintenance
Regularly update the application to include new features or improvements based on user feedback.

This methodology ensures a structured and efficient development process, resulting in a robust and user-friendly Todo List application.

