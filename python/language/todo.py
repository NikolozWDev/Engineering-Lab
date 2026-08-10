def pig_latin(s):
    if any(x.isdigit() for x in s) or not s:
        return None
    word = s.lower()
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    if word[0] in consonants:
        j = 0
        while j < len(word) and word[j] in consonants:
            j += 1
        if j == len(word):
            return word + "ay"
        return word[j:] + word[:j] + "ay"
    else:
        return word + "way"

def bmi(weight, height):
    bmi = weight / height * height
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"

import threading
import math
import random

class Neuron:
    def __init__(self, input_size):
        self.weights = [random.uniform(-1, 1) for _ in range(input_size)]
        self.bias = random.uniform(-1, 1)

    def activate(self, inputs):
        total = sum(w * i for w, i in zip(self.weights, inputs)) + self.bias
        return 1 / (1 + math.exp(-total))

def create_layer(size, input_size):
    return [Neuron(input_size) for _ in range(size)]

def forward_propagate(layer, inputs):


import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            try:
                contacts = json.load(file)
            except json.JSONDecodeError:
                contacts = []
    else:
        contacts = []
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}\n")

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    # Basic validation
    if not name or not phone or not email:
        print("All fields are required.")
        return

    # Check for duplicate
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("A contact with this name already exists.")
            return

    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

# Search contacts by name
def search_contacts(contacts):
    query = input("Enter name to search: ").strip().lower()
    found_contacts = [c for c in contacts if query in c['name'].lower()]

    if not found_contacts:
        print("No contacts found with that name.")
    else:
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}\n")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{name}' deleted successfully.")
            return
    print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. View all contacts")
        print("2. Add a new contact")
        print("3. Search contacts")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QLineEdit, QPushButton, QSizePolicy, QGridLayout
)
from PyQt5.QtCore import Qt

class TaskManager:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, text):
        self.tasks.append({"text": text, "done": False})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_complete(self, index, done=True):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = done

class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'To-Do List'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 400
        self.task_manager = TaskManager()
        self.task_manager.load_tasks('tasks.json')
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Central widget and layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # Input area: QLineEdit + Add Button
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a new task")
        input_layout.addWidget(self.input_field)

        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)
        self.add_task_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        input_layout.addWidget(self.add_task_button)

        # Task list
        self.task_list = QListWidget()
        self.task_list.setDragDropMode(QListWidget.InternalMove)
        self.task_list.itemChanged.connect(self.update_task_status)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)

        # Buttons at bottom: Delete and Mark Complete
        button_layout = QGridLayout()
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_selected_task)
        self.delete_button.setFixedSize(100, 40)
        self.delete_button.setStyleSheet("border-radius: 10px; background-color: #ff0000; color: #ffffff; font-size: 16px;")
        button_layout.addWidget(self.delete_button, 0, 0)

        self.mark_button = QPushButton("Toggle Complete")
        self.mark_button.clicked.connect(self.toggle_complete)
        self.mark_button.setFixedSize(150, 40)
        self.mark_button.setStyleSheet("border-radius: 10px; background-color: #00ff00; color: #ffffff; font-size: 16px;")
        button_layout.addWidget(self.mark_button, 1, 0)

        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Load existing tasks into UI
        self.load_tasks_into_ui()

    def load_tasks_into_ui(self):
        tasks = sorted(self.task_manager.tasks, key=lambda x: x['created_at'], reverse=True)
        for task in tasks:
            item = QListWidgetItem(task['text'])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            if task['done']:
                item.setCheckState(Qt.Checked)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
            else:
                item.setCheckState(Qt.Unchecked)
            self.task_list.addItem(item)

    def add_task(self):
        text = self.input_field.text().strip()
        if text:
            self.task_manager.add_task(text)
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setCheckState(Qt.Unchecked)
            self.task_list.addItem(item)
            self.input_field.clear()

    def delete_selected_task(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            row = self.task_list.row(item)
            self.task_manager.delete_task(row)
            self.task_list.takeItem(row)
        self.sync_tasks_with_ui()

    def toggle_complete(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            row = self.task_list.row(item)
            current_state = item.checkState()
            new_state = Qt.Unchecked if current_state == Qt.Checked else Qt.Checked
            item.setCheckState(new_state)
            self.task_manager.mark_complete(row, new_state == Qt.Checked)
            # Update font to strike through if completed
            font = item.font()
            font.setStrikeOut(new_state == Qt.Checked)
            item.setFont(font)

    def update_task_status(self, item):
        # Called when check state changes
        row = self.task_list.row(item)
        is_done = item.checkState() == Qt.Checked
        self.task_manager.mark_complete(row, is_done)
        font = item.font()
        font.setStrikeOut(is_done)
        item.setFont(font)
        self.sync_tasks_with_ui()

    def closeEvent(self, event):
        # Save tasks on exit
        # Update task list order and statuses before saving
        self.sync_tasks_with_ui()
        self.task_manager.save_tasks('tasks.json')
        super().closeEvent(event)

    def sync_tasks_with_ui(self):
        # Rebuild tasks list based on UI order and check states
        self.task_manager.tasks = []
        for index in range(self.task_list.count()):
            item = self.task_list.item(index)
            text = item.text()
            done = item.checkState() == Qt.Checked
            self.task_manager.tasks.append({"text": text, "done": done})

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TodoListApp()
    window.show()
    sys.exit(app.exec_())
