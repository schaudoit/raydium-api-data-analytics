# 📊 Raydium API Data Analytics (Solana)

This project aims to demonstrate my ability to interact with a REST API, structure financial data from the Solana blockchain, and perform an initial exploratory analysis.

---

## 🔍 Objectives

- Extract liquidity pool data from [Raydium](https://raydium.io/)
- Transform the data into a DataFrame for analysis
- Visualize top pools based on TVL (Total Value Locked)

---

## 🧠 Demonstrated Skills

- API request handling with `requests`
- Parsing structured JSON data
- Data manipulation with `pandas`
- Basic visualization with `matplotlib`
- Structuring a usable and clear Python project

---

## 📁 Graph Descriptions

### 📊 Graph 1 – Top 10 Pools by TVL (Total Value Locked)

This graph displays the 10 liquidity pools with the highest total value.

- The X-axis shows the names of the pools, i.e., token pairs (e.g., SLERF/WSOL, WSOL/USDC).
- The Y-axis shows the TVL, i.e., the total value of both tokens deposited, expressed in USD.

💡 Interpretation:  
A high TVL often reflects strong market interest in a token, high trading activity, or strong community trust in the pair.

🕒 Note:  
The displayed values represent a snapshot taken at the time of the API call.

---

### 📊 Graph 2 – Pairs with the Highest Unit Price Tokens

This graph presents the 10 pools where one of the tokens has the highest unit price, based on data extracted from the Raydium API.

- The **X-axis** shows the **token pairs** (e.g., `WSOL/Pnut`).
- The **Y-axis** shows the **unit price** (in USD) of the token in the pair.

💡 **Interpretation:**  
> A high price can indicate either a **highly valued token** by the market or a **low supply token**.  
> This graph highlights assets that have the **highest unit price** on the platform, even if they are not necessarily the most liquid or popular.

---

### 📊 Graph 3 – Popular Low-Priced Tokens (High TVL + Low Price)

This graph highlights tokens that combine a **low unit price** (less than $0.01) with a **high TVL** (over $1 million).  
These tokens are often **accessible to the general public**, heavily traded, and sometimes driven by active communities.

💡 **Interpretation:**  
> This profile often matches **memecoins or speculative assets**, which may offer high potential returns... but also come with high risk.

📌 About the $1M TVL threshold:  
A minimum TVL threshold of $1 million was set to retain only pools with significant liquidity.  
This allows us to filter out:
- Inactive or newly created pools
- Tokens with little real engagement on the platform