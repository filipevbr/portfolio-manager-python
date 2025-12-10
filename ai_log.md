# AI Development Log - Filipe Vaz

**Course:** Computational Reasoning - PUCPR
**Project:** Personal Portfolio Manager
**AI Tool:** Google Gemini

---

## Date: 2025-10-21

### Challenge Encountered
I needed to create documentation (`README.md`) but wasn't sure about the structure or correct Markdown syntax.

### Prompt used
"I want help building a markdown" and "Let's create a readme compatible with the current project status".

### AI Response (Summary)
The AI provided a complete skeleton for the `README.md`, divided into sections like "Project Status", "Features", and "How to Use". It also explained basic syntax (e.g., `#` for titles, `* [ ]` for checklists).

### Analysis & Learning
I learned how to structure and organize documentation clearly using correct Markdown syntax.

---

## Date: 2025-10-21

### Challenge Encountered
I wanted to clear the console screen every time the main menu appeared to keep the interface clean, but didn't know how to do it in Python.

### Prompt used
"How to clear?" and "How to implement the official logic?"

### AI Response (Summary)
The AI explained I needed to import the `os` module. It detailed the logic of checking the operating system (`os.name`) to run `cls` (Windows) or `clear` (Linux/Mac).

### Analysis & Learning
I learned to import the `os` library to interact with the terminal and understood the need to handle different operating systems for cross-platform compatibility.

---

## Date: 2025-10-31

### Challenge Encountered
The code was functional but disorganized ("dirty") and hard to maintain.

### Prompt used
"I am an IT intern... Identify bad practices and code smells... Suggest improvements".

### AI Response (Summary)
The AI suggested modularizing the code by creating functions, professionalizing the screen clear method, and using `enumerate()` to list projects, besides handling numeric input errors.

### Analysis & Learning
I understood the importance of functions for code reuse. I learned about `enumerate(list, start=1)` to avoid manual counters prone to errors.

---

## Date: 2025-12-10 (The Great Refactoring - V2)

### Challenge Encountered
The code was still a single script with global variables and mixed language (Portuguese/English). I needed to professionalize the architecture for my portfolio, implementing data persistence and technical English.

### Prompt used
"I will redo this code in English... separate files... create code from scratch... Tips?"

### AI Response (Summary)
The AI acted as a Senior Mentor guiding a complete refactoring:
1.  **Data Structure:** Migrated to a List of Dictionaries approach.
2.  **Modularization:** Separated concerns into `main.py` (business logic) and `utils.py` (helpers).
3.  **Persistence:** Implemented `json` library to save/load data automatically.

### Analysis & Learning
This was the biggest technical leap. I learned:
* **Modularization:** How to import functions (`from utils import...`).
* **JSON:** How to persist data so it survives program restart.
* **Clean Code:** Using English naming conventions for international standards.

---

## AI Usage Declaration

During the development of this project, the author used **Gemini (Google)** to **assist in structuring, code review, concept explanation (Dictionaries/Modularization), and documentation formatting**. The author reviewed, tested, and implemented the code, taking full responsibility for the software functionality.