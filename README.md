# Network Packet Flow Simulation

This project simulates the flow of data packets in a network of 1,024 computers. It models how packets are generated, assigned random origins and destinations, and tracked for size and transmission time. The simulation then visualizes key statistics about the network activity using plots and heatmaps.

## 📌 Features

- Simulates 10,000 packets flowing through a network of 1024 computers
- Uses probabilistic distributions to model:
  - Packet arrival times
  - Source and destination address selection
  - Packet sizes
- Tracks:
  - Number of packets sent and received by each computer
  - Total bytes sent and received
  - Bytes transmitted over time
  - Inter-computer traffic volumes (heatmap)
- Generates clear visualizations using `matplotlib`

## 📊 Visual Output

- 📈 Line plots for:
  - Number of packets sent/received per computer
  - Total bytes sent/received per computer
  - Bytes sent over time
- 🔥 Heatmap showing packet size volume between source/destination computers

## 🧪 Technologies Used

- Python 3
- NumPy
- matplotlib
- Standard Python libraries: `random`, `math`


