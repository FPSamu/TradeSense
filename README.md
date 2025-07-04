# 📈 TradeSense

> **A real-time trading analysis tool powered by AI, technical indicators, and news sentiment analysis.**

TradeSense is an intelligent system designed for day traders — from beginners to advanced — who want to improve their decision-making process through data-driven strategies. The platform analyzes market prices, technical indicators, and news sentiment to provide trade suggestions in real-time.

---

## 🔧 Tech Stack

| Layer         | Technology                    |
|---------------|-------------------------------|
| Frontend      | React + Vite (to be deployed on Vercel) |
| Backend       | FastAPI (Python)              |
| Data analysis | Python (NumPy, Pandas, scikit-learn) |
| AI / ML       | Custom-trained models         |
| APIs used     | Finnhub / Alpha Vantage (price data), NewsAPI (financial news) |
| Container     | Docker                        |
| Versioning    | Git + GitHub (Git Flow)       |

---

## 🚀 Features

- 🔍 Real-time market price retrieval via external APIs
- 📊 Technical analysis with indicators (RSI, MACD, SMA, etc.)
- 🧠 News sentiment analysis using AI models
- 📈 Trade recommendation engine for day trading
- 🧪 Backtesting system (planned)
- 🧰 Fully containerized with Docker
- 🌐 Public web interface (in development)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tradesense.git
cd tradesense
```

### 2. Setup Python virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file
> Create a .env file with your API keys:
```bash
API_KEY_FINNHUB=your_api_key
API_KEY_NEWSAPI=your_news_api_key
```

### 5. Run FastAPI server locally
```bash
uvicorn main:app --reload
```

### 6. Access the API
> Swagger UI will be available at:
```bash
http://localhost:8000/docs
```

### 🐳 Docker
> You can also run the project in a Docker container:
```bash
docker build -t tradesense-backend .
docker run -p 8000:8000 tradesense-backend
```

### 📡 API Endpoints
| Method | Endpoint            | Description                      |
| ------ | ------------------- | -------------------------------- |
| GET    | `/price?symbol=XYZ` | Get real-time price for a symbol |
| GET    | `/health`           | Check server health              |

### 👨‍💻 Author
Samuel Pia
Software Engineering Student
[LinkedIn Profile](https://www.linkedin.com/in/samupif/)