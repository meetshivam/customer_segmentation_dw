# Customer Segmentation Data Warehouse Project

## 📌 Project Overview

The **Customer Segmentation Data Warehouse (DW)** project is designed to analyze customer spending behavior and segment customers into meaningful groups using data warehousing and machine learning techniques.

This project follows a **complete ETL → Preprocessing → Dimensionality Reduction → Clustering → Prediction pipeline** and finally allows the **user to input spending amount and time (in days)** to predict the customer segment.

---

## 🛠️ Technologies Used

* **Python 3**
* **Pandas & NumPy** – Data manipulation
* **Scikit-learn** – PCA & K-Means clustering
* **Matplotlib / Seaborn** – Data visualization
* **Data Warehouse Concepts** – ETL, analytical processing

---

## 📂 Project Structure

```text
customer_segmentation_dw/
│
├── data/                   # Raw and processed datasets
├── scripts/                # Python scripts for each pipeline stage
│   ├── etl.py
│   ├── preprocessing.py
│   ├── pca.py
│   ├── clustering.py
│   └── user_segmentation.py
│
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python Dependencies

Make sure Python 3 is installed, then run:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project (Step-by-Step)

⚠️ **Run the following commands one by one in the given order**

---

### 🔹 Step 1: Run ETL Process

```bash
python3 scripts/etl.py
```

📌 This step:

* Extracts raw customer data
* Cleans and transforms it
* Loads it into a structured analytical format

---

### 🔹 Step 2: Data Preprocessing

```bash
python3 scripts/preprocessing.py
```

📌 This step:

* Handles missing values
* Applies feature scaling (standardization)
* Prepares data for PCA and clustering

---

### 🔹 Step 3: Apply PCA (Dimensionality Reduction)

```bash
python3 scripts/pca.py
```

📌 This step:

* Reduces high-dimensional data
* Preserves maximum variance
* Improves clustering performance and visualization

---

### 🔹 Step 4: Perform Clustering

```bash
python3 scripts/clustering.py
```

📊 **Output:**

* A **customer clustering graph** will appear on the screen

⚠️ **Important:**
➡️ **Close the clustering graph window before proceeding further**

---

### 🔹 Step 5: User-Based Customer Segmentation

```bash
python3 scripts/user_segmentation.py
```

📌 This step:

* Asks the user to input:

  * **Amount spent**
  * **Time period (in days)**

🧠 Based on the trained model, the system:

* Predicts the **customer segment**
* Displays the customer category on the terminal

---

## 📈 Example User Input

```text
Enter amount spent: 12000
Enter time in days: 45
```

### ✅ Output:

```text
Predicted Customer Segment: High-Value Customer
```

---

## 🧠 Conceptual Highlights (For Viva)

* **Data Warehouse approach** ensures structured analytical processing
* **Standardization** is used instead of normalization for PCA compatibility
* **PCA** reduces dimensionality while retaining variance
* **K-Means clustering** groups customers based on spending behavior
* **User-driven prediction** simulates real-world business decision making

---

## 🎯 Applications

* Customer behavior analysis
* Marketing strategy optimization
* Business intelligence systems
* Decision support systems

---

## 👨‍💻 Author

**Shivam Gautam**
BCA – Data Warehousing & Analytics Project

---

## 📜 License

This project is for **academic and learning purposes only**.
