import pandas as pd, streamlit as st, re, datetime
from datetime import datetime

current_year = datetime.now().year

airport_codes = {
	'AMS': 'Amsterdam',
	'ATH': 'Athens',
	'ATL': 'Atlanta',
	'AUS': 'Austin',
	'BCN': 'Barcelona',
	'BER': 'Berlin',
	'BKK': 'Bangkok',
	'BOS': 'Boston',
	'BRU': 'Brussels',
	'BUD': 'Budapest',
	'BUF': 'Buffalo',
	'BWI': 'Baltimore',
	'CDG': 'Paris',
	'CGN': 'Cologne',
	'CLE': 'Cleveland',
	'CLT': 'Charlotte',
	'CMH': 'Columbus',
	'COS': 'Colorado Springs',
	'CPH': 'Copenhagen',
	'CPT': 'Cape Town',
	'DAY': 'Dayton',
	'DEN': 'Denver',
	'DFW': 'Dallas',
	'DTW': 'Detroit',
	'DUB': 'Dublin',
	'DUS': 'Düsseldorf',
	'DXB': 'Dubai',
	'EZE': 'Buenos Aires',
	'FCO': 'Rome',
	'FLL': 'Fort Lauderdale',
	'FRA': 'Frankfurt',
	'GOT': 'Gothenburg',
	'GVA': 'Geneva',
	'HAM': 'Hamburg',
	'HKG': 'Hong Kong',
	'HNL': 'Honolulu',
	'IAH': 'Houston',
	'ICN': 'Seoul',
	'IND': 'Indianapolis',
	'IST': 'Istanbul',
	'JAX': 'Jacksonville',
	'JFK': 'New York',
	'KBP': 'Kyiv',
	'KUL': 'Kuala Lumpur',
	'LAS': 'Las Vegas',
	'LAX': 'Los Angeles',
	'LGB': 'Long Beach',
	'LGW': 'London Gatwick',
	'LHR': 'London Heathrow',
	'LIM': 'Lima',
	'LIS': 'Lisbon',
	'LTN': 'London Luton',
	'MAD': 'Madrid',
	'MCO': 'Orlando',
	'MEX': 'Mexico City',
	'MIA': 'Miami',
	'MSP': 'Minneapolis',
	'MSY': 'New Orleans',
	'MUC': 'Munich',
	'MXP': 'Milan',
	'NRT': 'Tokyo',
	'OKC': 'Oklahoma City',
	'ORD': 'Chicago',
	'OSL': 'Oslo',
	'PBI': 'West Palm Beach',
	'PDX': 'Portland',
	'PEK': 'Beijing',
	'PHX': 'Phoenix',
	'PIT': 'Pittsburgh',
	'PRG': 'Prague',
	'RDU': 'Raleigh-Durham',
	'SAN': 'San Diego',
	'SAV': 'Savannah',
	'SCL': 'Santiago',
	'SEA': 'Seattle',
	'SFO': 'San Francisco',
	'SIN': 'Singapore',
	'SJC': 'San Jose',
	'SJU': 'San Juan',
	'SLC': 'Salt Lake City',
	'STL': 'St. Louis',
	'STN': 'London Stansted',
	'STO': 'Stockholm',
	'SVO': 'Saint Petersburg',
	'SYD': 'Sydney',
	'TLV': 'Tel Aviv',
	'TPA': 'Tampa',
	'VIE': 'Vienna',
	'YUL': 'Montreal',
	'YVR': 'Vancouver',
	'YYZ': 'Toronto',
	'ZRH': 'Zurich',
}

