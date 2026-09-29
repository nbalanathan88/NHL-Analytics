##Config file to prep database tables

create_tbl_sql={}

##Table 1
create_tbl_sql['teams'] = """CREATE TABLE IF NOT EXISTS TEAMS (team_id INT AUTO_INCREMENT PRIMARY KEY,
team_abbrev VARCHAR(10) UNIQUE,
team_name VARCHAR(100),
conference_name VARCHAR(100),
division_name VARCHAR(100),
logo_url VARCHAR(200))"""

##Table 2
create_tbl_sql['standing'] ="""CREATE TABLE IF NOT EXISTS STANDING (standing_id INT AUTO_INCREMENT  PRIMARY KEY,
				                     		    team_id INT,
						      		  season VARCHAR(20),
							games_played INT,
							wins INT,
							losses INT,
							ot_losses INT,
							points INT,
							goals_for INT,
							goals_against INT,
							home_wins INT,
							away_wins INT,
							streak_type VARCHAR(20),
							streak_count INT,
							CONSTRAINT FOREIGN KEY (team_id) REFERENCES teams(team_id)
)"""
##Table 3
create_tbl_sql['players'] ="""CREATE TABLE IF NOT EXISTS PLAYERS (
player_id BIGINT PRIMARY KEY,
team_id INT,
first_name VARCHAR(100),
last_name VARCHAR(100),
position VARCHAR(10),
jersey_number INT,
birth_date DATE,
birth_country VARCHAR(10),
height_cm REAL,
weight_kg REAL,
shoots_catches VARCHAR(5) ,
headshot_url VARCHAR(200),
CONSTRAINT FOREIGN KEY (team_id) REFERENCES teams(team_id)
)

"""

##Table 4
create_tbl_sql['games']= """CREATE TABLE IF NOT EXISTS GAMES (
game_id BIGINT PRIMARY KEY,
season VARCHAR(20),
game_type INT,
game_date DATE,
home_team_id INT,
away_team_id INT,
home_score INT,
away_score INT,
game_state VARCHAR(20),
venue_name VARCHAR(150),
CONSTRAINT FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
CONSTRAINT FOREIGN KEY (away_team_id) REFERENCES teams(team_id)

)"""

##Table 5
create_tbl_sql['game_stats']= """CREATE TABLE IF NOT EXISTS GAME_STATS (
stat_id INT AUTO_INCREMENT PRIMARY KEY,
game_id BIGINT ,
player_id BIGINT,
team_id INT,
goals INT,
assists INT,
points INT,
shots_on_goal INT,
penalty_min INT,
toi VARCHAR(10),
plus_minus INT ,
CONSTRAINT FOREIGN KEY (player_id) REFERENCES players(player_id)

)"""

##Table 6
create_tbl_sql['skater_season_stats']="""CREATE TABLE IF NOT EXISTS skater_season_stats (
stat_id INT AUTO_INCREMENT PRIMARY KEY,
player_id BIGINT,
season VARCHAR(20),
team_id INT,
games_played INT,
goals INT,
assists INT,
points INT,
plus_minus INT,
penalty_min INT,
shots INT,
avg_toi VARCHAR(10),
CONSTRAINT FOREIGN KEY (team_id) REFERENCES teams(team_id),
CONSTRAINT FOREIGN KEY (player_id) REFERENCES players(player_id)
)"""

##Table 7
create_tbl_sql['goalie_season_stats']="""CREATE TABLE IF NOT EXISTS goalie_season_stats (
stat_id INT AUTO_INCREMENT PRIMARY KEY,
player_id BIGINT,
season VARCHAR(20),
team_id INT,
games_played INT,
wins INT,
losses INT,
ot_losses INT,
save_pct FLOAT,
goals_against_avg FLOAT,
shutouts INT,
saves INT,
CONSTRAINT FOREIGN KEY (team_id) REFERENCES teams(team_id),
CONSTRAINT FOREIGN KEY (player_id) REFERENCES players(player_id)
 )
"""
