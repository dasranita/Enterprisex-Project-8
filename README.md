# EnterpriseX — Project 08
Educational ERP prototype for procurement, inventory and accounting. Not a complete 15-assessment submission. Synthetic data only; no authentication; local use only.

## Run
Start Docker Desktop, then `docker compose up --build`. Open http://localhost:3000. API health: http://localhost:4000/health. Finance Swagger: http://localhost:8000/docs.

## Demo
Seed vendor and product IDs are 1. Create a purchase with quantity and unit cost in integer cents, approve, then receive and pay. The combined posting locks the purchase row, updates stock and creates balanced journal entries in one transaction. Repeating payment returns the existing paid purchase. This simplified workflow does not implement separate receipt, invoice matching or actual payments.

## Architecture
Browser → Express → PostgreSQL. FastAPI exposes a standalone tax calculation. Redis is provisioned but unused. SQL uses parameterized queries and row locking. See docs/assessment-status.md.

## Tests
`docker compose run --rm finance pytest -q`. Full stack and concurrency tests have not been executed.
