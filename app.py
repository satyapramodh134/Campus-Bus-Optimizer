import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
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

# Bottom Sidebar Info Box
st.sidebar.info(
    "💡 **Project 7: Campus Bus Route Optimizer**\n\n"
    "**Batch:** 2025-2029 (B.Tech First Year)\n"
    "**Domain:** AI & Graph Theory\n"
    "**Status:** Live GPS Integrated"
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
        st.write(
            "Project 7 addresses inefficient transit in modern university campuses. "
            "By mapping physical road segments into a weighted graph $G=(V, E)$, the system "
            "dynamically calculates the most efficient route considering **distance**, **travel time**, "
            "and **live student crowd density**."
        )
        st.write(
            "With integrated **Live GPS Simulation**, campus transport authorities can track "
            "active shuttle buses in real-time while providing students accurate estimated arrival times (ETA)."
        )
        
        st.markdown("---")
        st.subheader("📊 Key Operational Metrics")
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Campus Stops", "12 Active")
        k2.metric("Road Segments", "15 Connections")
        k3.metric("Peak Crowd", "150 Students")
        k4.metric("GPS Sync", "Real-Time")

    with col2:
        st.subheader("📋 Academic Details")
        st.info(
            "**Institution:** JNTUK R23\n\n"
            "**Branch:** AI & Data Science\n\n"
            "**Course:** Data Structures & Algorithms\n\n"
            "**Primary Engine:** Dijkstra's Algorithm"
        )

# ==========================================
# PAGE 2: SUBJECTS USED
# ==========================================
elif selected_page == "Subjects used in project":
    st.title("📚 Academic Subjects & Theoretical Foundation")
    
    st.subheader("1. Discrete Mathematics & Graph Theory")
    st.write("Campus topology modeled using undirected weighted graphs $G = (V, E)$. Node degree centrality helps identify high-traffic transfer hubs.")
    
    st.subheader("2. Design & Analysis of Algorithms (DAA)")
    st.write("Shortest path discovery executed via **Dijkstra’s Algorithm** with priority queues using Min-Heaps, achieving $O((|E| + |V|) \\log |V|)$ efficiency.")
    
    st.subheader("3. Linear Algebra & Optimization")
    st.write("Adjacency matrix representation combined with normalized dynamic weight vectors balancing distance, time, and student crowd volume.")

    st.subheader("4. Applied Statistics & Data Analytics")
    st.write("Density distribution modeling and variance analysis across peak campus hours for optimal shuttle scheduling.")

# ==========================================
# PAGE 3: PROGRAMMING USED
# ==========================================
elif selected_page == "Programming used":
    st.title("💻 Programming Languages & Libraries")
    
    st.markdown("### Core Stack: Python 3.10+")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("#### 🟢 NetworkX")
        st.write("Graph data structures and pathfinding algorithm execution.")
    with c2:
        st.markdown("#### 🔵 Pandas & NumPy")
        st.write("Data manipulation, array vectors, and metric computations.")
    with c3:
        st.markdown("#### 🔴 Streamlit")
        st.write("Interactive Web GUI and real-time state management.")
    with c4:
        st.markdown("#### 🟡 Matplotlib")
        st.write("Network topological plot rendering and analytics charts.")

# ==========================================
# PAGE 4: AI/ML LAYER
# ==========================================
elif selected_page == "AI/ML layer":
    st.title("🤖 Dynamic Cost Engine & AI Layer")
    
    st.subheader("Mathematical Objective Function")
    st.write("Standard navigation uses pure Euclidean distance. Our optimization engine factors in student crowd density dynamically:")
    
    st.latex(r"Cost(u, v) = w_1 \cdot Distance(u, v) + w_2 \cdot Time(u, v) - w_3 \cdot \left(\frac{Density_u + Density_v}{2}\right)")
    
    st.markdown("""
    * **$Distance(u,v)$**: Distance between stops in kilometers.
    * **$Time(u,v)$**: Estimated bus travel time in minutes.
    * **$Density$**: Real-time waiting student count at target stops.
    * **Weights ($w_1, w_2, w_3$)**: Hyperparameters adjusted based on rush hours.
    """)
    st.success("Result: High-density stops get cost-discounted, encouraging the algorithm to route buses through high-demand hubs!")

# ==========================================
# PAGE 5: ANALYTICS & GRAPHS
# ==========================================
elif selected_page == "Analytics & Graphs":
    st.title("📊 Campus Analytics & Data Charts")
    
    st.subheader("1. Student Density Distribution Across Campus Stops")
    stops_df = pd.DataFrame([{"Stop": k, "Students Waiting": v["density"]} for k, v in bus_stops.items()])
    stops_df = stops_df.sort_values(by="Students Waiting", ascending=False)
    
    st.bar_chart(stops_df.set_index("Stop"))
    
    st.markdown("---")
    st.subheader("2. Road Network Segment Distance vs Travel Time")
    
    edges_data = [{"Route": f"{u} ➔ {v}", "Distance (km)": d, "Time (min)": t} for u, v, d, t in road_network]
    edges_df = pd.DataFrame(edges_data)
    
    st.dataframe(edges_df, use_container_width=True)

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
        
        sim_speed = st.slider("Simulation Speed (sec/stop):", 1, 5, 2)
        start_sim = st.button("🚀 Start Live GPS Tracker")
        
    with col_display:
        if start_stop == end_stop:
            st.warning("⚠️ Origin and Destination stops must be different!")
        else:
            path = nx.dijkstra_path(G, source=start_stop, target=end_stop, weight='weight')
            total_dist = sum(G[path[i]][path[i+1]]['distance'] for i in range(len(path)-1))
            total_time = sum(G[path[i]][path[i+1]]['time'] for i in range(len(path)-1))
            
            st.success(f"**Optimal Route:** {' ➔ '.join(path)}")
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Distance", f"{total_dist:.2f} km")
            m2.metric("Time", f"{total_time:.1f} mins")
            m3.metric("Stops", f"{len(path)}")

    # Map Plot
    st.markdown("---")
    st.subheader("🗺️ Live Campus Network Graph")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    pos = nx.spring_layout(G, seed=42)
    node_sizes = [G.nodes[n]['density'] * 15 for n in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', edgecolors='black', ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5, alpha=0.4, edge_color='gray', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold', ax=ax)
    
    if start_stop != end_stop:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=4.0, edge_color='red', ax=ax)
    
    edge_labels = {(u, v): f"{d['distance']}km" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, ax=ax)
    
    plt.axis('off')
    st.pyplot(fig)
    
    # LIVE GPS DETECTOR SIMULATION
    if start_sim and start_stop != end_stop:
        st.markdown("---")
        st.subheader("📡 Live GPS Detector Bus Tracking")
        
        progress_bar = st.progress(0)
        status_box = st.empty()
        
        for idx, current_stop in enumerate(path):
            lat = bus_stops[current_stop]["lat"]
            lon = bus_stops[current_stop]["lon"]
            
            status_box.info(f"🚌 **Bus Position:** Currently at **{current_stop}** | 📍 Coordinates: `{lat}, {lon}`")
            
            # Map display
            map_data = pd.DataFrame([{"lat": lat, "lon": lon}])
            st.map(map_data, zoom=14)
            
            progress = (idx + 1) / len(path)
            progress_bar.progress(progress)
            
            time.sleep(sim_speed)
            
        st.balloons()
        st.success("🎯 Bus successfully arrived at Destination!")
