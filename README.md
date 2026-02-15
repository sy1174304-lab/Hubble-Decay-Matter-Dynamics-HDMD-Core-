# Hubble-Decay-Matter-Dynamics-HDMD-Core-
A Friedmann-Lemaître-Robertson-Walker (FLRW) simulation engine. It tracks $H(t)$ attenuation and scale factor ($a$) integration,
modeling the interaction between matter density ($\Omega_M$) and dark energy ($\Omega_\Lambda$) across cosmic time

Hubble-Decay-Matter-Dynamics (HDMD-Core)OverviewHDMD-Core is a high-precision computational simulation engine
designed to model the evolution of cosmic expansion. The framework is built upon the Friedmann-Lemaître-Robertson-Walker (FLRW) metric,
providing a mathematical substrate to analyze the large-scale structure of the universe across temporal scales.Technical DescriptionA computational
simulation engine focused on the evolution of cosmic expansion. The framework utilizes a Friedmann-Lemaître-Robertson-Walker (FLRW) Metric
approximation to model the interaction between matter density ($\Omega_M$) and dark energy ($\Omega_\Lambda$). 
Its primary function is the precise tracking of $H(t)$ attenuation and scale factor ($a$) integration across temporal benchmarks.Core ArchitecturePhysics Engine: ODE-based integration of the Friedmann acceleration equations.Density Parameters: Configured for $\Omega_M = 0.308$ (Matter) and $\Omega_\Lambda = 0.692$ (Dark Energy).
Integration Method: Utilizing scipy.integrate.odeint for solving coupled differential equations of expansion.

Output Metrics: Real-time mapping of Hubble Constant decay and Scale Factor progression.
