import numpy as np

def calculate_upi_score(dn, up, lat):
    BASE_RATE = 95.0
    
    # LATENCY PENALTY
    if lat < 50:
        lat_penalty = 0
    elif lat < 100:
        lat_penalty = 15
    elif lat < 150:
        lat_penalty = 35
    elif lat < 200:
        lat_penalty = 55
    else:
        lat_penalty = 75

    # UPLOAD PENALTY
    if up >= 2.0:
        up_penalty = 0
    elif up >= 1.0:
        up_penalty = 8
    elif up >= 0.5:
        up_penalty = 25
    else:
        up_penalty = 60

    # DOWNLOAD PENALTY
    if dn >= 2.0:
        dn_penalty = 0
    elif dn >= 0.5:
        dn_penalty = 5
    else:
        dn_penalty = 12

    jitter = 0 # Removing jitter for test consistency
    upi_score = BASE_RATE - lat_penalty - up_penalty - dn_penalty + jitter
    return max(5.0, min(99.8, upi_score))

# Test Data
dn = 36.20
up = 6.25
lat = 135.2

score = calculate_upi_score(dn, up, lat)
tier = "good" if score >= 75 else ("mid" if score >= 40 else "poor")

print(f"Metrics: Download={dn}Mbps, Upload={up}Mbps, Latency={lat}ms")
print(f"Calculated Score: {score}%")
print(f"Tier: {tier}")
