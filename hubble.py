import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# ==========================================
# ==========================================

G = 6.67430e-11 
c = 299792458 
H0_val = 67.8 
Omega_M = 0.308 
Omega_L = 0.692 

def calculate_expansion(y, t):
    a, H = y
    # Friedman equation based derivative
    dydt = [H, -H**2 * (Omega_M / a**3 + Omega_L)]
    return dydt

def plot_results(t, a, H):
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(t, a, color='blue')
    plt.xlabel('Time')
    plt.ylabel('Scale Factor (a)')
    plt.title('Universe Expansion')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(t, H, color='red')
    plt.xlabel('Time')
    plt.ylabel('Hubble Constant (H)')
    plt.title('H Over Time')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    a0 = 1 
    initial_H = H0_val 
    y0 = [a0, initial_H] 
    
    t = np.linspace(0, 10, 100) 
    
    solution = odeint(calculate_expansion, y0, t)
    a = solution[:, 0]
    H = solution[:, 1]
    
    # Validation Check
    print(f"Final Scale Factor: {a[-1]:.4f}")
    print(f"Final Hubble Rate: {H[-1]:.4f}")
    
    plot_results(t, a, H)

if __name__ == "__main__":
    main()
