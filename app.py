import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time

# Page Configuration
st.set_page_config(page_title="Project 7: Campus Bus Route Optimizer", layout="wide")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
st.sidebar.markdown("🎓 **Navigation Menu**")
st.sidebar.caption("JNTUK R23 B.Tech AI & DS")

selected_page = st.sidebar.radio(
    "Select Section:",
    [
        "Home",
        "Subjects used in project",
        "Programming used",
        "AI/ML layer",
        "Analytics & Graphs",
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
# DATA & GRAPH INITIALIZATION
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

G = nx.Graph()
for stop, info in bus_stops.items():
    G.add_node(stop, density=info["density"], lat=info["lat"], lon=info["lon"])

w1, w2, w3 = 1.0, 0.5, 0.01
for u, v, dist, time_min in road_network:
    avg_density = (bus_stops[u]["density"] + bus_stops[v]["density"]) / 2.0
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
        k3.metric("Peak Crowd", "150 Students")
        k4.metric("GPS Sync", "Real-Time")
    with col2:
        st.subheader("📋 Academic Details")
        st.info("**Institution:** JNTUK R23\n\n**Branch:** AI & DS\n\n**Algorithm:** Dijkstra's Graph Search")

# ==========================================
# PAGE 2: SUBJECTS USED
# ==========================================
elif selected_page == "Subjects used in project":
    st.title("📚 Academic Subjects")
    st.subheader("1. Graph Theory")
    st.write("Campus network represented as undirected weighted graphs $G = (V, E)$.")
    st.subheader("2. Design & Analysis of Algorithms")
    st.write("Shortest route evaluation using Dijkstra's algorithm.")

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
    st.title("🤖 Optimization Engine")
    st.latex(r"Cost(u, v) = w_1 \cdot Distance + w_2 \cdot Time - w_3 \cdot Density")

# ==========================================
# PAGE 5: ANALYTICS & GRAPHS
# ==========================================
elif selected_page == "Analytics & Graphs":
    st.title("📊 Campus Analytics")
    stops_df = pd.DataFrame([{"Stop": k, "Students Waiting": v["density"]} for k, v in bus_stops.items()])
    st.bar_chart(stops_df.set_index("Stop"))

# ==========================================
# PAGE 6: LIVE DEMO & GPS TRACKER
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

    # Visual Map
    st.markdown("---")
    fig, ax = plt.subplots(figsize=(10, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx(G, pos, node_color='skyblue', edge_color='gray', node_size=800, ax=ax, font_size=8)
    if start_stop != end_stop:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4.0, edge_color='red', ax=ax)
    plt.axis('off')
    st.pyplot(fig)
    
    # GUARANTEED LIVE GPS SIMULATION
    if start_sim and start_stop != end_stop:
        st.markdown("---")
        st.subheader("📡 Live GPS Bus Tracker (Active Connection)")
        
        status_box = st.empty()
        map_box = st.empty()
        prog_bar = st.progress(0)
        
        for idx, current_stop in enumerate(path):
            lat = bus_stops[current_stop]["lat"]
            lon = bus_stops[current_stop]["lon"]
            
            status_box.info(f"🚌 **Shuttle Current Location:** **{current_stop}** | 📍 Lat: `{lat}`, Lon: `{lon}`")
            
            # Realtime map update
            gps_data = pd.DataFrame([{"lat": lat, "lon": lon}])
            map_box.map(gps_data, zoom=14)
            
            prog_bar.progress((idx + 1) / len(path))
            time.sleep(sim_speed)
            
        st.balloons()
        st.success("🎯 Bus Arrived at Destination Successfully!")
       
