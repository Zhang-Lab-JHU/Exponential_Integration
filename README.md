# Exponential Integration Method

## Overview

Exponential integration is a computational technique used to estimate the free energy difference between two states. It is particularly useful in the study of phase transitions and interactions within complex fluids. 

## Application

This code was developed and utilized in the research article titled "Conformational entropy of intrinsically disordered proteins bars intruders from biomolecular condensates." The primary focus of the study is to explore the free energy barriers that proteins encounter when penetrating biomolecular condensates. 

The method compares two distinct states:
1. **Unperturbed Liquid State**: The baseline state of the unperturbed liquid.
2. **Liquid with Repulsive Spherical Particle**: A modified state of the liquid where it interacts with a repulsive spherical particle.

By evaluating these states, we can gain insights into the energetics of protein interactions within complex fluid systems.

## Theoretical Background

If $Z_0$ is partition function for system before insertion, $Z$ is partition function for system with inserted particle then the free energy of insertion (also known as the excess chemical potential) is 

$$
\Delta F = -k_\text{B}T\ln\frac{Z}{Z_0} = -k_\text{B}T\ln\int \rho_0(\boldsymbol{r})e^{-\frac{U(R|\boldsymbol{r})}{k_\text{B}T}}d\boldsymbol{r} = -k_\text{B}T\ln\left\langle e^{-\frac{U(R)}{k_\text{B}T}}\right\rangle,
$$

Where $U(R|\boldsymbol{r})$ is potential energy of interaction between inserted particle with radius R and surrounding liquid particles with coordinates $\boldsymbol{r}$. We use Weeks-Chandler-Andersen ptential tom model purely repulsive interaction.

The average is over all insertion locations and configurations of the system (different time steps).

## Code Usage

Initialization.py contains the function that calculates Partition function $Z$ which is related to insertion free energy as follows: 

$$
F = -k_\text{B}T \ln Z
$$

The dataset should consist of four columns: first is radii of liquid particles, and three other columns are x y and z coordinates of liquid particles (for example from MD simulations). Radii and coordinates from different time stems should not be separated by any extra lines

