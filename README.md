# **Fast ToDo App**

Fast ToDo App is a simple, responsive web-based application built using **FastAPI** for the backend and a combination of **HTML**, **CSS**, and **JavaScript** for the frontend. It provides a clean interface to manage a to-do list, allowing users to add, delete, rename, and toggle the status of tasks. The tasks are categorized into **Completed** and **Incomplete** sections for better organization.

---

## **Features**

- **Add Tasks**: Create new to-do items with ease.
- **Delete Tasks**: Remove tasks from the list with a single click.
- **Toggle Status**: Mark tasks as complete or incomplete.
- **Dynamic UI**: The interface dynamically updates to reflect changes.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Bootstrap Integration**: Styled using Bootstrap for a modern look.

---

## **Getting Started**

### **Prerequisites**

1. **Python 3.8+** installed on your system.
2. A package manager like `pip` or `pipenv`.

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/c2p-cmd/fast-todo-app
   cd fast-todo-app
   ```

2. **Set Up the Backend**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the FastAPI Server**
   ```bash
   python3 app.py
   ```
   The application will be available at `http://127.0.0.1:7860`.

4. **Frontend Configuration**
   - Open the browser and navigate to the server URL. The frontend will be rendered dynamically.

---

## **Folder Structure**

```
fast-todo-app/
├── models/
├── ├── todo.py        # Database models for tasks
├── static/
│   ├── index.js       # Contains JavaScript logic for the frontend
├── templates/
│   └── index.html     # HTML template with Jinja2 template
├── main.py            # FastAPI application entry point
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## **Usage**

### **Adding a Task**
1. Enter a task description in the input field.
2. Click the **"Add Item"** button to add the task to the list.

### **Completing or Uncompleting a Task**
- Use the checkbox next to a task to toggle its completion status.

### **Deleting a Task**
- Click the trash icon next to a task to delete it from the list.

---

## **Technical Details**

### **Frontend**
- **Bootstrap** is used for styling the application.
- Dynamic updates are handled using **JavaScript**.
- Inline templates are rendered using **Jinja2** for server-side rendering.

### **Backend**
- **FastAPI** serves as the backend framework.

---

## **Screenshots**

### Desktop View
*Coming Soon*

### Mobile View
*Coming Soon*

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- [FastAPI](https://fastapi.tiangolo.com/) 
- [Bootstrap](https://getbootstrap.com/) 
- [Font Awesome](https://fontawesome.com/)

---