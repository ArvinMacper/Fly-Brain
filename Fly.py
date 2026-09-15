from neuprint import Client, fetch_adjacencies
import navis

Tokennumb = "Your Token"

client = Client(
    "https://neuprint.janelia.org",
    dataset="male-cns:v1.0",
    token=Tokennumb
)

print("Connected to MaleCNS!")

outgoing_edges, neuron_info = fetch_adjacencies("DNge104")

incoming_edges, neuron_info2 = fetch_adjacencies(
    None,
    "DNge104"
)

print("Outgoing neurons:", len(outgoing_edges))
print("Incoming neurons:", len(incoming_edges))

print("\nOutgoing edges columns:")
print(outgoing_edges.columns.tolist())

print("\nOutgoing edges:")
print(outgoing_edges.head())

print("\nNeuron info columns:")
print(neuron_info.columns.tolist())

print("\nNeuron info:")
print(neuron_info.head())

import networkx as nx
import matplotlib.pyplot as plt

# Get strongest connections
strongest = neuron_info.sort_values(
    "weight",
    ascending=False
).head(50)

# Create graph
G = nx.DiGraph()

for _, row in strongest.iterrows():
    G.add_edge(
        row["bodyId_pre"],
        row["bodyId_post"],
        weight=row["weight"]
    )

# Draw graph
plt.figure(figsize=(12, 12))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    arrows=True
)

plt.title("DNge104 MaleCNS Connectivity")
plt.show()


