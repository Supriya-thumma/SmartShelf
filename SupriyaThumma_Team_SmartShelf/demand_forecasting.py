# demand_forecasting.py
import ollama

def predict_demand(model_name, input_data):
    predictions = {}

    for _, row in input_data.iterrows():
        print(f"Predicting demand for Product ID: {row['Product ID']}")
    
        prompt = (
            f"Given the product with the following details:\n"
            f"Date: {row['Date']}\n"
            f"Store ID: {row['Store ID']}\n"
            f"Price: {row['Price']}\n"
            f"Promotions: {row['Promotions']}\n"
            f"Seasonality: {row['Seasonality Factors']}\n"
            f"External Factors: {row['External Factors']}\n"
            f"Demand Trend: {row['Demand Trend']}\n"
            f"Customer Segment: {row['Customer Segments']}\n\n"
            f"Predict the expected sales quantity."
        )

        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )

        try:
            prediction = int(response['message']['content'].strip())
        except (ValueError, KeyError):
            prediction = 0

        product = row['Product ID']
        predictions[product] = prediction

    return predictions
