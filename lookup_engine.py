import pandas as pd
import pickle

# ===========================
# Load Dataset
# ===========================

df = pd.read_csv("data/laptop_price_dataset_india.csv")
# Change the path according to your project







# ===========================
# Model Lookup
# ===========================

model_lookup = (
    df.groupby("model")
      .agg({
          "touchscreen": "first",
          "operating_system": "first",
          "battery_capacity_wh": "first",
          "weight_kg": "first",
          "release_year": "first",
          "warranty_years": "first",
          "webcam_resolution": "first",
          "wifi_version": "first",
          "bluetooth_version": "first"
      })
      .to_dict(orient="index")
)

# ===========================
# CPU Lookup
# ===========================

cpu_lookup = (
    df.groupby("processor_model")
      .agg({
          "processor_cores": "first",
          "processor_threads": "first",
          "cpu_base_clock_ghz": "first",
          "cpu_boost_clock_ghz": "first"
      })
      .to_dict(orient="index")
)

# ===========================
# GPU Lookup
# ===========================

gpu_lookup = (
    df.groupby("gpu_model")
      .agg({
          "gpu_memory_gb": "first"
      })
      .to_dict(orient="index")
)

# ===========================
# RAM Lookup
# ===========================

ram_lookup = (
    df.groupby("ram_type")
      .agg({
          "ram_speed_mhz": "median"
      })
      .to_dict(orient="index")
)

# ===========================
# Resolution Lookup
# ===========================

resolution_lookup = {}

for resolution in df["screen_resolution"].unique():

    width = int(resolution.split("x")[0])
    height = int(resolution.split("x")[1])

    resolution_lookup[resolution] = {
        "resolution_width": width,
        "resolution_height": height
    }

# ===========================
# Brand Defaults
# ===========================

brand_lookup = (
    df.groupby("brand")
      .agg({
          "touchscreen": lambda x: x.mode().iloc[0],
          "operating_system": lambda x: x.mode().iloc[0],
          "battery_capacity_wh": "median",
          "weight_kg": "median",
          "release_year": "max",
          "warranty_years": "median",
          "webcam_resolution": lambda x: x.mode().iloc[0],
          "wifi_version": lambda x: x.mode().iloc[0],
          "bluetooth_version": "median"
      })
      .to_dict(orient="index")
)

# ===========================
# Save Everything
# ===========================

lookups = {
    "cpu": cpu_lookup,
    "gpu": gpu_lookup,
    "ram": ram_lookup,
    "resolution": resolution_lookup,
    "model": model_lookup
}

with open("lookup_tables.pkl", "wb") as f:
    pickle.dump(lookups, f)

print("Lookup tables saved successfully!")