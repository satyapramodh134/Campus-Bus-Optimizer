import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time

# ==========================================
# 1. PAGE CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Project 7: Campus Bus Route Optimizer",
    page_icon="🚌",
    layout="wide"
)

# Custom Styling (Pro UI Theme)
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
        "LIVE DEMO & GPS Tracker"
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

# Session State for Dynamic Density Sliders
if "stop_densities" not in st.session_state:
    st.session_state.stop_densities = {stop: info["density"] for stop, info in bus_stops.items()}

# Construct Graph with Dynamic Densities
G = nx.Graph()
for stop, info in bus_stops.items():
    current_density = st.session_state.stop_densities.get(stop, info["density"])
    G.add_node(stop, density=current_density, lat=info["lat"], lon=info["lon"])

w1, w2, w3 = 1.0, 0.5, 0.01
for u, v, dist, time_min in road_network:
    d_u = st.session_state.stop_densities.get(u, bus_stops[u]["density"])
    d_v = st.session_state.stop_densities.get(v, bus_stops[v]["density"])
    avg_density = (d_u + d_v) / 2.0
    cost = max((w1 * dist) + (w2 * time_min) - (w3 * avg_density), 0.1)
    G.add_edge(u, v, distance=dist, time=time_min, weight=cost)

# ==========================================
# PAGE 1: HOME
# ==========================================
if selected_page == "Home":
    st.title("🚌 Campus Bus Route Optimizer & Live GPS Tracking")
    st.caption("JNTUK R23 Curriculum — B.Tech Artificial Intelligence & Data Science")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📌 Project Overview")
        st.write("Project 7 calculates optimal campus bus paths considering **distance**, **travel time**, and **student density** using **Dijkstra's Algorithm**.")
        st.markdown("---")
        st.subheader("📊 Key Operational Metrics")
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Campus Stops", "12 Active")
        k2.metric("Road Links", "15 Routes")
        max_density_stop = max(st.session_state.stop_densities, key=st.session_state.stop_densities.get)
        k3.metric("Peak Stop", max_density_stop)
        k4.metric("GPS Sync", "Real-Time")
    with col2:
        st.subheader("📋 Academic Details")
        st.info("**Institution:** JNTUK R23\n\n**Branch:** AI & DS\n\n**Algorithm:** Dynamic Dijkstra's Engine")

# ==========================================
# PAGE 2: SUBJECTS USED
# ==========================================
elif selected_page == "Subjects used in project":
    st.title("📚 Academic Subjects & Theoretical Foundations")
    st.caption("Interdisciplinary Application of JNTUK R23 B.Tech AI & DS Curriculum")
    
    st.subheader("1. Graph Theory & Discrete Mathematics")
    st.write(
        """
        The foundational layer of the Campus Bus Route Optimizer relies on **Graph Theory**. 
        A university campus is modeled as a connected, non-directed, weighted graph $G = (V, E)$, 
        where the vertex set $V$ represents physical bus stops ($|V| = 12$) and the edge set $E$ represents road links ($|E| = 15$). 
        
        Unlike standard graphs with static scalar weights, our graph assigns dynamic vector properties to both vertices and edges. 
        Each node $v \\in V$ encapsulates geographical spatial coordinates $(\\text{Lat}, \\text{Lon})$ and real-time student queue densities ($D_v$). 
        Each edge $e = (u, v) \\in E$ captures physical length ($d_{uv}$) and average vehicle travel duration ($t_{uv}$). 
        This structural abstraction enables the conversion of complex physical campus transit problems into computable matrix representations.
        """
    )
    
    st.markdown("---")
    
    st.subheader("2. Design & Analysis of Algorithms (DAA)")
    st.write(
        """
        Routing efficiency is governed by algorithmic pathfinding. We implement **Dijkstra’s Algorithm** using a **Priority Queue (Min-Heap)** 
        data structure to solve the single-source shortest path problem on dynamically weighted edges. 
        
        By maintaining a tentative distance array and iteratively relaxing adjacent edges, the algorithm guarantees global optimality 
        with a worst-case time complexity of $\\mathcal{O}((|E| + |V|) \\log |V|)$. 
        Because the total graph size is relatively lightweight, execution completes in sub-milliseconds, allowing the engine to 
        re-evaluate path options dynamically whenever live crowd inputs or traffic parameters shift.
        """
    )
    
    st.markdown("---")
    
    st.subheader("3. Database Systems & Data Structures")
    st.write(
        """
        The graph network is internally represented using an **Adjacency List** implemented via nested hash maps (Python Dictionaries). 
        This approach offers optimal spatial complexity of $\\mathcal{O}(|V| + |E|)$, making it significantly more memory-efficient 
        than a sparse $12 \\times 12$ Adjacency Matrix. 
        
        Data integrity and state persistence across page renders are managed using in-memory state containers (`st.session_state`), 
        simulating a real-time reactive transactional layer for live parameter updates.
        """
    )

