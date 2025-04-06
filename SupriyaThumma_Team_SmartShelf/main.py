# main.py
from data_handler import load_data, preprocess_data
from demand_forecasting import predict_demand
from agents import StoreAgent, WarehouseAgent, SupplierAgent, CustomerAgent

def main():
    file_paths = [
        r'C:\Users\Supriya\Downloads\SupriyaThumma_Team_SmartShelf\demand_forecasting.csv',
        r'C:\Users\Supriya\Downloads\SupriyaThumma_Team_SmartShelf\inventory_monitoring.csv',
        r'C:\Users\Supriya\Downloads\SupriyaThumma_Team_SmartShelf\pricing_optimization.csv'
    ]

    data_dict = load_data(file_paths)
    for key in data_dict:
        data_dict[key] = preprocess_data(data_dict[key])

    demand_data = data_dict['demand_forecasting']
    demand_data = demand_data.head(3)  # only use first 3 rows for quick test
    demand_predictions = predict_demand('tinyllama', demand_data)

    store_agent = StoreAgent(store_id=1)
    warehouse_agent = WarehouseAgent()
    supplier_agent = SupplierAgent()
    customer_agent = CustomerAgent()

    for product_id, predicted_demand in demand_predictions.items():
        current_inventory = store_agent.check_inventory().get(product_id, 0)

        if current_inventory < predicted_demand:
            quantity_needed = predicted_demand - current_inventory
            warehouse_agent.restock(product_id, quantity_needed)
            supplier_agent.supply(product_id, quantity_needed)
            store_agent.update_inventory(product_id, quantity_needed)

        customer_agent.provide_feedback(product_id)

if __name__ == "__main__":
    main()
