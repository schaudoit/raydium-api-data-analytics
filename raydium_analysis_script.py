# Script principal d'analyse Raydium – version Python (équivalent du notebook)
from TokensApi import get_all_pools_data
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 📡 Chargement des données depuis Raydium API
print("📡 Loading data from Raydium API...")
raw_data = get_all_pools_data()
df = pd.DataFrame(raw_data)
print("📋 Colonnes disponibles :", df.columns)

# 🧹 Nettoyage et conversion
df["tvl"] = pd.to_numeric(df.get("liquidity", None), errors="coerce")
df["volume24h"] = pd.to_numeric(df.get("volume24h", None), errors="coerce")
df["price"] = pd.to_numeric(df.get("price", None), errors="coerce")

# 📊 Graphique 1 – Top 10 pools par TVL
top_tvl = df.sort_values(by="tvl", ascending=False).head(10)
print("\n✅ Top 10 pools par TVL :\n")
print(top_tvl[["name", "tvl", "volume24h", "price"]])

plt.figure(figsize=(10, 5))
plt.bar(top_tvl["name"], top_tvl["tvl"])
plt.xticks(rotation=45)
plt.ylabel("TVL (Total Value Locked)")
plt.title("Graphique 1 – Top 10 Raydium Pools par TVL")
plt.tight_layout()
plt.show()

# 📊 Graphique 2 – Tokens avec le prix unitaire le plus élevé
top_prices = df.sort_values(by="price", ascending=False).head(10)
print("\n💰 Top 10 tokens par prix unitaire :\n")
print(top_prices[["name", "price", "tvl"]])

plt.figure(figsize=(10, 5))
plt.bar(top_prices["name"], top_prices["price"])
plt.xticks(rotation=45)
plt.ylabel("Prix unitaire ($)")
plt.title("Graphique 2 – Tokens au prix unitaire le plus élevé")
plt.tight_layout()
plt.show()

# 📊 Graphique 3 – Tokens populaires à bas prix (TVL > 1M & prix < 0.01)
filtered_low_price = df[
    (df["tvl"] > 1_000_000) & 
    (df["price"] < 0.01)
].sort_values(by="tvl", ascending=False).head(10)

print("\n🔥 Tokens à bas prix mais à forte TVL :\n")
print(filtered_low_price[["name", "tvl", "price"]])

plt.figure(figsize=(10, 5))
plt.bar(filtered_low_price["name"], filtered_low_price["tvl"])
plt.xticks(rotation=45)
plt.ylabel("TVL (USD)")
plt.title("Graphique 3 – Tokens populaires à prix bas")
plt.tight_layout()
plt.show()