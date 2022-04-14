import numpy as np
import astropy.units as u
from astropy.constants import iau2015 as const
import matplotlib.pyplot as plt

#------------------------------------------------------------
sed = np.loadtxt("sed.txt", skiprows = 3, delimiter = ",")

wavelength = sed[:, 0]
specific_luminosity = sed[:, 1]
wavelength_ascending = wavelength[::-1]
specific_luminosity_ascending = specific_luminosity[::-1]

#Initializations.
#----
wavelength_plot = wavelength_ascending[np.where(wavelength_ascending >= 10)]*(u.um) #<-- The units have been added to these.
specific_luminosity_plot = specific_luminosity_ascending[np.where(wavelength_ascending >= 10)]*(const.L_sun)*(u.um**-1)
specific_luminosity_plot = specific_luminosity_plot.to((u.erg/u.s)*(u.um**-1))

#This section is just to set up the integral.
#----


#----
wavelength_ascending = wavelength_ascending*(u.um) 
specific_luminosity_ascending = specific_luminosity_ascending*(const.L_sun)*(u.um**-1)

#This section is messily shoved in here because I had to add it in after I already completed the code to fix the graph.
#----


plt.plot(wavelength_ascending, specific_luminosity_ascending)
plt.yscale('log')
plt.xscale('log')
plt.ylabel(r'Specific Luminosity (L☉/μm)')
plt.xlabel(r'Wavelength (μm)')
plt.xlim([0.05, 10**3])

plt.savefig('hoke_rhett_hw7.png', dpi = 150)
#======================================================================================
spectral_energy_distribution = np.trapz(specific_luminosity_plot, x = wavelength_plot)

print(spectral_energy_distribution) #<-- CHECK THIS PRINT STATEMENT. This is my answer to the integral.
#======================================================================================

#  NOTES BELOW


#print(const.L_sun)  <-- Verifies that the units exist in the constant.

#print(len(wavelength_plot))           <-- These are the same length, as they should be.
#print(len(specific_luminosity_plot))  <--

#print(specific_luminosity_plot[400])  <-- This proves to me that the units carry over in the array.

#print(wavelength)
#print(wavelength_ascending)
#print(specific_luminosity)
#print(specific_luminosity_ascending)
#print(wavelength_plot)
#print(specific_luminosity_plot)
#------------------------------------------------------------
#print(sed)

###########
#wavelength_plot = wavelength_ascending[np.where(wavelength_ascending >= 10)]
#specific_luminosity_plot = specific_luminosity_ascending[np.where(wavelength_ascending >= 10)]
