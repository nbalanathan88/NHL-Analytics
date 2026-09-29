**NHL Analytics Hub**
An end-to-end data analytics platform for NHL statistics. Live data is ingested directly from the official NHL API, processed and stored in a MySQL database through Jupyter notebooks, and then explored via an interactive Streamlit dashboard. The dashboard includes a built-in SQL Query Explorer, enabling both technical and non-technical users to run custom queries and gain deeper insights into team and player performance.

**Project Workflow**
NHL API → Live game and player data
Python Requests → Automated data extraction
JSON Data → Raw structured format
Jupyter Notebooks → Data exploration, cleaning, and transformation
MySQL Database → Centralized storage and management
SQL Analysis + Streamlit Dashboard → Interactive querying and visualization
Insights & Results → Actionable analytics for teams, players, and viewers

| Technology | Purpose |
| --- | --- |
| **Python** | Core language for data collection, processing, and automation |
| **Requests** | Fetching live data from NHL API endpoints |
| **VS Code** | Interactive environment for data exploration, transformation, and loading |
| **MySQL** | Relational database for structured storage of processed data |
| **SQL** | Querying and analyzing stored data |
| **Streamlit** | Building an interactive web-based analytics dashboard |
| **streamlit-option-menu** | Sidebar navigation and multi-page app structure in Streamlit |
| **pandas** | Data manipulation and analysis in notebooks and dashboard |
| **Git / GitHub** | Version control, collaboration, and project portfolio hosting |


**Database Tables Overview**
teams → Stores NHL team information including name, abbreviation, conference, and division.
standing → Tracks season standings and points earned by each team.
players → Contains player biographical details for each team’s roster.
games → Holds game schedules along with results.
game_stats → Records per-player statistics for individual games.
skater_season_stats → Aggregates season totals for skaters (goals, assists, points).

goalie_season_stats → Aggregates season totals for goalies (save percentage, goals-against average, shutouts)
