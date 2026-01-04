# Escrow2Crypto – Secure Gift Card to USDT Trading Platform

## 📌 Project Overview

**Escrow2Crypto** is a backend-driven web platform that allows users to exchange gift cards for cryptocurrency (USDT) using a secure **escrow-based trading system**.

The platform connects:
- **Buyers** who own gift cards and want USDT
- **Sellers** who own USDT and want to acquire gift cards

To prevent fraud, USDT is locked in escrow during a trade and only released after gift card verification by an **Admin / AI validation system**.

This project was built as part of the **ALX Backend Engineering Capstone**.

---

## 🎯 Problem Statement

Gift card trading is highly vulnerable to fraud.  
**Escrow2Crypto** solves this problem by:
- Locking seller’s USDT in escrow
- Verifying gift cards before releasing funds
- Providing proof when gift cards are invalid
- Automatically refunding escrowed funds when a trade fails

---

## 👥 User Roles

| Role | Description |
|----|----|
| Buyer | Owns gift card and wants USDT |
| Seller | Owns USDT and wants gift cards |
| Admin / AI | Validates gift cards and resolves disputes |

---

## ⚙️ Key Features

### 🔐 Authentication
- User signup
- Login & logout
- Token-based authentication

### 💼 Wallet System
- Built-in USDT wallet per user
- Automatic wallet creation on signup
- View wallet balance
- Deposit and withdraw USDT
- Escrow locking & releasing

### 🏷️ Offers Marketplace
- Sellers create gift card offers
- Buyers can view all available offers

### 🔄 Trade & Escrow System
- Buyer starts trade
- Seller’s USDT is locked in escrow
- Admin validates gift card
- Funds released or refunded automatically

### 📊 Trade Monitoring
- Trade status tracking (pending / completed / failed)
- Proof image attached for failed trades

---

## 🏗️ Tech Stack

| Layer | Technology |
|----|----|
| Backend | Django, Django REST Framework |
| Database | SQLite (development) |
| Authentication | Token Authentication |
| Deployment | PythonAnywhere |
| Version Control | Git & GitHub |

---

## 🗂️ Database Models (ERD Summary)

### User
- username
- email
- password
- role (buyer / seller / admin)

### Wallet
- user (OneToOne)
- usdt_balance

### Offer
- seller (FK)
- gift_card_type
- login_email
- login_password (encrypted)
- rate
- status

### Trade
- buyer (FK)
- offer (FK)
- amount
- usdt_locked
- status
- evidence_img

### Escrow
- trade (OneToOne)
- locked_usdt
- released (boolean)

---

## 🔗 API Endpoints

### Authentication
| Endpoint | Method | Description |
|------|------|------|
| `/api/auth/signup/` | POST | Register new user |
| `/api/auth/login/` | POST | Login user |
| `/api/auth/logout/` | POST | Logout user |

### Wallet
| Endpoint | Method | Description |
|------|------|------|
| `/api/wallet/balance/` | GET | View wallet balance |
| `/api/wallet/deposit/` | POST | Deposit USDT |
| `/api/wallet/withdraw/` | POST | Withdraw USDT |

### Offers
| Endpoint | Method | Description |
|------|------|------|
| `/api/offers/create/` | POST | Create offer (seller) |
| `/api/offers/` | GET | List all offers |

### Trades & Escrow
| Endpoint | Method | Description |
|------|------|------|
| `/api/trade/start/` | POST | Start trade |
| `/api/trade/<id>/status/` | GET | View trade status |
| `/api/trade/<id>/complete/` | POST | Complete trade (admin) |
| `/api/trade/<id>/fail/` | POST | Fail trade + proof (admin) |

---

## 🔄 Trade Flow

1. Seller creates offer
2. Buyer selects offer and starts trade
3. Seller’s USDT is locked in escrow
4. Admin / AI validates gift card
5. If successful:
   - Buyer receives USDT
   - Trade marked completed
6. If failed:
   - Buyer receives proof image
   - USDT returned to seller
   - Trade marked failed

---

## 🚀 Deployment (PythonAnywhere)

Deployment steps:
1. Create PythonAnywhere account
2. Upload project files
3. Create virtual environment
4. Install dependencies
5. Configure WSGI file
6. Run migrations
7. Collect static files
8. Reload web application

---

## 🧪 Testing

All endpoints were tested using **Postman**:
1. Signup user
2. Login user and retrieve token
3. Pass token in request headers:
Authorization: Token <your_token>

yaml
Copy code
4. Test wallet, offers, trades, and escrow logic

---

## 📅 Development Timeline

| Week | Focus |
|----|----|
| Week 1 | Project setup & database design |
| Week 2 | Authentication & wallet system |
| Week 3 | Offers & trade system |
| Week 4 | Escrow logic & admin controls |
| Week 5 | Deployment & documentation |

---

## 🧠 Lessons Learned

- Secure financial systems require escrow logic
- Token authentication is essential for APIs
- Production deployment requires proper configuration
- Logging is critical for debugging live systems

---

## 📌 Future Improvements

- AI-based gift card validation
- Blockchain-based USDT integration
- Dispute resolution system
- Frontend user interface (React)

---

## 👤 Author

**Name:** Fawaz  
**Program:** ALX Backend Engineering  
**Capstone Project:** Escrow2Crypto  

---

## 🏁 Conclusion

**Escrow2Crypto** demonstrates real-world backend engineering skills including authentication, wallet management, escrow handling, and secure API design using Django REST Framework.

This project represents the practical knowledge gained during the ALX Backend Engineering program