# ==========================================
# PAGE 3: PROGRAMMING USED
# ==========================================
elif selected_page == "Programming used":
    st.title("💻 Stack Used")
    st.markdown("### Python 3.10+, NetworkX, Streamlit, Matplotlib, Pandas")

# ==========================================
# PAGE 4: AI/ML LAYER
# ==========================================
elif selected_page == "AI/ML layer":
    st.title("🤖 Optimization Engine & AI Heuristic Layer")
    st.caption("Crowd-Aware Dynamic Cost Calculation Mechanics")
    
    st.subheader("1. The Dynamic Objective Cost Function")
    st.write(
        """
        In traditional navigation systems (like standard GPS), road weights are static values derived solely from physical distance ($d_{uv}$). 
        However, in a smart campus transit ecosystem, prioritizing shorter distance alone leads to massive delays at heavily overcrowded stops. 
        
        To solve this, our system introduces a **Multi-Objective Composite Cost Function**:
        """
    )
    
    st.latex(r"Cost(u, v) = \max\left(w_1 \cdot d_{uv} + w_2 \cdot t_{uv} - w_3 \cdot \left(\frac{D_u + D_v}{2}\right), \, 0.1\right)")
    
    st.write(
        """
        * **$d_{uv}$ (Distance Factor):** Physical road distance between stop $u$ and stop $v$ in kilometers.
        * **$t_{uv}$ (Time Factor):** Estimated base travel time in minutes.
        * **$D_u, D_v$ (Density Factors):** Real-time student crowd counts waiting at stops $u$ and $v$.
        * **$w_1, w_2, w_3$ (Hyperparameters):** Tunable weight coefficients balancing distance penalty ($w_1 = 1.0$), time penalty ($w_2 = 0.5$), and student density discount ($w_3 = 0.01$).
        * **$\\max(\\dots, 0.1)$ Boundary Constraint:** Prevents edge weights from dropping below zero or becoming negative, preserving Dijkstra's algorithmic correctness and preventing infinite loop relaxation bugs.
        """
    )
    
    st.markdown("---")
    
    st.subheader("2. Heuristic Search & Adaptive Decision Making")
    st.write(
        """
        The core intelligence lies in the **subtraction of average density** in the cost formula. 
        In graph optimization, algorithms naturally seek paths with the lowest total edge weights. 
        By applying a mathematical discount ($w_3 \\cdot \\text{Density}$) to edges connected to crowded hubs, 
        we artificially reduce the edge cost of routes serving high student queues.
        
        This forces Dijkstra's search algorithm to dynamically divert shuttle buses toward high-demand passenger clusters, 
        effectively operating as a rule-based AI heuristic search engine that balances operational transit costs with maximum passenger coverage.
        """
    )
    
    st.markdown("---")
    
    st.subheader("3. Future Extension: Predictive ML Pipeline")
    st.write(
        """
        In a full-scale smart city production system, the static density inputs would be replaced by an automated **Time-Series ML Pipeline** 
        (such as XGBoost or LSTM Neural Networks). 
        By ingesting historical class timetables, weather data, and past station queue trends, the model would forecast student crowd spikes 
        15-30 minutes in advance, allowing the optimizer to dispatch buses proactively before queues accumulate.
        """
    )

# ==========================================
# PAGE 5: ANALYTICS & DYNAMIC CROWD CONTROL
# ==========================================
elif selected_page == "Analytics & Crowd Control":
    st.title("📊 Dynamic Student Crowd Density Control")
    st.write("Adjust the sliders below to simulate live crowd density updates at any bus stop:")
    
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
    st.write("Daily operational timings for campus shuttles:")
    
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
            path = nx.dijkstra_path(G, source=start_stop, target=end_stop, weight='weight')
            total_dist = sum(G[path[i]][path[i+1]]['distance'] for i in range(len(path)-1))
            total_time = sum(G[path[i]][path[i+1]]['time'] for i in range(len(path)-1))
            
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
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4.0, edge_color='red', ax=ax)
    plt.axis('off')
    st.pyplot(fig)
    
    # LIVE GPS SIMULATION WITH AUDIO ALERT
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
        
        # Audio Notification Alert (HTML5 Audio chime)
        st.components.v1.html(
            """
            <audio autoplay>
              <source src="https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3" type="audio/mpeg">
            </audio>
            """,
            height=0
        )
        
        st.success(f"🎯 **Arrival Alert:** Bus Arrived at `{end_stop}` Successfully!")
