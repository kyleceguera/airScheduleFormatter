import pandas as pd, streamlit as st, re, datetime
from datetime import datetime

current_year = datetime.now().year

#append year based on derived date from df - needed for sked from air dept
def adjust_date(x):
    current_date = datetime.now()
    
    # Convert the DDMMM part into a date with current year
    date_with_current_year = pd.to_datetime(f"{x}{current_year}", format='%d%b%Y')
    
    # If the date is already past the current date, append next year
    if date_with_current_year < current_date:
        return f"{x}{current_year + 1}"
    else:
        return f"{x}{current_year}"

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
	'MCI': 'Kansas City(MO)',
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
    "5J": "Cebu Pacific Air",
    "9K": "Cape Air",
    "9W": "Jet Airways",
    "A3": "Aegean Airlines",
    "A4": "Allegiant Air",
	"AA": "American Airlines",
    "AC": "Air Canada",
    "AF": "Air France",
    "AI": "Air India",
    "AM": "Aeroméxico",
    "AR": "Aerolíneas Argentinas",
    "AS": "Alaska Airlines",
    "AV": "Avianca",
    "AY": "Finnair",
    "AZ": "ITA Airways",
    "B6": "JetBlue Airways",
    "BA": "British Airways",
    "BT": "airBaltic",
    "CA": "Air China",
    "CI": "China Airlines",
    "CM": "Copa Airlines",
    "CX": "Cathay Pacific Airways",
    "CZ": "China Southern Airlines",
    "D8": "Norwegian Air International",
    "DL": "Delta Air Lines",
    "DY": "Norwegian Air Shuttle",
    "EI": "Aer Lingus",
    "EK": "Emirates",
    "ET": "Ethiopian Airlines",
    "EY": "Etihad Airways",
    "FZ": "Flydubai",
    "FI": "Icelandair",
    "FR": "Ryanair",
    "G3": "Gol Linhas Aéreas",
    "GA": "Garuda Indonesia",
    "GF": "Gulf Air",
    "HA": "Hawaiian Airlines",
    "HG": "Niki",
    "HR": "Hahn Air",
    "IB": "Iberia",
    "JL": "Japan Airlines",
    "JJ": "LATAM Airlines Brazil",
    "KE": "Korean Air",
    "KL": "KLM Royal Dutch Airlines",
    "KU": "Kuwait Airways",
    "LA": "LATAM Airlines Group",
    "LH": "Lufthansa",
    "LO": "LOT Polish Airlines",
    "LY": "El Al",
    "ME": "Middle East Airlines",
    "MH": "Malaysia Airlines",
    "MS": "EgyptAir",
    "NH": "All Nippon Airways",
    "NZ": "Air New Zealand",
    "OK": "Czech Airlines",
    "OO": "SkyWest Airlines",
    "OS": "Austrian Airlines",
    "OZ": "Asiana Airlines",
    "PC": "Pegasus Airlines",
    "PK": "Pakistan International Airlines",
    "PR": "Philippine Airlines",
    "PS": "Ukraine International Airlines",
    "QR": "Qatar Airways",
    "QF": "Qantas Airways",
    "RO": "TAROM",
    "RS": "Air Seoul",
    "S7": "S7 Airlines",
    "SA": "South African Airways",
    "SK": "SAS Scandinavian Airlines",
    "SQ": "Singapore Airlines",
    "SU": "Aeroflot",
    "SV": "Saudia",
    "SZ": "Somon Air",
    "TG": "Thai Airways",
    "TK": "Turkish Airlines",
    "TP": "TAP Air Portugal",
    "U2": "easyJet",
    "UA": "United Airlines",
    "VA": "Virgin Australia",
    "VN": "Vietnam Airlines",
    "VY": "Vueling Airlines",
    "VS": "Virgin Atlantic",
    "WS": "WestJet",
    "WN": "Southwest Airlines",
    "WY": "Oman Air",
    "X3": "TUIfly",
    "YX": "Republic Airways",
    "ZB": "Monarch Airlines",
    "ZH": "Shenzhen Airlines"
}

