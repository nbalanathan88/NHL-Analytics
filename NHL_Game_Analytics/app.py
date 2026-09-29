import pandas as pd
import streamlit as st
from db_api import execute_sql
from streamlit_option_menu import option_menu

st.set_page_config(page_title="🏃🏒NHL Analytics Dashboard", layout="wide")

# Load sample or live data (Using public NHL API or mock data for demonstration)
@st.cache_data
def load_nhl_data(sql):
  data = execute_sql(sql,output=True)
  return pd.DataFrame(data)


@st.cache_data(ttl=300)
def run_sql(sql):
    return load_nhl_data(sql)

# Sidebar navigation

with st.sidebar:
    st.markdown("Main Menu")
    page = option_menu(
        menu_title=None,
        options=["Home", "SQL Query"],
        icons=["house", "code-slash"],
        default_index=0,
    )


# HOME
if page == "Home":
    st.title("🏒 NHL Analytics Hub")
    st.caption("API-driven hockey data pipeline with SQL analysis and Streamlit dashboard")


    st.subheader("League Stats")
    teams_count = run_sql("SELECT COUNT(*) AS n FROM teams").iat[0, 0]
    players_count = run_sql("SELECT COUNT(*) AS n FROM players").iat[0, 0]
    games_count = run_sql("SELECT COUNT(*) AS n FROM games").iat[0, 0]

    #Final goals
    goals_total = run_sql(
        "SELECT SUM(home_score + away_score) AS n FROM games WHERE game_state = 'FINAL'"
    ).iat[0, 0]

    opt1, opt2, opt3, opt4 = st.columns(4)
    with opt1:
        with st.container(border=True):
            st.metric("Team Count", teams_count)
    with opt2:
        with st.container(border=True):
            st.metric("Player Count", players_count)
    with opt3:
        with st.container(border=True):
            st.metric("Game Count", games_count)
    with opt4:
        with st.container(border=True):
            #Final goals
            st.metric("Total Goals Scored", int(goals_total))

    st.divider()

elif page ==  "SQL Query":
        st.title("🔎 SQL Query Runner")
        st.write("Select Option to analyze game details !")
        query_options = {
        "Team with most goals": """SELECT tm.team_name, SUM(st.goals_for) AS total_goals
                              FROM standing st
                              JOIN teams tm ON st.team_id = tm.team_id
                              GROUP BY tm.team_name
                              ORDER BY total_goals DESC
                              LIMIT 1""",
        "Team with above avg point": """SELECT tm.team_name, st.points
                                        FROM standing st
                                        JOIN teams tm ON st.team_id = tm.team_id
                                        WHERE st.points > (SELECT round(AVG(points)) FROM standing)
                                        ORDER BY st.points DESC
                                        """,
        "Top Scored Team"       :"""SELECT t.team_name, s.goals_for
                                    FROM standing s
                                    JOIN teams t ON s.team_id = t.team_id
                                    ORDER BY s.goals_for DESC
                                    LIMIT 1""",
        "Teams with Avg > 50"  : """SELECT t.division_name, ROUND(AVG(s.points), 1) AS avg_points
                                FROM standing s
                                JOIN teams t ON s.team_id = t.team_id
                                GROUP BY t.division_name
                                HAVING AVG(s.points) > 90
                                ORDER BY avg_points DESC""",

        "Top 10 Teams" : """SELECT t.team_name, s.wins
                            FROM standing s
                            JOIN teams t ON s.team_id = t.team_id
                            ORDER BY s.wins DESC
                            LIMIT 10""",


        "Players and country": """SELECT first_name, last_name, birth_country
                                    FROM players
                                    Group by first_name, last_name, birth_country
                                """,

        "Distinct Teams"    : """SELECT distinct team_name, conference_name, division_name FROM teams"""}


        select_opt = st.selectbox("Choose a query:", list(query_options.keys()))
    
        choice = st.text_area("USer Query", value=query_options[select_opt], height=150)

        if st.button("▶ Run Query"):
            if not choice.strip():
                st.warning("Enter a SQL query first.")
            else:
                df = run_sql(choice.strip())

            if not df.empty or choice.strip().lower().startswith("select"):
                st.success(f"{len(df)} rows returned")
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("Query ran with no rows returned.")