# 🚇 London Underground Network Analysis
*A graph-based Python tool for exploring and optimising the London Underground.*

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/London_Underground.svg" width="140" alt="London Underground logo">
</p>

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](#) 
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

---

## 📋 Table of Contents
1. [Project Structure](#-project-structure)
2. [Installation](#-installation)
3. [Overview](#-overview)
4. [Key Features](#-key-features)
5. [How to Use](#-how-to-use)
6. [License](#-license)
7. [Authors](#-authors)

---

## 📂 Project Structure
```
clrsPython/
└── library/
    ├── aaaMain.py              # main script
    └── london_underground_data.xlsx
requirements.txt
README.md
```

* **Main script:** `library/aaaMain.py`  
* **Data file:** `library/london_underground_data.xlsx`

---

## ⚙️ Installation
```bash
# Clone the repo
git clone https://github.com/<YOUR-USER>/clrsPython.git
cd clrsPython

# Install dependencies
pip install -r requirements.txt
```
> **Requires:** Python 3.x

---

## Overview
This project performs a comprehensive analysis of the **London Underground** network:

- Calculates shortest paths between stations based on both travel time and number of stops, using Dijkstra’s algorithm as the primary method.
- Then applies additional graph algorithms such as Bellman-Ford for detecting negative cycles and Kruskal’s algorithm to compute the Minimum Spanning Tree (MST) for network optimisation.
- Visualises network-wide travel statistics with histograms.
- Compares pre- and post-optimisation metrics to assess the impact of MST-based changes.

---

## Key Features
| # | Feature | Details |
|---|---------|---------|
| 1 | **Shortest Path Analysis** | Dijkstra’s algorithm for any two stations (time & stops). |
| 2 | **Graph Optimisation** | Bellman-Ford for negative cycles; Kruskal for MST. |
| 3 | **Data Visualisation** | Histograms of travel times and stop counts. |
| 4 | **Impact Analysis** | Evaluates network after MST closure. |

---

## How to Use
<details>
<summary><strong>Step-by-step guide</strong></summary>

1. **Prepare the data**  
   Ensure `london_underground_data.xlsx` contains the columns:  
   `Line`, `Station`, `Connection`, `Time`.

2. **Run the script**
   ```bash
   python library/aaaMain.py
   ```

3. **Enter station names** when prompted, e.g.  
   ```
   Please enter your first station: Victoria
   Please enter your destination station: bank
   ```

4. **View results** in the console:  
   * route, journey time, number of stops  
   * histogram plots of global statistics

5. **Analyse optimisation output** for MST and travel-time changes.

</details>

---

## Author

Developed by **Silvester Dan** as part of a university coursework project.

Algorithms in the `clrsPython` library are based on the textbook *Introduction to Algorithms* by Cormen, Leiserson, Rivest, and Stein (CLRS).


---

> *Happy analysing & safe travels!* 
