# Usecase-7




## 📊 Dataset Information

### 📁 Dataset: `final_data.csv`
This dataset contains football player statistics, including performance metrics, appearances, goals, assists, disciplinary records, and market value.

### 🔍 Dataset Overview:
- **File Format:** CSV 
- **Number of Players:** **10,754**
- **Number of Features:** **22**


### 🔑 Key Features:
| Feature Name           | Type      | Description |
|------------------------|-----------|-------------|
| `player`              | String    | Unique identifier for the player. |
| `team`                | String    | Club the player is associated with. |
| `position`            | String    | Position played (Goalkeeper, Defender, Midfielder, Forward). |
| `height`              | Float     | Player’s height in cm. |
| `age`                 | Float     | Player’s age. |
| `appearance`          | Integer   | Number of games played. |
| `goals`               | Float     | Goals scored. |
| `assists`             | Float     | Assists provided. |
| `yellow cards`        | Float     | Number of yellow cards. |
| `red cards`           | Float     | Number of red cards. |
| `goals conceded`      | Float     | Goals conceded (relevant for goalkeepers/defenders). |
| `clean sheets`        | Float     | Matches without conceding a goal. |
| `minutes played`      | Integer   | Total minutes played. |
| `days_injured`        | Integer   | Number of days the player was injured. |
| `games_injured`       | Integer   | Number of games missed due to injury. |
| `award`              | Integer   | Individual awards won. |
| `current_value`       | Integer   | Current estimated market value (€). |
| `highest_value`       | Integer   | Highest market value (€). |
| `position_encoded`    | Integer   | Encoded numerical version of position. |
| `winger`              | Integer   | Binary (1 = Winger, 0 = Not a Winger). |

---


## 📌 Models Used
The following machine learning models were explored and implemented:
- **K-Means Clustering** (Used in the final application)
- **DBSCAN**
- **Decision Tree & Random Forest**
- **K-Nearest Neighbors (KNN)**
- **Linear Regression**
- **Logistic Regression**
- **Support Vector Machine (SVM)**

## 🚀 Deployment
The **K-Means** clustering model was selected for deployment using **FastAPI**.

### 🔗 Live Links:
- **Web App:** [Streamlit Application](https://usecase-7-xrpdn6mocfmcpwmkbbdpvg.streamlit.app)
- **API Endpoint:** [FastAPI Prediction Endpoint](https://detest-bsd7.onrender.com/predict)
