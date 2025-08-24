# 🤖 AI Crypto Wallet Assistant

An *AI-powered portfolio assistant* that works in *two modes*:  
- 💬 *Chatbot Mode* – Ask natural language questions like "Rebalance my portfolio for passive income" and get strategies + charts.  
- 🧠 *Agent Mode* – A *24/7 autonomous agent* that analyzes your portfolio, monitors market conditions, and can execute strategies automatically on testnets.  

⚡ Built with *FastAPI, **React Native, **LangChain, **Groq, and **Web3*.

---

## ✨ Features

### 🔹 Chatbot Mode
- Natural language interface for your crypto portfolio.  
- AI generates optimal strategies (Conservative, Balanced, Aggressive).  
- Visualizes allocations with *charts & performance metrics*.  
- Users choose + implement strategies in a single click.

### 🔹 Agent Mode
- Runs in background, constantly *monitoring wallet drift*.  
- Can auto-trigger rebalancing, lending, or diversification strategies.  
- Uses testnet tokens (Sepolia ETH, LINK, custom USDC) for safe experimentation.  
- Extensible to mainnet with real assets + DeFi integrations.  

---

## 🛠 Tech Stack

*Backend*
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) – high-performance APIs  
- 🧩 LangChain + Groq – AI reasoning & RAG  
- 🔗 Web3.py + Etherscan API – wallet & on-chain execution  

*Frontend*
- 📱 React Native (Expo) – cross-platform mobile app  
- 📊 react-native-chart-kit – asset allocation & performance charts  
- 🔔 Real-time strategy notifications  

*Blockchain*
- ⛓ Ethereum Sepolia Testnet  
- 🪙 Custom ERC-20 Test USDC & faucet LINK  
- 🔒 MetaMask + Alchemy RPC  

---

## 🚀 Getting Started

### 1. Clone Repo
```sh
git clone https://github.com/yourusername/wallet.git
cd wallet

