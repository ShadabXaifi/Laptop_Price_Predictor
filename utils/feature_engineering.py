import pickle
import math
import pandas as pd

# ==========================
# Load Lookup Tables
# ==========================

with open("lookup_tables.pkl", "rb") as f:
    lookups = pickle.load(f)

cpu_lookup = lookups["cpu"]
gpu_lookup = lookups["gpu"]
ram_lookup = lookups["ram"]
resolution_lookup = lookups["resolution"]
model_lookup = lookups["model"]


# ==========================
# PPI Calculation
# ==========================

def calculate_ppi(screen_size, resolution):

    width = resolution_lookup[resolution]["resolution_width"]
    height = resolution_lookup[resolution]["resolution_height"]

    diagonal_pixels = math.sqrt(width**2 + height**2)

    return diagonal_pixels / screen_size


# ==========================
# Prepare Model Input
# ==========================

def prepare_input(

    brand,
    model,

    processor_brand,
    processor_model,
    processor_generation,

    gpu_brand,
    gpu_model,

    ram_gb,
    ram_type,

    storage_capacity_gb,
    storage_type,

    screen_size_inches,
    screen_resolution,
    refresh_rate_hz,
    panel_type,

    keyboard_backlit,
    fingerprint_sensor

):

    cpu = cpu_lookup[processor_model]

    gpu = gpu_lookup[gpu_model]

    ram = ram_lookup[ram_type]

    model_info = model_lookup[model]

    resolution = resolution_lookup[screen_resolution]

    ppi = calculate_ppi(
        screen_size_inches,
        screen_resolution
    )

    input_df = pd.DataFrame([{

        "brand": brand,
        "model": model,

        "processor_brand": processor_brand,
        "processor_model": processor_model,
        "processor_generation": processor_generation,

        "processor_cores": cpu["processor_cores"],
        "processor_threads": cpu["processor_threads"],

        "cpu_base_clock_ghz": cpu["cpu_base_clock_ghz"],
        "cpu_boost_clock_ghz": cpu["cpu_boost_clock_ghz"],

        "gpu_brand": gpu_brand,
        "gpu_model": gpu_model,
        "gpu_memory_gb": gpu["gpu_memory_gb"],

        "ram_gb": ram_gb,
        "ram_type": ram_type,
        "ram_speed_mhz": ram["ram_speed_mhz"],

        "storage_type": storage_type,
        "storage_capacity_gb": storage_capacity_gb,

        "screen_size_inches": screen_size_inches,
        "screen_resolution": screen_resolution,
        "refresh_rate_hz": refresh_rate_hz,
        "panel_type": panel_type,

        "touchscreen": model_info["touchscreen"],

        "operating_system": model_info["operating_system"],

        "battery_capacity_wh": model_info["battery_capacity_wh"],

        "weight_kg": model_info["weight_kg"],

        "release_year": model_info["release_year"],

        "warranty_years": model_info["warranty_years"],

        "webcam_resolution": model_info["webcam_resolution"],

        "wifi_version": model_info["wifi_version"],

        "bluetooth_version": model_info["bluetooth_version"],

        "keyboard_backlit": keyboard_backlit,

        "fingerprint_sensor": fingerprint_sensor,

        "resolution_width": resolution["resolution_width"],

        "resolution_height": resolution["resolution_height"],

        "ppi": ppi

    }])

    return input_df