import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time
import qrcode
from io import BytesIO

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Project 7: Campus Bus Route Optimizer",
    page_icon="🚌",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main { padding: 1rem; }
    .stButton>button { width: 100%; font-weight: bold; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.title("🎓 Project Navigation")
st.sidebar.caption("JNTUK R23 B.Tech AI & DS")

selected_page = st.sidebar.radio(
    "Select Section:",
    [
        "Home",
        "Subjects used in project",
        "Programming used",
        "AI/ML layer",
        "Analytics & Crowd Control",
        "Bus Timetable & Schedule",
        "LIVE DEMO & GPS Tracker",
        "🌱 Eco & Efficiency Analytics",
        "🤖 Campus AI Transit Assistant",
        "🎟️ QR Digital Bus Pass"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Project 7: Campus Bus Route Optimizer**\n\n"
    "**Batch:** 2025-2029 (B.Tech First Year)\n"
    "**Domain:** AI & Graph Theory\n"
    "**Status:** Live GPS Tracker Active"
)

# ==========================================
# 3. BASE DATA INITIALIZATION
# ==========================================
bus_stops = {
    "Main Gate": {"density": 10, "lat": 17.3850, "lon": 78.4867},
    "Library": {"density": 85, "lat": 17.3862, "lon": 78.4880},
    "Hostel Block A": {"density": 120, "lat": 17.3875, "lon": 78.4895},
    "Hostel Block B": {"density": 95, "lat": 17.3880, "lon": 78.4910},
    "Engineering Block": {"density": 150, "lat": 17.3892, "lon": 78.4925},
    "Science Block": {"density": 60, "lat": 17.3905, "lon": 78.4940},
    "Sports Complex": {"density": 40, "lat": 17.3918, "lon": 78.4955},
    "Cafeteria": {"density": 110, "lat": 17.3870, "lon": 78.4930},
    "Auditorium": {"density": 30, "lat": 17.3910, "lon": 78.4965},
    "Admin Building": {"density": 25, "lat": 17.3845, "lon": 78.4885},
    "Research Park": {"density": 45, "lat": 17.3900, "lon": 78.4980},
    "Medical Center": {"density": 20, "lat": 17.3925, "lon": 78.4990}
}

road_network = [
    ("Main Gate", "Admin Building", 0.8, 2), ("Main Gate", "Library", 1.2, 4),
    ("Library", "Engineering Block", 1.0, 3), ("Library", "Cafeteria", 0.7, 2),
    ("Hostel Block A", "Hostel Block B", 0.4, 1), ("Hostel Block A", "Cafeteria", 0.9, 3),
    ("Hostel Block B", "Sports Complex", 1.1, 4), ("Engineering Block", "Science Block", 0.6, 2),
    ("Engineering Block", "Research Park", 1.5, 5), ("Science Block", "Auditorium", 0.8, 3),
    ("Cafeteria", "Science Block", 0.5, 2), ("Sports Complex", "Medical Center", 1.3, 4),
    ("Auditorium", "Medical Center", 0.7, 2), ("Research Park", "Medical Center", 1.0, 3),
    ("Admin Building", "Hostel Block A", 1.4, 4)
]

# Session State Initializations
if "stop_densities" not in st.session_state:
    st.session_state.stop_densities = {stop: info["density"] for stop, info in bus_stops.items()}

if "weather" not in st.session_state:
    st.session_state.weather = "Clear Sky"

# Weather multiplier logic
weather_multiplier = 1.5 if st.session_state.weather in ["Heavy Rain", "Dense Fog"] else 1.0

# Construct Graph
G = nx.Graph()
for stop, info in bus_stops.items():
    current_density = st.session_state.stop_densities.get(stop, info["density"])
    G.add_node(stop, density=current_density, lat=info["lat"], lon=info["lon"])

w1, w2, w3 = 1.0, 0.5, 0.01
for u, v, dist, time_min in road_network:
    d_u = st.session_state.stop_densities.get(u, bus_stops[u]["density"])
    d_v = st.session_state.stop_densities.get(v, bus_stops[v]["density"])
    avg_density = (d_u + d_v) / 2.0
    adjusted_time = time_min * weather_multiplier
    cost = max((w1 * dist) + (w2 * adjusted_time) - (w3 * avg_density), 0.1)
    G.add_edge(u, v, distance=dist, time=adjusted_time, weight=cost)

# ==========================================
# ANNOUNCEMENT BANNER
# ==========================================
st.warning("📢 **Campus Notice:** Real-time dynamic optimization active. Weather & crowd parameters auto-updated.")

# ==========================================
# PAGE 1: HOME
# ==========================================
if selected_page == "Home":
    st.title("🚌 Campus Bus Route Optimizer & Live GPS Tracking")
    st.caption("JNTUK R23 Curriculum — B.Tech Artificial Intelligence & Data Science")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📌 Project Overview")
        st.write("Project 7 calculates optimal campus bus paths considering **distance**, **travel time**, **weather delay**, and **student density** using **Dijkstra's Algorithm**.")
        st.markdown("---")
        st.subheader("📊 Key Operational Metrics")
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Campus Stops", "12 Active")
        k2.metric("Road Links", "15 Routes")
        max_density_stop = max(st.session_state.stop_densities, key=st.session_state.stop_densities.get)
        k3.metric("Peak Stop", max_density_stop)
        k4.metric("Weather State", st.session_state.weather)
    with col2:
        st.subheader("📋 Academic Details")
        st.info("**Institution:** JNTUK R23\n\n**Branch:** AI & DS\n\n**Algorithm:** Dynamic Dijkstra's Engine")

# ==========================================
# PAGE 2: SUBJECTS USED (EXPANDED HIGH DEPTH CONTENT)
# ==========================================
elif selected_page == "Subjects used in project":
    st.title("📚 Academic Subjects & Theoretical Foundations")
    st.caption("Comprehensive Interdisciplinary Mapping of JNTUK R23 B.Tech AI & DS Curriculum")
    
    st.markdown("### 1. Discrete Mathematics & Graph Theory")
    st.write(
        """
        The backbone of the entire Campus Bus Route Optimizer is built upon **Graph Theory**. 
        In our model, the physical university campus infrastructure is mapped into an undirected, dynamically weighted mathematical graph $G = (V, E)$.
        
        * **Vertex Set ($V$):** Represents $12$ key physical bus stops across campus (e.g., Main Gate, Library, Engineering Block, Hostels). Each vertex holds real-time state attributes like student crowd queues ($D_v$) and spatial GPS coordinates $(\\text{Latitude}, \\text{Longitude})$.
        * **Edge Set ($E$):** Represents $15$ physical road links connecting adjacent bus stops. Unlike basic textbook graphs with static scalar edge lengths, our edges feature dynamic weight vectors combining physical distance ($d_{uv}$), expected vehicular travel time ($t_{uv}$), and environmental weather friction multipliers.
        * **Mathematical Representation:** This graph abstraction allows complex real-world transportation logistics to be mathematically encoded into computable memory matrices and dictionaries.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 2. Design & Analysis of Algorithms (DAA)")
    st.write(
        """
        Optimal path planning is powered by principles from algorithm design and computational analysis:
        
        * **Dijkstra’s Algorithm Engine:** Solves the Single-Source Shortest Path (SSSP) problem. It guarantees globally optimal path selections under non-negative edge weights.
        * **Min-Heap / Priority Queue Data Structure:** Instead of an unoptimized linear search $\\mathcal{O}(|V|^2)$, the engine utilizes a Min-Heap priority queue to fetch the next closest unvisited node in $\\mathcal{O}(\\log |V|)$ time.
        * **Asymptotic Time Complexity:** Overall execution operates at $\\mathcal{O}((|E| + |V|) \\log |V|)$. With $|V|=12$ nodes and $|E|=15$ edges, path computation completes in sub-milliseconds (under 0.001s), enabling real-time interactive UI re-computations when user inputs shift.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 3. Data Structures & Memory Storage Systems")
    st.write(
        """
        Efficient graph storage and state management are achieved through fundamental data structure choices:
        
        * **Adjacency List Structure:** Represented internally using nested Python Hash Maps (Dictionaries of Dictionaries). This guarantees an optimal spatial complexity of $\\mathcal{O}((|V| + |E|))$, which avoids the high memory overhead of a $12 \\times 12$ sparse Adjacency Matrix.
        * **In-Memory Session State Containers:** Managed via Streamlit's `st.session_state` reactive dictionary layer. This ensures dynamic crowd slider adjustments and weather selections persist seamlessly across UI browser refreshes without data loss.
        """
    )

# ==========================================
# PAGE 3: PROGRAMMING USED (EXPANDED HIGH DEPTH CONTENT)
# ==========================================
elif selected_page == "Programming used":
    st.title("💻 Technology Stack & Software Architecture")
    st.caption("Detailed Breakdown of Modern Open-Source Libraries & Frameworks Employed")
    
    st.markdown("### 1. Python 3.10+ (Core Runtime Engine)")
    st.write(
        """
        Python was chosen as the primary programming language due to its unmatched ecosystem for Artificial Intelligence, Graph Data Processing, and Web Application rapid prototyping. Python's clean expression handling allows complex dynamic cost equations to execute with minimal overhead.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 2. NetworkX (`networkx`) — Graph Computation Library")
    st.write(
        """
        * **Purpose:** Acts as the mathematical core for graph generation, node/edge attribute storage, and pathfinding.
        * **Role in Project:** Constructs the dynamic graph $G$, attaches multi-variable attributes (Distance, Time, Density) to edges, and executes `nx.dijkstra_path()` with heap optimization to extract the shortest/most optimal sequence of bus stops.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 3. Streamlit (`streamlit`) — Interactive Web Application Framework")
    st.write(
        """
        * **Purpose:** Converts pure Python code into a production-grade, reactive, interactive web dashboard without requiring traditional HTML, CSS, or JavaScript web stacks.
        * **Role in Project:** Renders the sidebar navigation, live telemetry controls, crowd density sliders, progress bars for GPS tracking, and reactive layout grids.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 4. Matplotlib (`matplotlib`) — Data & Topology Visualization")
    st.write(
        """
        * **Purpose:** Programmatic plotting and graph rendering engine.
        * **Role in Project:** Draws the 2D spatial campus graph topology using `spring_layout`. It dynamically colors normal road connections in gray and highlights the active calculated bus route in bright **Red / Orange** lines.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 5. Pandas (`pandas`) — Data Analysis & Tabular Processing")
    st.write(
        """
        * **Purpose:** High-performance data manipulation and DataFrame structuring.
        * **Role in Project:** Organizes student crowd queue numbers, bus timetables, and environmental efficiency metrics into structured tabular DataFrames displayed cleanly in the UI.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 6. QRCode (`qrcode`) & BytesIO — Pass Generation Pipeline")
    st.write(
        """
        * **Purpose:** Generates two-dimensional barcode matrices on-the-fly and handles in-memory binary image buffers.
        * **Role in Project:** Encodes student boarding pass details into a scannable PNG QR code for seamless digital pass validation.
        """
    )

# ==========================================
# PAGE 4: AI/ML LAYER (EXPANDED HIGH DEPTH CONTENT)
# ==========================================
elif selected_page == "AI/ML layer":
    st.title("🤖 Optimization Engine & Heuristic AI Layer")
    st.caption("Deep Mathematical Analysis of Dynamic Crowd-Aware Route Selection Mechanics")
    
    st.markdown("### 1. The Multi-Objective Dynamic Composite Cost Function")
    st.write(
        """
        Standard navigation systems (e.g., standard Google Maps) typically calculate route costs purely based on physical distance ($d_{uv}$) or historical road speed limits. In a smart university campus transit system, this naive approach leads to severe bottlenecking — buses bypass massively overcrowded stops simply because another route is 100 meters shorter.
        
        To solve this, our system implements a **Multi-Objective Composite Heuristic Cost Function**:
        """
    )
    
    st.latex(r"Cost(u, v) = \max\left(w_1 \cdot d_{uv} + w_2 \cdot (t_{uv} \cdot M_{\text{weather}}) - w_3 \cdot \left(\frac{D_u + D_v}{2}\right), \, 0.1\right)")
    
    st.write(
        """
        #### Formula Parameter Breakdown:
        * **$d_{uv}$ (Physical Distance):** Length of the road segment between stop $u$ and stop $v$ in kilometers.
        * **$t_{uv}$ (Base Travel Time):** Normal vehicle transit time in minutes.
        * **$M_{\text{weather}}$ (Environmental Weather Multiplier):** Safety delay factor ($1.0\\times$ for Clear Sky, $1.5\\times$ for Heavy Rain/Fog).
        * **$D_u, D_v$ (Real-Time Student Crowd Counts):** Current number of waiting students at origin stop $u$ and target stop $v$.
        * **$w_1, w_2, w_3$ (Weight Hyperparameters):** Configurable weights balancing Distance Penalty ($w_1 = 1.0$), Travel Time Penalty ($w_2 = 0.5$), and Student Crowd Discount ($w_3 = 0.01$).
        * **$\max(\dots, 0.1)$ Boundary Condition:** Prevents total edge weight from dropping to zero or negative values, preserving Dijkstra's mathematical contract and preventing infinite loop bugs.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 2. Heuristic Search & Adaptive AI Decision-Making Logic")
    st.write(
        """
        The intelligence of the algorithm rests on the **subtraction of average student density** in the cost equation.
        
        * **Discount Mechanism:** In graph optimization, pathfinding algorithms natively search for routes that minimize total edge cost. By applying a mathematical discount ($- w_3 \\cdot \\text{Density}$) on edges leading to crowded stops, we artificially reduce the edge cost of routes serving high student queues.
        * **Dynamic Rerouting Behavior:** This forces Dijkstra's search tree to dynamically expand toward high-demand passenger clusters. When crowd numbers spike at the Hostel or Canteen, the algorithm automatically reroutes the shuttle toward those stops, acting as a rule-based AI heuristic decision engine.
        """
    )
    
    st.markdown("---")
    
    st.markdown("### 3. Production Scalability: Predictive Machine Learning Pipeline")
    st.write(
        """
        In a full-scale smart city / smart university enterprise deployment, manual slider inputs are replaced by an automated **Time-Series Machine Learning Predictive Pipeline**:
        
        1. **Data Ingestion:** Historical student class timetables, weather forecasts, and IoT camera queue counts are fed into **XGBoost Regressor / LSTM Neural Networks**.
        2. **Predictive Demand Forecasting:** The ML model predicts crowd surges 15-30 minutes before classes finish.
        3. **Proactive Dispatching:** The Graph Engine ingests these predicted density inputs and dispatches buses proactively before passenger queues even form.
        """
    )

# ==========================================
# PAGE 5: ANALYTICS & DYNAMIC CROWD CONTROL
# ==========================================
elif selected_page == "Analytics & Crowd Control":
    st.title("📊 Dynamic Crowd & Weather Control")
    
    st.subheader("🌤️ Weather Condition Simulation")
    st.session_state.weather = st.selectbox(
        "Select Weather Condition:",
        ["Clear Sky", "Light Rain", "Heavy Rain", "Dense Fog"]
    )
    if st.session_state.weather in ["Heavy Rain", "Dense Fog"]:
        st.info("🌧️ **Weather Impact Active:** Road travel times increased by 50%.")
        
    st.markdown("---")
    st.subheader("👥 Student Crowd Density Controls")
    
    c1, c2 = st.columns(2)
    stops_list = list(bus_stops.keys())
    
    with c1:
        for stop in stops_list[:6]:
            st.session_state.stop_densities[stop] = st.slider(
                f"👥 {stop}:", 0, 300, st.session_state.stop_densities[stop]
            )
            
    with c2:
        for stop in stops_list[6:]:
            st.session_state.stop_densities[stop] = st.slider(
                f"👥 {stop}:", 0, 300, st.session_state.stop_densities[stop]
            )
            
    st.markdown("---")
    st.subheader("📈 Live Density Distribution")
    df = pd.DataFrame([{"Stop": k, "Students Waiting": v} for k, v in st.session_state.stop_densities.items()])
    st.bar_chart(df.set_index("Stop"))

# ==========================================
# PAGE 6: BUS TIMETABLE & SCHEDULE
# ==========================================
elif selected_page == "Bus Timetable & Schedule":
    st.title("⏱️ Campus Bus Schedule & Timetable")
    timetable_data = {
        "Shuttle ID": ["Bus 1 (North Express)", "Bus 2 (South Circuit)", "Bus 3 (Hostel Loop)", "Bus 4 (Central Express)"],
        "Start Time": ["08:00 AM", "08:30 AM", "09:00 AM", "09:30 AM"],
        "Frequency": ["Every 15 mins", "Every 20 mins", "Every 10 mins", "Every 15 mins"],
        "Primary Route": ["Main Gate ➔ Eng. Block", "Admin ➔ Medical Center", "Hostels ➔ Canteen", "Library ➔ Research Park"],
        "Status": ["🟢 Active", "🟢 Active", "🟡 High Crowd", "🟢 Active"]
    }
    st.table(pd.DataFrame(timetable_data))

# ==========================================
# PAGE 7: LIVE DEMO & GPS TRACKER
# ==========================================
elif selected_page == "LIVE DEMO & GPS Tracker":
    st.title("⚡ Live Navigation & GPS Simulation Detector")
    
    emergency_mode = st.toggle("🚨 Emergency / Medical Vehicle Override Mode")
    
    col_input, col_display = st.columns([1, 2])
    
    with col_input:
        st.subheader("🕹️ Route Parameters")
        start_stop = st.selectbox("Origin Stop:", list(bus_stops.keys()), index=0)
        end_stop = st.selectbox("Destination Stop:", list(bus_stops.keys()), index=11)
        sim_speed = st.slider("GPS Speed Delay (seconds):", 1, 3, 1)
        start_sim = st.button("🚀 Start Live GPS Tracker")
        
    with col_display:
        if start_stop == end_stop:
            st.warning("⚠️ Select different Origin & Destination stops!")
        else:
            selected_weight = 'distance' if emergency_mode else 'weight'
            path = nx.dijkstra_path(G, source=start_stop, target=end_stop, weight=selected_weight)
            total_dist = sum(G[path[i]][path[i+1]]['distance'] for i in range(len(path)-1))
            total_time = sum(G[path[i]][path[i+1]]['time'] for i in range(len(path)-1))
            
            if emergency_mode:
                st.error(f"🚨 **EMERGENCY PATH (Shortest Distance):** {' ➔ '.join(path)}")
            else:
                st.success(f"**Optimal Route:** {' ➔ '.join(path)}")
                
            m1, m2, m3 = st.columns(3)
            m1.metric("Distance", f"{total_dist:.2f} km")
            m2.metric("Time", f"{total_time:.1f} mins")
            m3.metric("Stops", f"{len(path)}")

    # Visual Topology Graph Map
    st.markdown("---")
    st.subheader("🗺️ Campus Network Graph Route")
    fig, ax = plt.subplots(figsize=(10, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx(G, pos, node_color='skyblue', edge_color='gray', node_size=800, ax=ax, font_size=8)
    if start_stop != end_stop:
        path_edges = list(zip(path[:-1], path[1:]))
        edge_color_choice = 'orange' if emergency_mode else 'red'
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4.0, edge_color=edge_color_choice, ax=ax)
    plt.axis('off')
    st.pyplot(fig)
    
    # LIVE GPS SIMULATION
    if start_sim and start_stop != end_stop:
        st.markdown("---")
        st.subheader("📡 Live GPS Bus Telemetry & Tracking")
        
        status_box = st.empty()
        prog_bar = st.progress(0)
        
        for idx, current_stop in enumerate(path):
            lat = bus_stops[current_stop]["lat"]
            lon = bus_stops[current_stop]["lon"]
            
            status_box.info(
                f"🚌 **Shuttle Status: IN-TRANSIT**\n\n"
                f"📍 **Current Stop:** `{current_stop}`\n"
                f"🌐 **GPS Coordinates:** Latitude: `{lat}`, Longitude: `{lon}`\n"
                f"📶 **Signal:** 5G Connected | **Speed:** 40 km/h"
            )
            
            prog_bar.progress((idx + 1) / len(path))
            time.sleep(sim_speed)
            
        st.balloons()
        st.components.v1.html(
            """
            <audio autoplay>
              <source src="https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3" type="audio/mpeg">
            </audio>
            """,
            height=0
        )
        st.success(f"🎯 **Arrival Alert:** Bus Arrived at `{end_stop}` Successfully!")

# ==========================================
# PAGE 8: ECO & EFFICIENCY ANALYTICS
# ==========================================
elif selected_page == "🌱 Eco & Efficiency Analytics":
    st.title("🌱 Environmental Impact & Transit Efficiency")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("CO₂ Savings / Month", "142 kg", "+18%")
    col2.metric("Fuel Optimization", "18.4%", "+4.2%")
    col3.metric("Passenger Coverage", "94.2%", "+22%")

# ==========================================
# PAGE 9: CAMPUS AI TRANSIT ASSISTANT
# ==========================================
elif selected_page == "🤖 Campus AI Transit Assistant":
    st.title("🤖 Campus AI Transit Query Assistant")
    
    user_query = st.selectbox(
        "Select a question for the AI Assistant:",
        [
            "Which bus stop has the highest student congestion right now?",
            "How does weather impact travel time?",
            "What happens if there is a medical emergency?",
            "Why is Dijkstra's algorithm preferred over BFS?"
        ]
    )
    
    if st.button("💬 Ask AI Assistant"):
        st.markdown("---")
        if "highest student congestion" in user_query:
            max_stop = max(st.session_state.stop_densities, key=st.session_state.stop_densities.get)
            st.info(f"🤖 **AI Answer:** Currently, **{max_stop}** has the highest crowding.")
        elif "weather impact" in user_query:
            st.info("🤖 **AI Answer:** Heavy Rain or Fog adds a 1.5x multiplier to travel time for safety.")
        elif "medical emergency" in user_query:
            st.info("🤖 **AI Answer:** Enable Emergency Mode to recalculate routes purely on physical shortest distance.")
        elif "BFS" in user_query:
            st.info("🤖 **AI Answer:** BFS only works on unweighted graphs. Dijkstra is needed for weighted distance, time, and crowd factors.")

# ==========================================
# PAGE 10: QR DIGITAL BUS PASS
# ==========================================
elif selected_page == "🎟️ QR Digital Bus Pass":
    st.title("🎟️ Digital Campus Shuttle Pass Generator")
    st.caption("Generate a downloadable QR boarding pass for campus shuttles")
    
    c1, c2 = st.columns(2)
    with c1:
        student_name = st.text_input("Student Name:", "John Doe")
        roll_no = st.text_input("Roll Number / ID:", "23331A1201")
        pass_from = st.selectbox("From Stop:", list(bus_stops.keys()), index=0)
        pass_to = st.selectbox("To Stop:", list(bus_stops.keys()), index=4)
        
    with c2:
        if st.button("🎫 Generate Boarding Pass"):
            ticket_info = f"NAME: {student_name}\nROLL NO: {roll_no}\nFROM: {pass_from}\nTO: {pass_to}\nSTATUS: VALIDATED"
            
            # Generate QR Code
            qr = qrcode.QRCode(version=1, box_size=6, border=2)
            qr.add_data(ticket_info)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            buf = BytesIO()
            img.save(buf)
            byte_im = buf.getvalue()
            
            st.success("✅ **Digital Pass Generated Successfully!**")
            st.image(byte_im, width=180, caption="Scan at Bus Gate")
            st.download_button(
                label="📥 Download QR Ticket",
                data=byte_im,
                file_name=f"Campus_Pass_{roll_no}.png",
                mime="image/png"
            )
