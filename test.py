import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import pandas as pd 
from tensorpotential.utils.utilities import generate_tp_atoms
from ase.calculators.singlepoint import SinglePointCalculator

df = pd.read_pickle('./Cu_df1_A1_A2_A3_EV_elast_phon.pckl.gzip', compression="gzip")

cutoff = 6

def do_tp_atoms(row):
    at = row['ase_atoms']
    en = row['energy_corrected']
    f = row['forces']
    calc = SinglePointCalculator(at, energy=en, forces=f)
    at.set_calculator(calc)     # attaches calculator object to atoms 
    
    return generate_tp_atoms(at, cutoff=cutoff)


row = df.iloc[2]
at = row['ase_atoms']
t = generate_tp_atoms(at, cutoff=cutoff) 

print(t['_ind_i'][:50]) 
print(t['_ind_j'][:50])