# Student Performance Tracker

A terminal-based application for managing student records and analyzing
performance across multiple subjects. It supports CRUD operations, search,
filtering by performance category, and JSON persistence.

## Key Features

- Add, update, delete, and list students
- Search students by ID
- Filter students by performance category
- Import student data from a JSON file
- Data persistence to a JSON file on every change
- Input validation for names, gender, and scores

## Tech Stack

- Python 3 (command-line application)
- JSON for data storage
- Node/Total.js wrapper for the web terminal (deployment environment)

## How It Works

- The app starts in run.py and launches the App class.
- App provides the menu and delegates actions to StudentManager.
- StudentManager handles all business logic and saves data to students.json.

## Menu Options

1. List all students
2. Add new student
3. Update student
4. Delete student
5. Search students by ID
6. Filter by marks category
7. Import from JSON file
0. Exit

## Data Model

Each student record includes:

- id (auto-assigned)
- name (full name)
- gender (Male or Female)
- english_score (0-100)
- math_score (0-100)
- science_score (0-100)
- art_score (0-100)

Total score is computed as the sum of the four subject scores.

### Performance Categories

- Distinction: total >= 380
- First Class: 300 to 379
- Second Class: 240 to 299
- Third Class: 180 to 239
- Fail: total < 180

## Project Structure

- run.py: Application entry point
- main.py: Menu and app flow
- student.py: Student model and manager
- students.json: Stored student data
- index.js, controllers/default.js, views/: Web terminal wrapper

## Setup

1. Ensure Python 3 is installed.
2. (Optional) Create and activate a virtual environment.
3. Install Python dependencies (none required by default):

	 pip install -r requirements.txt

## Run Locally

From the project root:

python3 run.py

## Importing Data

Use the menu option “Import from JSON file” and provide a filename such as
students.json. The file must be a JSON array of objects with the same fields
as the data model.

Example format:

[
	{
		"id": 1,
		"name": "Jane Doe",
		"gender": "Female",
		"english_score": 80,
		"math_score": 90,
		"science_score": 85,
		"art_score": 75
	}
]

## Deployment Notes (Heroku / CI Template)

If deploying using the Code Institute terminal template:

1. Add buildpacks in this order:
	 - heroku/python
	 - heroku/nodejs
2. Set config var PORT to 8000.
3. If using credentials, set config var CREDS with the JSON value.

## Constraints

The deployment terminal is 80 columns by 24 rows, so keep output within
that width for readability.
