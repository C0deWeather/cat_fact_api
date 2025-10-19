# 🐱 Cat Fact API

A simple RESTful API built with **Flask** that returns a user profile alongside a random cat fact fetched from an external API.

## 🚀 Features
- Built with **Flask**.
- Single endpoint `/me` that returns:
  - Basic user information (name, email, stack).
  - A random cat fact from [catfact.ninja/fact](https://catfact.ninja/fact).
  - A UTC timestamp in ISO 8601 format.
- Deployed on **Railway**.
- No authentication required.

---

## 🛠️ Technologies Used
- **Python 3**
- **Flask** — lightweight web framework
- **Requests** — to fetch external cat facts

---

## ⚙️ Getting Started

### 1. Clone the repository
```
git clone https://github.com/C0deWeather/cat_fact_api.git
cd cat_fact_api

```
### 2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run the application
```
python3 app.py
```
By default, the app runs at http://localhost:5000/me


---

## 📡 API Endpoint

GET /me

Returns user profile information along with a random cat fact.

Example Response
```
{
  "status": "success",
  "user": {
    "name": "John Doe",
    "email": "example@email.com",
    "stack": "Backend Developer"
  },
  "fact": "Cats sleep 70% of their lives.",
  "timestamp": "2025-10-19T12:34:56.789Z"
}

```
---

## 🧱 Project Structure
```

├── app.py
├── requirements.txt
|── Procfile
└── README.md
```

---

## 🚢 Deployment

This project is deployed on Railway at:
```
👉 https://web-production-f3714.up.railway.app/me
```