st.set_page_config(layout='wide', page_title='Air Schedule Tool', page_icon=":airplane_arriving:")
st.title("Flight Schedule Formatting Tool")

display_price = 0

if 'format' not in st.session_state:
	st.session_state.format = False
	
if 'history' not in st.session_state:
	st.session_state.history = []
	
if 'text' not in st.session_state:
	st.session_state.text = ""
	
if 'price' not in st.session_state:
	st.session_state.price = ""
	
if 'widget' not in st.session_state:
	st.session_state.widget = ""

col1, col2, col3 = st.columns([0.34, 0.05, 0.561])

st.markdown(
	"""
	<style>
	.stButton>button {
		background-color: #2E8B57; 
		color: white;
		border-radius: 10px;
		height: 2vh;  /* 5% of the viewport height */
		width: 4vw;  /* 20% of the viewport width */
		min-height: 2em;  /* Ensure there's a minimum height */
		min-width: 10em;   /* Ensure there's a minimum width */
		font-size: 10px;
		font-size: 1.4vw;
		text-wrap: pretty;
		line-height: 15px
	}
	.stButton>button:hover {
		background-color: #216640; 
		color: white;
		border-radius: 10px;
		height: 2vh;  /* 5% of the viewport height */
		width: 4vw;  /* 20% of the viewport width */
		min-height: 2em;  /* Ensure there's a minimum height */
		min-width: 10em;   /* Ensure there's a minimum width */
		font-size: 10px;
		font-size: 1.4vw;
		text-wrap: pretty;
		line-height: 15px
	}
	.stButton>button:active {
		background-color: #388E3C; /* Change background color when button is clicked */
		transform: scale(0.95); /* Slightly shrink the button on click */
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Add shadow when clicked */
	}
	.stButton>button:focus:not(:active) {
		background-color: #808080;
		outline: none; /* Remove the outline */
		color: white;
		height: 2vh;  /* 5% of the viewport height */
		width: 4vw;  /* 20% of the viewport width */
		min-height: 2em;  /* Ensure there's a minimum height */
		min-width: 10em;   /* Ensure there's a minimum width */
		font-size: 10px;
		font-size: 1.4vw;
		text-wrap: pretty;
		line-height: 15px
	}
	</style>
	""",
	unsafe_allow_html=True
)

def clear_text():
	st.session_state.text = ""
	st.session_state.price = st.session_state.widget
	st.session_state.widget = ""
	
with col1:
	sked_source = st.selectbox(label='Schedule Source - Where did you get your schedule from?',options=['Tropics', 'Air Department'], placeholder='Tropics', help="Selection dictates how the schedule gets parsed")
	st.write("Paste your schedule below and the software will format it for you.")
	data = st.text_area(label='inputted schedule',label_visibility='collapsed', height=250, value=st.session_state.text)
	st.session_state.text = data
	recordPrice = st.toggle('**OPTIONAL - CAPTURE PRICE**\n\nUsed only to show price at time of formatting (when looking through previous requests)')
	if recordPrice:
		price_inputted = st.text_input('Schedule Price - per person',help="Price must be inputted before formatting otherwise it will not be captured", key = 'widget', placeholder=0)
		if price_inputted:
			if re.search(r'[a-zA-Z]', price_inputted):  # This regex allows only numbers and periods
				st.warning("Please enter a valid price without any letters.")
			else:
				# Optionally, you can further process the price here (like removing commas, etc.)
				price = re.sub(r'[^0-9.]', '', price_inputted)
		else:
			price = False
	else:
		price = False
	st.write('')
	st.write('')
	subcol1, subcol2 = st.columns([0.5, 0.5])
	with subcol1:
		format = st.button("Format Flight Schedule"	)
	with subcol2:
		if st.button('Clear', key='clear_button', on_click= clear_text):
			pass

