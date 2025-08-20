# ⚡ Cyclotron Simulation  

A Python simulation of a **cyclotron particle accelerator**, where a charged particle spirals outward under the influence of alternating electric fields and a perpendicular magnetic field.  

![Cyclotron Spiral](https://cdn.britannica.com/68/3368-050-1EEDBBAC/particles-cyclotron-Plan-view-middle-dees-magnetic.jpg)  
*Particle trajectory inside the cyclotron*  

---

## ✨ Features
- Implements the **Lorentz force law**  
- Alternating RF electric field in the “D-gap”  
- Uniform perpendicular magnetic field in the cyclotron region  
- Tracks **particle trajectory** (spiral path)  
- Computes **kinetic energy vs time** (staircase growth)  
- Visualizes results with Matplotlib  

---

## 📸 Sample Output  

**Trajectory (x vs y):**  
Spiral growth due to acceleration inside the cyclotron.  



---

## 🧑‍🔬 Physics Background
- The particle is confined by a **magnetic field** `B` perpendicular to its velocity.  
- Acceleration occurs in the **gap region** with an oscillating **electric field** `E`.  
- Each time the particle crosses the gap, it gains a “kick” of energy.  
- The motion is governed by the **Lorentz force equation**:  




---

## 📜 Requirements
- Python 3.x  
- NumPy  
- SciPy  
- Matplotlib  

Install dependencies with:  
```bash
pip install numpy scipy matplotlib

