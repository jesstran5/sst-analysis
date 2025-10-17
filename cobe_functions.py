import xarray as xr
import numpy as np
from math import pi

'''
Adapted from `Lab4-modules.ipynb` file of given code in the cells
'''
def read_latest_sst(dataset_path):
    sst_ds = xr.load_dataset(dataset_path)
    sst = sst_ds['sst']

    return sst[-1]

def get_time_series_at_coordinate_latest_sst(latitude, longitude, dataset_path):
    sst_ds = xr.load_dataset(dataset_path)
    sst = sst_ds['sst']
    time = sst_ds['time']

    return time, sst[:, latitude, longitude]

def get_times_from_dataset(sst_ds):
    return sst_ds['time']

def load_time():
    return

def read_entire_ds(dataset_path):
    sst_ds = xr.load_dataset(dataset_path)

    return sst_ds

def get_velocity_slope_from_dataset_coordinate(sst_np, G_months, latitude, longitude):
    sst_np_coordinate = sst_np[:, latitude, longitude]

    # Find solution vector parameters m
    m_months = np.linalg.inv(G_months.T @ G_months) @ G_months.T @ sst_np_coordinate

    return m_months[1]



