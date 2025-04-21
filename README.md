# Data-Analytics-and-Big-Data
IU International University of Applied Sciences


# 📊 Airbnb Data Analytics in Sydney

This repository contains a comprehensive data analytics project that explores the impact of Airbnb on the urban housing landscape of **Sydney, Australia**. The analysis applies the **CRISP-DM framework** and leverages Python for data processing, visualization, and sentiment analysis.

---

## 🧠 Project Objective

To analyze Airbnb's presence in Sydney using publicly available datasets from [Inside Airbnb](http://insideairbnb.com/), with a focus on:

- Listing distribution across neighborhoods
- Property types and host professionalism
- Booking duration trends
- Price and listing time series
- Guest sentiment through topic modeling

---

## 📁 Repository Structure

📦airbnb-sydney-analysis/ ┣ 📜README.md ┣ 📜load_clean_listings.py ┣ 📜top_neighborhoods_visualization.py ┣ 📜rental_type_distribution.py ┣ 📜professional_host_detection.py ┣ 📜booking_duration_classification.py ┣ 📜listings_price_time_series.py ┣ 📜guest_review_sentiment_lda.py ┣ 📜listings.csv ┗ 📜reviews.csv


---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Pandas** – Data manipulation
- **Matplotlib & Seaborn** – Visualizations
- **Gensim & NLTK** – Topic modeling and NLP
- **CRISP-DM Framework** – Structured data analysis

---

## 📊 Key Insights

✔ Airbnb listings are heavily concentrated in **inner-city neighborhoods** like Surry Hills, Darlinghurst, and Bondi Beach  
✔ Most properties in these areas are **entire homes**, often run by **professional hosts**  
✔ **Short-term rentals** dominate the central neighborhoods  
✔ **LDA sentiment analysis** revealed 5 major concerns:
- Cleanliness & Hygiene  
- Host Communication  
- Location Accessibility  
- Noise & Neighborhood Disturbance  
- Value for Money  

---

## 🧪 Files Description

| File Name                        | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `load_clean_listings.py`        | Loads and preprocesses Airbnb listings dataset                              |
| `top_neighborhoods_visualization.py` | Visualizes top 10 neighborhoods by listing count                          |
| `rental_type_distribution.py`   | Shows distribution of room types across Sydney                              |
| `professional_host_detection.py`| Classifies hosts into professional and individual types                     |
| `booking_duration_classification.py` | Categorizes listings into short vs. long-term stays                     |
| `listings_price_time_series.py` | Time series analysis of listing volume and average prices                   |
| `guest_review_sentiment_lda.py` | LDA topic modeling on guest reviews to extract top guest concerns           |

---

## 🖼️ Visuals Included

- 📍 Top 10 Neighborhoods by Listings
- 🏠 Distribution of Property Types
- 📈 Time Series of Listings and Price
- 💬 Topics Discovered in Guest Reviews (LDA)

---

## 📚 Citation

This work is based on the academic case study submitted as part of:
> **Data Analytics and Big Data (DLBINGDABD01_E)**  
> IU International University of Applied Sciences  
> Professor: Martin Ejeagwu  
> Date: April 18, 2025  
> Author: Mosbah Alalawi, Matriculation ID: 92113854  

📄 **APA Citations used** (Full reference list available in the report)

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/airbnb-sydney-analysis.git
   cd airbnb-sydney-analysis

2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn nltk gensim

3. Run any script using:
   ```bash
   python filename.py


## Outputs

<img width="959" alt="image" src="https://github.com/user-attachments/assets/2f1722ca-f81d-4590-bc4b-5df4c54fdf7d" />
<img width="1439" alt="image" src="https://github.com/user-attachments/assets/e6eee7aa-34b8-4dd0-b4b3-4a5f6f20b4f3" />
<img width="637" alt="image" src="https://github.com/user-attachments/assets/7f43b2bd-f928-4e20-ac8b-d57e85a4f715" />
<img width="638" alt="image" src="https://github.com/user-attachments/assets/8b07365d-3dfb-4cb2-88e6-73c619d105db" />