airlines = {
	"AA": "American Airlines",
	"AF": "Air France",
	"BA": "British Airways",
	"DL": "Delta Air Lines",
	"UA": "United Airlines",
	"LH": "Lufthansa",
	"QF": "Qantas Airways",
	"EK": "Emirates",
	"SQ": "Singapore Airlines",
	"CX": "Cathay Pacific Airways",
	"NH": "All Nippon Airways",
	"AI": "Air India",
	"KL": "KLM Royal Dutch Airlines",
	"OS": "Austrian Airlines",
	"JL": "Japan Airlines",
	"AC": "Air Canada",
	"AF": "Air France",
	"TK": "Turkish Airlines",
	"SA": "South African Airways",
	"AZ": "Alitalia",
	"MS": "EgyptAir",
	"IB": "Iberia",
	"HA": "Hawaiian Airlines",
	"WY": "Oman Air",
	"SK": "SAS Scandinavian Airlines",
	"FI": "Icelandair",
	"VN": "Vietnam Airlines",
	"A3": "Aegean Airlines",
	"FI": "Icelandair",
	"PS": "Ukraine International Airlines",
	"G3": "Gol Linhas Aéreas",
	"9W": "Jet Airways",
	"VY": "Vueling Airlines",
	"S7": "S7 Airlines",
	"TP": "TAP Air Portugal",
	"LY": "El Al",
	"GF": "Gulf Air",
	"PK": "Pakistan International Airlines",
	"TK": "Turkish Airlines",
	"KU": "Kuwait Airways",
	"EY": "Etihad Airways",
	"QR": "Qatar Airways",
	"AF": "Air France",
	"SV": "Saudia",
	"MH": "Malaysia Airlines",
	"A4": "Allegiant Air",
	"5J": "Cebu Pacific Air",
	"B6": "JetBlue Airways"
}

st.set_page_config(layout='wide', page_title='Air Schedule Tool', page_icon=":airplane_arriving:")
st.title("Flight Schedule Formatting Tool")

if 'format' not in st.session_state:
	st.session_state.format = False
	
if 'history' not in st.session_state:
	st.session_state.history = []
	
if 'text' not in st.session_state:
    st.session_state.text = ""

