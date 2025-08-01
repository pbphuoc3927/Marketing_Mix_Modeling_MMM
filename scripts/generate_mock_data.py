import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 1000 weekly dates
weeks = pd.date_range(start="2005-01-02", periods=10000, freq="W")

# Simulate weekly spend across 4 marketing channels
data = pd.DataFrame({
    "week": weeks,
    "tv_spend": np.random.uniform(1000, 5000, size=10000),
    "facebook_spend": np.random.uniform(500, 3000, size=10000),
    "search_spend": np.random.uniform(800, 4000, size=10000),
    "other_spend": np.random.uniform(300, 2000, size=10000),
})

# Chia chi tiêu theo ngàn đô để dễ đọc
for col in ['tv_spend', 'facebook_spend', 'search_spend', 'other_spend']:
    data[col] = data[col] / 1000

# Tạo biến revenue mới (có scale phù hợp với unit chi tiêu)
data["revenue"] = (
    8 * data["tv_spend"] +
    12 * data["facebook_spend"] +
    15 * data["search_spend"] +
    5 * data["other_spend"] +
    np.random.normal(0, 200, size=10000)
)

# Tạo thêm cột log_revenue để thử nghiệm hồi quy log
data["log_revenue"] = np.log(data["revenue"].clip(lower=1))  # tránh log(0)


# Round and export
data = data.round(2)
data.to_csv(r"C:\Users\phuoc\Marketing_Mix_Modeling_MMM\data\marketing_weekly_spend.csv", index=False)

print("✅ Mock data generated with ROI variation and clean revenue.")
