# SQL Mate – Natural Language to SQL Assistant

SQL Mate is an AI-powered **Natural Language to SQL assistant** that allows users to query an IPL analytics database using natural language instead of writing SQL queries manually.

For example, users can ask:

* Which player had the most sixes?
* Which player had the most wickets?
* Which team won the most matches?
* Who scored the most runs?

The application uses **Google Gemini** to convert natural language questions into SQL queries and executes the generated queries against a **MySQL database**.

## Features

* Natural Language to SQL conversion using Google Gemini
* Schema-aware SQL generation
* Automated SQL query generation and execution
* MySQL database integration
* IPL player and team performance analytics
* Query result display in a tabular format
* Environment-based credential management
* Error handling for AI and database operations

## Tech Stack

* **Python**
* **Google Gemini API**
* **MySQL**
* **Pandas**
* **PyYAML**
* **MySQL Connector/Python**

## Architecture

```text
User Question
      ↓
Google Gemini
      ↓
SQL Query Generation
      ↓
SQL Cleaning / Processing
      ↓
MySQL Database
      ↓
Query Execution
      ↓
Formatted Result
```

## How It Works

### 1. User enters a natural language question

```text
Which player had the most sixes?
```

### 2. Database schema is provided to Gemini

The application provides the database schema to the Gemini model so it can understand the available tables and columns.

### 3. Gemini generates SQL

Example:

```sql
SELECT
    BATTER AS player_name,
    SUM(CASE WHEN BATTER_RUNS = 6 THEN 1 ELSE 0 END) AS total_sixes
FROM BALL_BY_BALL
GROUP BY BATTER
ORDER BY total_sixes DESC
LIMIT 1;
```

### 4. SQL is executed

The generated query is executed against the MySQL IPL analytics database.

### 5. Result is displayed

```text
player_name    total_sixes
CH Gayle       359
```

## Database

The project uses an IPL analytics database containing ball-by-ball, match, player, and team information.

The database supports analysis of:

* Batting performance
* Bowling performance
* Runs
* Sixes and boundaries
* Wickets
* Match results
* Teams
* Players
* Venues
* Player of the Match statistics

The original datasets are not included in this repository.

## Project Structure

```text
sql_mate/
│
├── main.py
├── schema.py
├── create_database.py
├── import_data.py
├── schema.yaml
├── .gitignore
└── README.md
```

## Example Queries

```text
Which player had the most sixes?

Which player had the most wickets?

Which team won the most matches?

Who scored the most runs?

Which venue has the highest scoring average?

Give me the top 10 players by sixes.
```

## Setup

### Clone the repository

```bash
git clone https://github.com/Vicky14112004/sql_mate.git
cd sql_mate
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file containing your Gemini API key and MySQL credentials:

```env
GEMINI_API_KEY=your_gemini_api_key
MYSQL_HOST=localhost
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=IPL_ANALYTICS
```

Do not commit the `.env` file to GitHub.

### Run the application

```bash
python main.py
```

## Key Learning Outcomes

* Generative AI integration
* Natural Language Processing
* Text-to-SQL generation
* Prompt engineering
* Schema-aware LLM applications
* SQL query generation and execution
* MySQL database connectivity
* Data analytics using Python
* Error handling
* End-to-end AI application development

## Future Improvements

* SQL query validation and safety checks
* Conversational memory
* Query history
* Interactive web interface
* Automatic result visualization
* SQL query explanation
* Support for multiple databases
* Role-based database access

## Author

**Vignesh V**

AI / ML Developer

GitHub: [https://github.com/Vicky14112004/sql_mate](https://github.com/Vicky14112004/sql_mate)