col1, col2, col3 = st.columns([0.34, 0.05, 0.561])

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #2E8B57; 
        color: white;
		border: 2px solid #000;
        border-radius: 10px;
        height: 3em;
        width: 12em;
    }
	.stButton>button:hover {
        background-color: #216640; 
        color: white;
		border: 2px solid white;
        border-radius: 10px;
        height: 3em;
        width: 12em;
    }
	.stButton>button:active {
        background-color: #388E3C; /* Change background color when button is clicked */
		border: 2px solid white;
        transform: scale(0.95); /* Slightly shrink the button on click */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Add shadow when clicked */
    }
	.stButton>button:focus {
        outline: none; /* Remove the outline */
		background-color: #4b514a; 
        border: none; /* Remove any border */
		color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        /* Target the button with data-testid="stBaseButton-secondary" and text "Clear" */
        button[data-testid="stBaseButton-secondary"] {
            background-color: red;
            color: white;
            border: none;
        }
        
        button[data-testid="stBaseButton-secondary"]:hover {
            background-color: darkred;
            color: white;
            border: 2px solid white;
            border-radius: 10px;
            height: 3em;
            width: 12em;
        }
        
        button[data-testid="stBaseButton-secondary"]:focus {
            outline: none;
            background-color: red;
            color: white;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

def clear_text():
    st.session_state.text = ""

with col1:
	sked_source = st.selectbox(label='Schedule Source - Where did you get your schedule from?',options=['Tropics', 'Air Department'], placeholder='Tropics', help="Selection dictates how the schedule gets parsed")
	st.write("Paste your schedule below and the software will format it for you.")
	data = st.text_area(label='inputted schedule',label_visibility='collapsed', height=250, value=st.session_state.text)
	st.session_state.text = data
	format = st.button("Format Flight Schedule")
	if st.button('Clear', key='clear_button', on_click= clear_text):
		pass


def format_airdept_flights(text):
	air_dept_pattern = r'^\s*([A-Za-z]{2}\d{1,5})\s+([A-Za-z])\s+([A-Za-z]+)\s+([A-Za-z]{3})\s+([A-Za-z]{3})\s+([0-9]{2}[A-Za-z]{3})\s+([0-9]{4})\s+([0-9]{2}[A-Za-z]{3})\s+([0-9]{4})\s+([A-Za-z]{2})\s+0\s+([A-Za-z\s]+)\s*$'
	flights = text.strip().split("\n")
	schedule = []

	for index, item in enumerate(flights):
		match = re.match(air_dept_pattern, item)
		if match:
			flight_info = match.groups()
			schedule.append(flight_info)
		
	df = pd.DataFrame(schedule, columns=[
		'Flight No', 
		'Bkg Class',
		'Cabin Class',
		'From',
		'To',
		'Dep Date',
		'Dep Time',
		'Arr Date',
		'Arr Time',
		'CODE',
		'Operating Airlines'])
	
	df['Airline'] = df['Flight No'].astype(str).str[:2]
	df['Flight Number'] = df['Flight No'].astype(str).str[2:]
	# Convert to datetime, add current year if no year is provided
	df['Dep Date'] = pd.to_datetime(df['Dep Date'].apply(lambda x: f"{x}{current_year}" if len(x) == 5 else x), format='%d%b%Y')
	df['Dep Date'] = df['Dep Date'].dt.strftime('%d-%b-%Y')
	df['Arr Date'] = pd.to_datetime(df['Arr Date'].apply(lambda x: f"{x}{current_year}" if len(x) == 5 else x), format='%d%b%Y')
	df['Arr Date'] = df['Arr Date'].dt.strftime('%d-%b-%Y')
	df['Dep Time'] = df['Dep Time'].apply(lambda x: f"{str(x).zfill(4)[:2]}:{str(x).zfill(4)[2:]}")
	df['Arr Time'] = df['Arr Time'].apply(lambda x: f"{str(x).zfill(4)[:2]}:{str(x).zfill(4)[2:]}")
		
	column_order = [
		'Flight No',
		'Airline',
		'Flight Number',
		'From',
		'Dep Date',
		'Dep Time',
		'To',
		'Arr Date',
		'Arr Time',
		'Cabin Class', 
		'Operating Airlines']
	
	df = df[column_order]
	return df

def format_tropics_flights(text):
	tropics_pattern = r'^\s*([A-Za-z]{2}\d{1,5})\s+([A-Za-z])\s+([A-Za-z]{3})\s+([A-Za-z]{3})\s+(\d{2}-[A-Za-z]{3}-\d{4})\s+(\d{2}:\d{2})\s+(\d{2}-[A-Za-z]{3}-\d{4})\s+(\d{2}:\d{2})\s+([A-Za-z]+)\s+((?:non\s+stop|[A-Za-z\s]+))\s+(\d{1,2}[hH]\s*\d{1,2}[mM])\s+([A-Za-z\s]+)\s*$'
	flights = text.strip().split("\n")
	schedule = []
	for index, item in enumerate(flights):
		# Check if the current item is the first (index 0)
		if index == 0:
			# Split the item based on spaces
			parts = item.split()
			parts = parts[:-3]
			item = ' '.join(parts)

		match = re.match(tropics_pattern, item)
		if match:
			flight_info = match.groups()
			schedule.append(flight_info)
			
	df = pd.DataFrame(schedule, columns=[
		'Flight No',
		'Bkg Class',
		'From',
		'To',
		'Dep Date',
		'Dep Time',
		'Arr Date',
		'Arr Time',
		'Cabin Class', 
		'Transit Stops',
		'Layover Time',
		'Operating Airlines'])
	
	df['Airline'] = df['Flight No'].astype(str).str[:2]
	df['Flight Number'] = df['Flight No'].astype(str).str[2:]
	
	column_order = [
		'Flight No',
		'Airline',
		'Flight Number',
		'From',
		'Dep Date',
		'Dep Time',
		'To',
		'Arr Date',
		'Arr Time',
		'Cabin Class', 
		'Transit Stops',
		'Layover Time',
		'Operating Airlines']
	df = df[column_order]
	return df

def generate_script(df):
	script = ""
	previous_segment_date = None
	for i, row in df.iterrows():
		departure_city = airport_codes.get(row['From'], row['From']) 
		arrival_city = airport_codes.get(row['To'], row['To']) 
		depart_time = row['Dep Time']
		arrive_time = row['Arr Time']
		airline = airlines.get(row["Airline"], row["Airline"])
		operating_airlines = row.get(row['Operating Airlines'], row['Operating Airlines']).strip()
		
		dep_time = datetime.strptime(depart_time, "%H:%M").strftime("%I:%M %p")
		arr_time = datetime.strptime(arrive_time, "%H:%M").strftime("%I:%M %p")
		
		current_segment_date = pd.to_datetime(row['Arr Date'])
		
		# For the first row, skip the logic until previous_segment_date is set
		if previous_segment_date is None:  #we know this is the first segment
			script_open = f"We're able to offer:\n\n"
		elif i == df.index[-1]:
			script_open = f'Our final leg would be '
		elif abs((current_segment_date - previous_segment_date).days) <= 1 :
			script_open = f'This flight would connect to'
		elif abs((current_segment_date - previous_segment_date).days) > 5:
			script_open = f'On the return we have'
			
		# Update previous_segment_date after the check
		previous_segment_date = current_segment_date
		
		# Append the script_open to the overall script
		script += (script_open + f" **{airline}** flight **{row['Flight Number']}** departing from **{departure_city}** on **{row['Dep Date']}** at **{dep_time}** and arriving into **{arrival_city}** on **{row['Arr Date']}** at **{arr_time}**. This flight is operated by *{operating_airlines}*. \n\n")
		
	return script

if format:
	timestamp = datetime.now()
	st.session_state.format = True
	if sked_source == 'Tropics':
		schedule = format_tropics_flights(data)
	if sked_source == 'Air Department':
		schedule = format_airdept_flights(data)

	if st.session_state.format and isinstance(schedule, pd.DataFrame):
		with col3:	
			st.markdown("### DOT SCRIPT", help = 'Only major airports are currently mapped. Some DOT scripts will return the Airport code, especially if lesser used airports are included in the schedule')
			script = generate_script(schedule)
			st.markdown(script)
			
			tropics_column_order = [
			'Flight No',
			'From',
			'Dep Date',
			'Dep Time',
			'To',
			'Arr Date',
			'Arr Time',
			'Cabin Class', 
			'Layover Time',
			'Operating Airlines']
			
			airdept_column_order = [
			'Flight No',
			'From',
			'Dep Date',
			'Dep Time',
			'To',
			'Arr Date',
			'Arr Time',
			'Cabin Class', 
			'Operating Airlines']
			
			formatted_df = schedule[tropics_column_order] if sked_source == "Tropics" else schedule[airdept_column_order]
			st.markdown("#### Formatted Air Schedule",help="To make copy and pasting easier")
			st.markdown(formatted_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
	
		st.session_state.history.append({"timestamp": timestamp, "schedule": formatted_df, "script": script})
		
# Toggle to show/hide history
st.write("-" * 50)
show_history = st.checkbox("Show Previous Requests")

if show_history and st.session_state.history:
	st.subheader("Past Schedules")
	for idx, entry in enumerate(reversed(st.session_state.history), 1):
		st.markdown(f"Run Order: **{len(st.session_state.history) - idx + 1}**\n\nRuntime: **{entry['timestamp']}**")
		st.write("Formatted Schedule:")
		historic_df = pd.DataFrame(entry['schedule'])
		st.markdown(historic_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
		st.markdown("#### Script:")
		st.markdown(f"{entry['script']}")
		st.write("-" * 50)