def format_airdept_flights(text):
	air_dept_pattern = r'^\s*([A-Za-z]{2}\d{1,5})\s+([A-Za-z])\s+([A-Za-z]+(?:\s[A-Za-z]+)*)\s+([A-Za-z]{3})\s+([A-Za-z]{3})\s+([0-9]{2}[A-Za-z]{3})\s+([0-9]{4})\s+([0-9]{2}[A-Za-z]{3})\s+([0-9]{4})\s+([A-Za-z]{2})\s+(?:0\s+)?([A-Za-z\s]+)\s*$'
	flights = text.replace(",",'').strip().split("\n")
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
	df['Dep Date'] = pd.to_datetime(df['Dep Date'].apply(lambda x: adjust_date(x) if len(x) == 5 else x), format='%d%b%Y')
	df['Dep Date'] = df['Dep Date'].dt.strftime('%d-%b-%Y')
	df['Arr Date'] = pd.to_datetime(df['Arr Date'].apply(lambda x: adjust_date(x) if len(x) == 5 else x), format='%d%b%Y')
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
	df['Operating Airlines'] = df['Operating Airlines'].apply(lambda x: airlines.get(x, x))
	return df

def format_tropics_flights(text):
	tropics_pattern = r'^\s*([A-Za-z]{2}\d{1,5})\s+([A-Za-z])\s+([A-Za-z]{3})\s+([A-Za-z]{3})\s+(\d{2}-[A-Za-z]{3}-\d{4})\s+(\d{2}:\d{2})\s+(\d{2}-[A-Za-z]{3}-\d{4})\s+(\d{2}:\d{2})\s+([A-Za-z]+(?:\s(?!non\s)[A-Za-z]+)?)\s+((?:non\s+stop|[A-Za-z\s]+))\s+(\d{1,2}[hH]\s*\d{1,2}[mM]|\d{1,2}[mM])\s+([A-Za-z\s\-]+)\s*$'
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
	df['DepDate'] = pd.to_datetime(df['Dep Date'], format='%d-%b-%Y')
	df['ArrDate'] = pd.to_datetime(df['Arr Date'], format='%d-%b-%Y')

	# Iterate through rows and compare with previous row
	for index in range(len(df) - 1):
		# Calculate the time difference between the current row's 'Arr Date' and the previous row's 'Arr Date'
		date_diff = (df.at[index+1, 'ArrDate'] - df.at[index, 'ArrDate'])
		date_diff = abs(date_diff)
		if date_diff > pd.Timedelta(days=1):
			df.at[index, 'Layover Time'] = ''  # or np.nan
	df.at[len(df) - 1, 'Layover Time'] = ''  # or np.nan
		
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
		if i==0:  #we know this is the first segment
			script_open = f"We're able to offer:\n\n"
		elif i == df.index[-1]:
			script_open = f'Our final leg would be '
		elif abs((current_segment_date - previous_segment_date).days) > 5:
			script_open = f'On the return we have'
		elif abs((current_segment_date - previous_segment_date).days) <= 2 :
			script_open = f'This flight would connect to'
			
		# Update previous_segment_date after the check
		previous_segment_date = current_segment_date
		
		# Append the script_open to the overall script
		script += (script_open + f" **{airline}** flight **{row['Flight Number']}** departing from **{departure_city}** on **{row['Dep Date']}** at **{dep_time}** and arriving into **{arrival_city}** on **{row['Arr Date']}** at **{arr_time}**. This flight is operated by *{operating_airlines}*. \n\n")
		
	return script

