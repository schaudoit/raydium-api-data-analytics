# Main analysis script – Python version (equivalent to the Jupyter notebook)
from TokensApi import get_all_pools_data
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 📡 Loading data from the Raydium API
print("📡 Loading data from the Raydium API...")
raw_data = get_all_pools_data()
df = pd.DataFrame(raw_data)
print("📋 Available columns:", df.columns)

# 🧹 Data cleaning and conversion
df["tvl"] = pd.to_numeric(df.get("liquidity", None), errors="coerce")
df["volume24h"] = pd.to_numeric(df.get("volume24h", None), errors="coerce")
df["price"] = pd.to_numeric(df.get("price", None), errors="coerce")

# 📊 Graph 1 – Top 10 pools by TVL
top_tvl = df.sort_values(by="tvl", ascending=False).head(10)
print("\n✅ Top 10 pools by TVL:\n")
print(top_tvl[["name", "tvl", "volume24h", "price"]])

plt.figure(figsize=(10, 5))
plt.bar(top_tvl["name"], top_tvl["tvl"])
plt.xticks(rotation=45)
plt.ylabel("TVL (Total Value Locked)")
plt.title("Graph 1 – Top 10 Raydium Pools by TVL")
plt.tight_layout()
plt.show()

# 📊 Graph 2 – Tokens with the highest unit price
top_prices = df.sort_values(by="price", ascending=False).head(10)
print("\n💰 Top 10 tokens by unit price:\n")
print(top_prices[["name", "price", "tvl"]])

plt.figure(figsize=(10, 5))
plt.bar(top_prices["name"], top_prices["price"])
plt.xticks(rotation=45)
plt.ylabel("Unit price ($)")
plt.title("Graph 2 – Tokens with highest unit price")
plt.tight_layout()
plt.show()

# 📊 Graph 3 – Popular low-priced tokens (TVL > 1M & price < 0.01)
filtered_low_price = df[
    (df["tvl"] > 1_000_000) & 
    (df["price"] < 0.01)
].sort_values(by="tvl", ascending=False).head(10)

print("\n🔥 Low-priced tokens with high TVL:\n")
print(filtered_low_price[["name", "tvl", "price"]])

plt.figure(figsize=(10, 5))
plt.bar(filtered_low_price["name"], filtered_low_price["tvl"])
plt.xticks(rotation=45)
plt.ylabel("TVL (USD)")
plt.title("Graph 3 – Popular low-priced tokens")
plt.tight_layout()
plt.show()