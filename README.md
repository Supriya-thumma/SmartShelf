# 🛒 SmartShelf - a Smart approach Optimizing Retail Inventory with Multi Agents

## 📌 Problem Statement
Retail businesses often face challenges in balancing supply and demand due to unpredictable customer behavior, seasonal changes, and logistical delays. This leads to either overstocking or stockouts, impacting revenue and customer satisfaction.

## 💡 Proposed Solution
We developed a Multi-Agent AI system using TinyLLaMA and Python that dynamically forecasts demand and facilitates real-time inventory management. By simulating interactions between Store, Warehouse, Supplier, and Customer agents, our system optimizes inventory flows across the supply chain.

## 🔍 Methodology
- Demand data is preprocessed and passed to the TinyLLaMA model using the Ollama framework.
- The model predicts future sales quantity based on historical and contextual product data.
- Based on predictions, agents interact: stores request stock, warehouses fulfill or escalate to suppliers, and customer feedback is simulated.
- Inventory levels are updated accordingly, ensuring optimal stock availability.

## ⚙️ Technologies Used
- **Python 3.9+**
- **Pandas** for data handling
- **Ollama API** with **TinyLLaMA** for demand forecasting
- **Multi-Agent Design** (StoreAgent, WarehouseAgent, SupplierAgent, CustomerAgent)
- **Matplotlib** (optional for visualizations)
- CSV files for input datasets

## 🧠 Code Structure
- ├── main.py # Main execution file
- ├── data_handler.py # Loads and preprocesses CSV data
- ├── demand_forecasting.py # Uses TinyLLaMA to predict sales demand
- ├── agents.py # Defines logic for multi-agent interaction
- ├── datasets/
- │ ├── demand_forecasting.csv
- │ ├── inventory_monitoring.csv
- │ └── pricing_optimization.csv

  
## 🔄 Agent Interaction Design
- **Store Agent** checks inventory and requests restocks.
- **Warehouse Agent** verifies availability and supplies to the store.
- **Supplier Agent** provides goods to warehouse if needed.
- **Customer Agent** gives feedback simulating satisfaction or demand shifts.

## 📊 Example Output
- Predicting demand for Product ID: 4277
- Predicting demand for Product ID: 5540
- Predicting demand for Product ID: 5406
- Customer feedback for 4277
- Customer feedback for 5540
- Customer feedback for 5406


## 📎 References
- Datasets provided by the problem statement.
- [Ollama Documentation](https://ollama.com/library/tinyllama) for TinyLLaMA integration.
- Medium articles for using Ollama in local environments.
- Python official docs for syntax and packages.

## ✅ Conclusion
SmartShelf showcases the power of combining AI-based forecasting with agent-based systems to automate inventory optimization. It provides a scalable, modular approach to solving supply chain inefficiencies in retail.

---

Feel free to contribute, fork, or adapt the project for your own retail AI solutions!


