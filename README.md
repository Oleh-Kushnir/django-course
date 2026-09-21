# Store Server — E-Commerce Web Platform & REST API

A scalable, full-featured e-commerce platform engineered with **Django** and **Django REST Framework (DRF)**. The project covers the end-to-end e-commerce lifecycle, featuring asynchronous task processing, third-party payment gateways, caching, and clean Class-Based Views architecture.

---

## ⚡ Key Highlights & Engineering Features

* **Authentication & User Management:**
  * Custom User model extending Django's auth ecosystem.
  * Time-limited token-based email activation via dedicated verification models.
  * Social authentication powered by **OAuth2**.
  * User profile management with order history tracking.

* **Catalog, Query Optimization & Caching:**
  * Efficient product browsing with multi-level category filtering and pagination (PageNumber & LimitOffset).
  * Low-level database query caching and template fragment caching via **Redis** to eliminate redundant DB hits.
  * Dynamic, non-reloading cart updates with asynchronous frontend interactions.

* **Payment Infrastructure (Stripe):**
  * Integrated **Stripe Checkout API** for secure, PCI-compliant card transactions.
  * Real-time **Stripe Webhooks** listener handling asynchronous payment confirmations and automated order state transitions.

* **RESTful Architecture (DRF):**
  * Standalone API endpoints for product catalogs, carts, and customer profiles.
  * Serializers handling data transformation and validation.
  * Fine-grained permissions and dual-scheme auth support (`SessionAuthentication`, `BasicAuthentication`).

* **Background Workers & Tasks:**
  * **Celery** integration backed by **Redis** as a message broker for deferred operations (transactional emails, notification queues).

* **Reliability & Code Quality:**
  * Automated testing coverage (`django.test.TestCase`) covering models, views, and critical endpoints.
  * Strict PEP 8 compliance maintained via **Flake8**.
  * Strict separation of configuration and secrets using environment variables.

---

## 🛠 Tech Stack

| Domain | Technologies |
| :--- | :--- |
| **Core & Frameworks** | Python 3.11+, Django, Django REST Framework |
| **Database** | PostgreSQL, SQLite |
| **Async & Caching** | Celery, Redis |
| **Payments** | Stripe API, Stripe Webhooks |
| **Auth & Security** | OAuth2, Session/Basic Auth, Token Verification |
| **Code Standards** | Flake8, django-environ 
| **Frontend:** Django Templates, HTML5, CSS3, Bootstrap, JavaScript/jQuery|

---
