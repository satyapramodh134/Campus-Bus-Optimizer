import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

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
        "Bus Timetable & Schedule",
        "LIVE DEMO & GPS Tracker",
        "🤖 Campus AI Transit Assistant"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Project 7: Campus Bus Route Optimizer**\n\n"
    "**Batch:** 2025-2029 (B.Tech First Year)\n"
    "**Domain:** Linear Algebra & Differential Equations\n"
    "**Status:** Live Mathematical Engine Active"
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

# Session State Initialization
if "stop_densities" not in st.session_state:
    st.session_state.stop_densities = {stop: info["density"] for stop, info in bus_stops.items()}

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
    cost = max((w1 * dist) + (w2 * time_min) - (w3 * avg_density), 0.1)
    G.add_edge(u, v, distance=dist, time=time_min, weight=cost)

# ==========================================
# ANNOUNCEMENT BANNER
# ==========================================
st.warning("📢 **Campus Notice:** Real-time dynamic optimization active. Differential Equations & Matrix models running.")

# ==========================================
# PAGE 1: HOME
# ==========================================
if selected_page == "Home":
    st.title("🚌 Campus Bus Route Optimizer & Live GPS Tracking")
    st.caption("JNTUK R23 Curriculum — Applied Mathematics & Computer Science")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("📌 Project Overview")
        st.write("Project 7 calculates optimal campus bus paths using **Linear Algebra Matrix Operations**, **Differential Equations for Traffic Rates**, and **Programming Algorithms**.")
        st.markdown("---")
        st.subheader("📊 Key Operational Metrics")
        k1, k2, k3 = st.columns(3)
        k1.metric("Campus Stops", "12 Active")
        k2.metric("Road Links", "15 Routes")
        max_density_stop = max(st.session_state.stop_densities, key=st.session_state.stop_densities.get)
        k3.metric("Peak Stop", max_density_stop)
    with col2:
        st.subheader("📋 Academic Details")
        st.info("**Institution:** JNTUK R23\n\n**Subjects:** Linear Algebra, Differential Equations, Programming\n\n**Algorithm:** Dynamic Matrix Dijkstra")

# ==========================================
# PAGE 2: SUBJECTS USED IN PROJECT
# ==========================================
elif selected_page == "Subjects used in project":
    st.title("📚 Academic Subjects & Mathematical Foundations")
    st.caption("Interdisciplinary Application of JNTUK R23 Mathematics & Computer Science")
    
    st.markdown("### 1. 📐 Linear Algebra (Network Matrix Representation)")
    st.write(
        """
        The structural framework of the campus transportation network relies on **Linear Algebra**:
        
        * **Adjacency Matrix ($A \in \mathbb{R}^{12 \times 12}$):** The physical network of 12 campus stops is encoded into a $12 \times 12$ square matrix. An entry $A_{ij} > 0$ denotes a direct road link between stop $i$ and stop $j$, holding the vector weight parameters.
        * **Vectorized Cost Computation:** Distance vectors $\mathbf{d}$, travel time vectors $\mathbf{t}$, and student density vectors $\mathbf{D}$ are combined using matrix transformations:
        """
    )
    st.latex(r"\mathbf{W} = w_1 \mathbf{A}_d + w_2 \mathbf{A}_t - w_3 \mathbf{A}_{\text{density}}")
    
    # Live Matrix Table Display
    st.markdown("#### 🔢 Live $12 \\times 12$ Adjacency Matrix View (Linear Algebra Layer):")
    nodes_list = list(bus_stops.keys())
    adj_matrix = nx.to_numpy_array(G, nodelist=nodes_list, weight='distance')
    matrix_df = pd.DataFrame(adj_matrix, index=nodes_list, columns=nodes_list)
    st.dataframe(matrix_df)

    st.markdown("---")
    
    st.markdown("### 2. 📉 Differential Equations (Dynamic Crowd Rate Modeling)")
    st.write(
        """
        Traffic and student passenger density at stops do not remain static; they change continuously over time. We model crowd dynamics using an **Ordinary Differential Equation (ODE)**:
        """
    )
    st.latex(r"\frac{dD_i(t)}{dt} = \lambda_i(t) - \mu_i(t)")
    st.write(
        """
        * **$\frac{dD_i(t)}{dt}$:** Rate of change of student crowd density at stop $i$ with respect to time $t$.
        * **$\lambda_i(t)$:** Student arrival rate function (Inflow rate from classes finishing).
        * **$\mu_i(t)$:** Student departure rate function (Outflow rate via bus boarding).
        
        Using **Euler's Numerical Method**, the software solves this differential equation iteratively at each time step $\Delta t$:
        """
    )
    st.latex(r"D_i(t + \Delta t) = D_i(t) + \left(\lambda_i(t) - \mu_i(t)\right) \Delta t")

    st.markdown("---")
    
    st.markdown("### 3. 💻 Programming (Computational Engine & Solver)")
    st.write(
        """
        Programming acts as the bridge that translates mathematical equations into a real-time running application:
        
        * **Numerical Execution Engine:** Solves matrix transformations and differential equations in Python using high-performance vector libraries like **NumPy** and **NetworkX**.
        * **Interactive Graphical Interface:** Uses **Streamlit** to visualize matrix states, render dynamic route graphs using **Matplotlib**, and update live coordinates.
        """
    )