if format and data:
	timestamp = datetime.now()
	st.session_state.format = True
	if sked_source == 'Tropics':
		try:
			schedule = format_tropics_flights(data)
		except Exception as e:
			with col3:
				st.warning(f"Something went wrong while trying to parse flights:\n\n{e}")
				st.stop()
	if sked_source == 'Air Department':
		try:
			schedule = format_airdept_flights(data)
		except Exception as e:
			with col3:
				st.warning(f"Something went wrong while trying to parse flights:\n\n{e}")
				st.stop()

	if st.session_state.format and isinstance(schedule, pd.DataFrame):
		with col3:	
			st.markdown("### DOT SCRIPT", help = 'Only major airports are currently mapped. Some DOT scripts will return the Airport code, especially if lesser used airports are included in the schedule')
			try:
				script = generate_script(schedule)
				st.markdown(script)
				
				st.markdown(
					"<h5 style='color:red;'>Airfare is subject to rate change and availability until your reservation is confirmed with air deposit.</h5>",
					unsafe_allow_html=True
				)
				
				tropics_column_order = [
				'Flight No',
				'From',
				'To',
				'Dep Date',
				'Dep Time',
				'Arr Date',
				'Arr Time',
				'Cabin Class', 
				'Layover Time',
				'Operating Airlines']
				
				airdept_column_order = [
				'Flight No',
				'From',
				'To',
				'Dep Date',
				'Dep Time',
				'Arr Date',
				'Arr Time',
				'Cabin Class', 
				'Operating Airlines']
				
				formatted_df = schedule[tropics_column_order] if sked_source == "Tropics" else schedule[airdept_column_order]
				
				# Convert the DataFrame to HTML with inline CSS to force gridlines
				html_table = formatted_df.to_html(classes='custom-table1 table-bordered', index=False)

				# Custom CSS for gridlines
				css1 = """
					<style>
						.custom-table1 {
							border: 2px solid black;
							border-collapse: collapse;
							margin-left: auto;
							margin-right: auto;
						}
						.custom-table1 th, .custom-table1 td {
							border: 1px solid black;
							padding: 8px;
							text-align: center;  /* Center align text in both th and td */
						}
					</style>
				"""
				# Render the DataFrame with gridlines in Streamlit
				st.markdown(css1, unsafe_allow_html=True)
				st.markdown(html_table, unsafe_allow_html=True)
	
				st.session_state.history.append({"timestamp": timestamp, "schedule": formatted_df, "script": script, "price": float(price) if price else ''})
		
			except Exception as e:
					st.error(f"There was an error with formatting the provided schedule or generating the DOT Script. Please review the schedule inputted to ensure its copied/pasted correctly and the correct schedule source is selected. \n\nErrorMessage: {e}")
					st.markdown("Based on what was provided, the current output for the schedule is:")
					st.dataframe(schedule)

# Toggle to show/hide history
st.write("-" * 50)
show_history = st.checkbox("Show Previous Requests")

if show_history and st.session_state.history:
	st.subheader("Past Schedules")
	for idx, entry in enumerate(reversed(st.session_state.history), 1):
		st.markdown(f"Run Order: **{len(st.session_state.history) - idx + 1}**\n\nRuntime: **{entry['timestamp']}**")
		if isinstance(entry['price'], float):
			formatted_price = f"Price Inputted at Time of Formatting: **${entry['price']:,.2f}**"
		else:
			formatted_price = 'No price inputted at time of formatting'
		st.markdown(formatted_price)
		st.markdown("##### Formatted Schedule:")
		historic_df = pd.DataFrame(entry['schedule'])
		historic_html = historic_df.to_html(classes='custom-table2 table-bordered', index=False)
		# Custom CSS for gridlines
		css2 = """
			<style>
				.custom-table2 {
					border: 2px solid black;
					border-collapse: collapse;
					align: left;
				}
				.custom-table2 th, .custom-table2 td {
					border: 1px solid black;
					padding: 8px;
					text-align: center;  /* Center align text in both th and td */
				}
				.st-emotion-cache-1h9usn1 {
					margin-bottom: 0px;
					margin-top: 0px;
					margin-left: 0px;
					width: 70%;
					border-style: solid;
					border-width: 1px;
					border-color: rgba(49, 51, 63, 0.2);
					border-radius: 0.5rem;
				}
			</style>
		"""
		# Render the DataFrame with gridlines in Streamlit
		st.markdown(css2, unsafe_allow_html=True)
		st.markdown(historic_html, unsafe_allow_html=True)
		previous_script = st.expander('Auto-generated script')
		previous_script.write(f"#### Script: \n\n{entry['script']}")
		previous_script.markdown(
				"<h5 style='color:red;'>Airfare is subject to rate change and availability until your reservation is confirmed with air deposit.</h5>",
				unsafe_allow_html=True
			)
		st.write("-" * 50)
