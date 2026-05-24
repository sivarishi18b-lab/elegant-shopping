# 🛍️ Elegant Shopping

> A production-grade, full-featured e-commerce web application built with Django and Python.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📌 Overview

Elegant Shopping is a comprehensive e-commerce platform developed as a final year project for B.Tech in Computer Science and Engineering at SRM Institute of Science and Technology (2024–2025).

The system simulates a real-world online shopping environment with two user roles — **Customer** and **Admin** — each with a distinct set of permissions and capabilities. It covers the entire shopping lifecycle from product discovery to order delivery.

---

## ✨ Features

### 👤 User Management
- Custom user model with role-based access control (Customer / Admin)
- Secure registration and login with Django's authentication framework
- Profile management with profile picture and contact info
- Multiple delivery address management with default address support

### 🛒 Product Catalog
- Hierarchical organization: Category → SubCategory → Brand → Product
- Product variants (size, color) with individual stock tracking
- Multiple product images with primary image designation
- Dynamic discount calculation via `discount_percentage` field
- Featured products for homepage showcasing

### 🛒 Cart & Wishlist
- Database-backed persistent cart (survives session expiry)
- Real-time price calculation with discount application
- Quantity management with stock validation
- Wishlist with one-click move to cart

### 📦 Order Management
- Complete order lifecycle: `Pending → Confirmed → Processing → Shipped → Delivered`
- Price snapshot at time of purchase (not affected by future price changes)
- Order cancellation and return request support
- Admin order status management with automatic customer notification

### 💳 Payment Module
- Multiple payment methods: **Credit/Debit Card, UPI, PayPal, Cash on Delivery**
- Transaction tracking with gateway reference IDs
- Payment status lifecycle: `Pending → Completed → Failed → Refunded`
- Refund handling linked to order cancellation

### 🎟️ Coupon & Discounts
- Percentage-based and flat-amount coupons
- Time-bound validity with automatic expiry enforcement
- Minimum order value requirements
- Usage limits (single-use or multi-use)

### ⭐ Reviews & Ratings
- Star rating system (1–5) with written comments
- One review per customer per product (enforced at DB level)
- Aggregated product ratings displayed on listing and detail pages

### 🔔 Notification System
- Automatic notifications on order placement and status changes
- Read/unread tracking with badge count in navigation
- Admin broadcast notifications to all customers

### 🖥️ Admin Dashboard
- Summary widgets: total users, orders, revenue, low-stock alerts
- Full product catalog management (add/edit/delete)
- Order processing and status updates
- User account management
- Coupon creation and deactivation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.9+, Django 4.2 |
| Database | SQLite (development), MySQL 8.0 (production) |
| ORM | Django ORM |
| Frontend | HTML5, CSS3, JavaScript |
| UI Framework | Bootstrap 5 |
| Authentication | Django Auth + Custom User Model |
| Payment | Razorpay / PayPal SDK |
| Forms | Django Forms |
| Admin | Django Admin Panel (customized) |

---

## 🏗️ Architecture

The project follows Django's **MVT (Model-View-Template)** pattern:

```
elegant-shopping/
├── manage.py
├── requirements.txt
├── elegantshop/             # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/                   # Main application
│   ├── models.py            # All data models
│   ├── views.py             # Business logic
│   ├── urls.py              # URL routing
│   ├── forms.py             # Form definitions
│   ├── admin.py             # Admin configuration
│   └── signals.py           # Event-driven automation
├── templates/               # HTML templates
│   ├── base.html
│   ├── store/
│   └── admin/
└── static/                  # CSS, JS, Images
    ├── css/
    ├── js/
    └── images/
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip
- Git

### 1. Clone the repository
```bash
git clone https://github.com/SivarishiB/elegant-shopping.git
cd elegant-shopping
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (Admin account)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 🗄️ Database Models

| Model | Description |
|-------|-------------|
| `CustomUser` | Extended AbstractUser with role, phone, profile picture |
| `Category / SubCategory` | Two-level product hierarchy |
| `Brand` | Product brand management |
| `Product` | Core product with pricing, stock, discount |
| `ProductVariant` | Size/color variants with individual stock |
| `ProductImage` | Multiple images per product |
| `Cart / CartItem` | Persistent shopping cart |
| `Wishlist / WishlistItem` | Saved products for later |
| `Address` | Multiple delivery addresses per user |
| `Order / OrderItem` | Order with price snapshot line items |
| `Payment` | Transaction records with gateway integration |
| `Coupon` | Promotional discount codes |
| `Review` | Star ratings and written reviews |
| `Notification` | User alerts with read/unread tracking |

---

## 🧪 Testing

The project achieved **100% pass rate across 99 test cases**:

| Category | Test Cases | Passed |
|----------|-----------|--------|
| Unit Tests (Models) | 24 | 24 ✅ |
| Unit Tests (Views) | 18 | 18 ✅ |
| Integration Tests | 12 | 12 ✅ |
| Functional Tests | 30 | 30 ✅ |
| User Acceptance Tests | 15 | 15 ✅ |
| **Total** | **99** | **99** |

Run tests with:
```bash
python manage.py test
```

---

## 🚀 Future Enhancements

- [ ] AI-based product recommendation engine (scikit-learn / TensorFlow)
- [ ] Real-time notifications with Django Channels (WebSockets)
- [ ] REST API with Django REST Framework for mobile app support
- [ ] Flutter / React Native mobile application
- [ ] Celery + Redis for async email and payment processing
- [ ] Elasticsearch for advanced product search
- [ ] Multi-language and multi-currency support
- [ ] Cloud deployment on AWS with CDN (CloudFront)
- [ ] Customer loyalty points system
- [ ] Progressive Web App (PWA) support

---

## 👨‍💻 Author

**Sivarishi B**
- 📧 sivarishi.b18@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/sivarishi-b-0200b6296)
- 🐙 [GitHub](https://github.com/SivarishiB)
- 🌐 [Portfolio](https://sivarishi-b.github.io)

---

## 📄 License

This project is licensed under the MIT License — feel free to use it for learning and personal projects.

---

*Final Year Project — B.Tech Computer Science & Engineering, SRM Institute of Science and Technology, 2024–2025*
