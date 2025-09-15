# EEX5335_LAB03
Memory System Simulator

## 📌 Overview
This project is a simple **Memory Management Simulator** that demonstrates how modern operating systems handle memory access using:
- **Translation Lookaside Buffer (TLB)**
- **Page Table**
- **Cache**
- **Main Memory**

It simulates:
- Virtual to physical address translation
- TLB hits and misses
- Page faults (with FIFO replacement)
- Cache hits and misses

This simulator is for educational purposes only (based on *Operating System Concepts* by Silberschatz, Galvin, and Gagne).

---

## ⚙️ Requirements
- Python 3.x (tested on Python 3.8+)
- Works on Windows, Linux, and macOS

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/memory-simulator.git
   cd memory-simulator
Run the simulator:

bash
Copy code
python simulator.py
Example output:

yaml
Copy code
Accessing VA 0x569E (VPN=86, Offset=158)
TLB MISS
Page Fault: Loaded VPN 86 into Frame 0
Cache MISS: Loading block (0,9)
Returned data: 0
🧪 Test Virtual Addresses
You can edit the list of virtual addresses inside simulator.py:

python
Copy code
virtual_addresses = [0x569E, 0x569E, 0x569F, 0x569E, 0x376E, 0x376E]
Re-running will show TLB Hits and Cache Hits after the first access.

📊 Sample Statistics
makefile
Copy code
=== Statistics ===
accesses: 6
tlb_hits: 2
page_faults: 2
cache_hits: 3
📚 References
Abraham Silberschatz, Peter B. Galvin, Greg Gagne, Operating System Concepts, 8th Edition (Chapters 8 & 9)

👩‍💻 Author
