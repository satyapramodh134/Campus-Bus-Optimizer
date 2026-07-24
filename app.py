import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Project 7: Campus Bus Route Optimizer", layout="wide")

# ==========================================
# SIDEBAR NAVIGATION (MEE FRIEND STYLE)
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
        "LIVE DEMO"
    ]
)

st.sidebar.markdown("---")

# Bottom Sidebar Info Box
st.sidebar.info(
    "💡 **Project 7: Campus Bus Route Optimizer**\n\n"
    "**Batch:** 2025-2029 (B.Tech First Year)\n"
    "**Domain:** AI & Graph Theory"
)

# ==========================================
# GLOBAL DATA & GRAPH INITIALIZATION
# ==========================================
bus_stops = {
    "Main Gate": 10, "Library": 85, "Hostel Block A": 120, "Hostel Block B": 95,
    "Engineering Block": 150, "Science Block": 60, "Sports Complex": 40,
    "Cafeteria": 110, "Auditorium": 30, "Admin Building": 25,
    "Research Park": 45, "Medical Center": 20
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
for stop, density in bus_stops.items():
    G.add_node(stop, density=density)

w1, w2, w3 = 1.0, 0.5, 0.01
for u, v, dist, time_min in road_network:
    avg_density = (bus_stops[u] + bus_stops[v]) / 2.0
    cost = max((w1 * dist) + (w2 * time_min) - (w3 * avg_density), 0.1)
    G.add_edge(u, v, distance=dist, time=time_min, weight=cost)

# ==========================================
# PAGE 1: HOME
# ==========================================
if selected_page == "Home":
    st.title("🎓 Campus Bus Route Optimizer")
    st.caption("JNTUK R23 Curriculum — B.Tech Artificial Intelligence & Data Science")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📌 Project Overview & Updates")
        st.write(
            "Welcome to **Project 7: Campus Bus Route Optimizer**! This application models "
            "a physical campus road network with **12 key bus stops** and optimizes transit paths "
            "based on student density, segment distance, and estimated travel times."
        )
        st.write(
            "By evaluating student demand dynamically, the system minimizes wait times and "
            "travel delays using **Dijkstra's Shortest Path Algorithm**."
        )
        
        st.markdown("---")
        st.subheader("📊 Campus Key Stats")
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Total Bus Stops", "12 Stops")
        k2.metric("Road Links", "15 Routes")
        k3.metric("Max Density Stop", "150 Students")
        k4.metric("Avg Speed", "20 km/h")

    with col2:
        st.subheader("📋 Project Details")
        st.info(
            "**Institution:** JNTUK Curriculum R23\n\n"
            "**Branch:** AI & DS\n\n"
            "**Project ID:** Project 7\n\n"
            "**Optimization Target:** Distance, Time, & Density Balance"
        )

# ==========================================
# PAGE 2: SUBJECTS USED IN PROJECT
# ==========================================
elif selected_page == "Subjects used in project":
    st.title("📚 Subjects Used in Project")
    
    st.subheader("1. Graph Theory & Discrete Mathematics")
    st.write("Used for modeling bus stops as **Vertices (V)** and connecting roads as **Edges (E)** using undirected weighted graphs $G = (V, E)$.")
    
    st.subheader("2. Design & Analysis of Algorithms (DAA)")
    st.write("Core usage of **Dijkstra’s Shortest Path Algorithm** with dynamic cost weighting to optimize path selection.")
    
    st.subheader("3. Linear Algebra & Matrices")
    st.write("Using **Adjacency Matrices** and **Density Vectors** to store graph weights and node attributes.")

    st.subheader("4. Physics & Motion Kinematics")
    st.write("Calculating travel time across distance segments using average velocity equations: $\\Delta t = \\frac{\\Delta s}{v_{avg}}$.")

# ==========================================
# PAGE 3: PROGRAMMING USED
# ==========================================
elif selected_page == "Programming used":
    st.title("💻 Programming & Technologies Used")
    
    st.markdown("### 🐍 Python 3.8+")
    st.write("The core engine of the project is written completely in beginner-friendly Python.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🟢 NetworkX")
        st.write("Used for graph data structures and running Dijkstra's shortest path calculations.")
    with c2:
        st.markdown("#### 🔵 Matplotlib")
        st.write("Used to render network maps, node sizes, and route highlights visually.")
    with c3:
        st.markdown("#### 🔴 Streamlit")
        st.write("Used to build this modern web dashboard layout with zero HTML/CSS required.")

# ==========================================
# PAGE 4: AI/ML LAYER
# ==========================================
elif selected_page == "AI/ML layer":
    st.title("🤖 AI & Optimization Layer")
    
    st.subheader("Weighted Cost Function")
    st.write("Instead of simple geometric distance, our AI engine computes a dynamic **Composite Edge Weight ($C_{ij}$)**:")
    
    st.latex(r"C_{ij} = w_1 \cdot d_{ij} + w_2 \cdot t_{ij} - w_3 \cdot \left(\frac{D_i + D_j}{2}\right)")
    
    st.markdown("""
    * $d_{ij}$: Segment distance (km)
    * $t_{ij}$: Segment travel time (mins)
    * $D_i, D_j$: Student density at origin & destination stops
    * $w_1, w_2, w_3$: Weighting factors balancing distance vs student demand
    """)
    st.info("High student density reduces the composite cost, instructing Dijkstra's algorithm to prioritize high-demand stops!")

# ==========================================
# PAGE 5: LIVE DEMO
# ==========================================
elif selected_page == "LIVE DEMO":
    st.title("⚡ Live Route Optimization Demo")
    
    col_input, col_display = st.columns([1, 2])
    
    with col_input:
        st.subheader("🕹️ Select Route")
        start_stop = st.selectbox("Origin Stop:", list(bus_stops.keys()), index=0)
        end_stop = st.selectbox("Destination Stop:", list(bus_stops.keys()), index=11)
        
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
            m3.metric("Stops Visited", f"{len(path)}")

    st.markdown("---")
    st.subheader("🗺️ Visual Map Representation")
    
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