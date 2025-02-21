#  Ship24TrackingAPI-Django

A Django-based package tracking system with real-time tracking updates and in-memory caching for faster responses

## Installation


### 1. Ship24 Integration Setup

1. **Create an Account**  
   Register at [Ship24 Dashboard](https://dashboard.ship24.com/).

2. **Subscribe to "Tracking API & Webhook (Per-shipment plans)" (It's free)**  
   Go to [Subscriptions](https://dashboard.ship24.com/general/subscriptions) and select **"Tracking API & Webhook (Per-shipment plans)"**.

3. **Generate API Key**  
   Navigate to [API Keys](https://dashboard.ship24.com/integrations/api-keys) and create a new API key.

4. **Configure API Key in .env**  
   Copy the generated key and add it to your `.env` file. There is `.env.sample` as an example.

### 2. Run Project
#### Docker
```
git clone https://github.com/haldaniko/Ship24TrackingAPI-Django.git
cd Ship24TrackingAPI-Django

(Copy .env.sample to .env and populate it with all required data)

docker-compose build
docker-compose up
```

#### Manual
```
git clone https://github.com/haldaniko/Ship24TrackingAPI-Django.git
cd Ship24TrackingAPI-Django

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

(Copy .env.sample to .env and populate it with all required data)

python manage.py runserver
```

Application will be available at http://127.0.0.1:8000

Shortcut for fast use http://127.0.0.1:8000/tracking/00340434521313139299/ (valid for 15.01.2025)