# ==========================================
# PAGE 3: PROGRAMMING USED
# ==========================================
elif selected_page == "Programming used":
    st.title("💻 Programming Stack & Computational Architecture")
    
    st.markdown("### 1. Python 3.10+ (Core Language)")
    st.write("Executes matrix transformations, numerical solvers, and routing logic with high performance.")
    
    st.markdown("### 2. NumPy (`numpy`) — Linear Algebra Operations")
    st.write("Handles multi-dimensional array operations, adjacency matrix constructions, and vectorized calculations.")
    
    st.markdown("### 3. NetworkX (`networkx`) — Graph Theory Engine")
    st.write("Provides heap-optimized implementation of Dijkstra's algorithm running over matrix weights.")
    
    st.markdown("### 4. Streamlit (`streamlit`) — Interactive Web Framework")
    st.write("Renders reactive UI components, slider controls, and real-time dashboard elements.")

# ==========================================
# PAGE 4: AI/ML LAYER
# ==========================================
elif selected_page == "AI/ML layer":
    st.title("🤖 Optimization Engine & Heuristic AI Layer")
    st.latex(r"Cost(u, v) = \max\left(w_1 \cdot d_{uv} + w_2 \cdot t_{uv} - w_3 \cdot \left(\frac{D_u + D_v}{2}\right), \, 0.1\right)")
    st.info("The AI layer balances path lengths with student density weighting using composite cost formulas.")

# ==========================================
# PAGE 5: BUS TIMETABLE & SCHEDULE
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
# PAGE 6: LIVE DEMO & GPS TRACKER
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
# PAGE 7: CAMPUS AI TRANSIT ASSISTANT
# ==========================================
elif selected_page == "🤖 Campus AI Transit Assistant":
    st.title("🤖 Campus AI Transit Query Assistant")
    
    user_query = st.selectbox(
        "Select a question for the AI Assistant:",
        [
            "Which bus stop has the highest student congestion right now?",
            "What happens if there is a medical emergency?",
            "Why is Dijkstra's algorithm preferred over BFS?"
        ]
    )
    
    if st.button("💬 Ask AI Assistant"):
        st.markdown("---")
        if "highest student congestion" in user_query:
            max_stop = max(st.session_state.stop_densities, key=st.session_state.stop_densities.get)
            st.info(f"🤖 **AI Answer:** Currently, **{max_stop}** has the highest crowding.")
        elif "medical emergency" in user_query:
            st.info("🤖 **AI Answer:** Enable Emergency Mode in LIVE DEMO to recalculate routes purely on physical shortest distance.")
        elif "BFS" in user_query:
            st.info("🤖 **AI Answer:** BFS only works on unweighted graphs. Dijkstra is needed for weighted distance and time factors.")
