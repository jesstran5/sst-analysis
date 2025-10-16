import xarray as xr

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

def load_time():
    return