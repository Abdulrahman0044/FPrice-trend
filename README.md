# **Market Price Prediction for Farm Harvested Crops**

## **Project Overview**  
This project focuses on predicting the market prices of farm-harvested crops using advanced natural language processing (NLP) techniques. By leveraging data scraped from Wikipedia and training a BERT MASK model, the system provides insights into price trends, enabling better decision-making for farmers, traders, and stakeholders in the agricultural sector.  

---

## **Objectives**  
- To develop a predictive model that forecasts market prices for various crops based on historical and contextual data.  
- To utilize Wikipedia as a data source for crop-related information, including pricing trends, cultivation regions, and seasonal factors.  
- To apply state-of-the-art NLP techniques, specifically the BERT MASK model, for analyzing and deriving insights from text data.  

---

## **Methodology**  

### **1. Data Collection**  
- **Source**: Wikipedia was scraped to gather relevant data on farm-harvested crops, including:  
  - Historical price trends  
  - Crop production data  
  - Geographical and seasonal variations  
  - Market factors influencing pricing  
- **Preprocessing**: The raw data was cleaned, structured, and tokenized to prepare it for NLP-based modeling.  

### **2. Model Selection and Training**  
- **BERT MASK Model**:  
  - A pre-trained BERT (Bidirectional Encoder Representations from Transformers) MASK model was fine-tuned on the collected dataset.  
  - The MASK functionality was used to predict missing or unobserved price data based on context, improving the accuracy of the predictions.  
- **Training Pipeline**:  
  - Input text data was tokenized using WordPiece embeddings.  
  - Fine-tuning was carried out on pricing-related sentences, allowing the model to understand nuances in crop pricing trends.  
  - Optimized hyperparameters for performance improvement.  

### **3. Evaluation Metrics**  
- **Accuracy**: Measured how closely the predicted prices aligned with actual historical prices.  
- **Mean Absolute Error (MAE)**: Evaluated the prediction errors to ensure minimal deviation.  
- **Contextual Relevance**: Assessed the model's ability to derive price predictions based on contextual input.  

---

## **Key Features**  
- **Market Trend Analysis**:  
  Provides an overview of crop price fluctuations over time, helping users identify patterns and predict future trends.  

- **Dynamic Contextual Predictions**:  
  Uses the BERT MASK model to fill in gaps in the data, ensuring robust price forecasting even with incomplete inputs.  

- **Real-World Application**:  
  The model's insights are valuable for:  
  - Farmers planning crop sales  
  - Traders optimizing market strategies  
  - Policymakers developing agricultural policies  

---

## **Results**  
- **Improved Prediction Accuracy**: The fine-tuned BERT MASK model achieved high accuracy in forecasting crop prices based on historical and contextual data.  
- **Scalable Insights**: The model effectively adapted to various crop types and market conditions.  
- **Actionable Insights**: Enabled users to make informed decisions regarding crop sales and market investments.  

---

## **Challenges and Solutions**  
- **Data Imbalance**: Some crops had less historical data available.  
  - **Solution**: Used data augmentation techniques and the MASK model's contextual understanding to fill gaps.  
- **Complexity of Text Data**: Wikipedia's diverse and unstructured text posed preprocessing challenges.  
  - **Solution**: Developed a robust preprocessing pipeline to clean and structure the data effectively.  

---

## **Technologies Used**  
- **Programming Language**: Python  
- **Libraries**:  
  - `Transformers` (Hugging Face) for BERT MASK model fine-tuning  
  - `BeautifulSoup` and `Scrapy` for data scraping  
  - `Pandas` and `NumPy` for data preprocessing and analysis  
- **Evaluation Tools**: Scikit-learn for metrics calculation and performance evaluation  

---

## **Conclusion**  
This project successfully leverages the power of NLP and machine learning to predict market prices for farm-harvested crops. By utilizing Wikipedia as a data source and fine-tuning a BERT MASK model, it bridges the gap between data availability and actionable insights, empowering stakeholders in the agricultural ecosystem.  

**Future Work**: Expand the dataset to include additional sources like government reports, integrate real-time price updates, and further optimize the model for multilingual data.  

