#!/usr/bin/env python
"""
This script formats the downloaded photometry files
by get_lco_data.py

Next: Copy the formatted *.csv as input to allesfitter
"""
import pandas as pd

# input file name : output file name
files = {
"TIC88785435-11_20240416_LCO-CTIO-1m0_gp_measurements.tbl": "lco_gp.csv",
"TIC88785435-11_20240213_LCO-CTIO-1m0_ip_measurements.tbl": "lco_ip.csv",
"TIC88785435-11_20240305_LCO-CTIO-1m0_ip_measurements.tbl": "lco_ip2.csv",
"TIC88785435-11_20240326_LCO-CTIO-1m0_ip_measurements.tbl": "lco_ip3.csv",
}

def read_lco1m_data(fp):
    df = pd.read_csv(fp, delimiter='\t')
    mapping = {#'BJD_TDB': 'BJD_TDB',
               'rel_flux_T1': 'Flux',
               'rel_flux_err_T1': 'Err',
               'AIRMASS': 'Airmass',
                   #'Peak_T1',
                   # 'FWHM_T1',
                   # 'X(IJ)_T1',
                   # 'Y(IJ)_T1',
                   # 'Source-Sky_T1'
                   }
    df = df.rename(mapping, axis=1)
    #import pdb; pdb.set_trace()
    cols = mapping.values()
    print("Flux is normalized by its median value.")
    df['Flux']/=df['Flux'].median()
    return df[cols]

if __name__=='__main__':
    for f in files.keys():
        df = read_lco1m_data(f)
        fp = files[f]
        df.to_csv(fp, index=False, header=False)
        print("Saved: ", fp)
