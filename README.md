# GitView – GitHub User Search Tool

GitView is a simple Python CLI tool that fetches public information about GitHub users using the GitHub API.

---

##  Features

- Fetch GitHub user data instantly  
- Supports single and bulk username lookup  
- Handles errors (404, timeout, etc.)  
- Displays useful API response headers  

---

##  Requirements

- Python 3.x  
- requests library  

---

##  Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/HH-Labs-Official/GitView.git
```
2. Go into the Project Folder
```
cd GitView
```
4. Install Dependencies
```
pip install requests
```
   How to Run
```
python GitView.py
```
   Usage 

After running the program, you will see:

===== GitHub User Search Tool =====
1. Search single username.
2. Search usernames from file.
3. Exit
   
  ###  Option 1: Search Single Username
Select option 1
Enter a GitHub username

Example:

Enter username : torvalds

  ###  Option 2: Search Usernames from File

Select option 2

Enter file name

Example:

File name : users.txt

  Example users.txt
