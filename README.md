# django-cf

## ⚠️ Experimental Django setup for exploring Cloudflare Worker and Pages integration

This repository represents an ongoing effort to adapt a Django project (`django-cf`) for deployment via [Cloudflare Pages](https://pages.cloudflare.com/) and optionally [Cloudflare Workers](https://developers.cloudflare.com/workers/). While the static assets build and deploy correctly, full support for Python-based Workers (including Django runtime) is currently **not available** on Cloudflare’s platform.

---

## 🚀 Current Status

- ✅ Static files successfully built via `collectstatic`
- ❌ Cloudflare Workers cannot deploy Django runtime (`wsgi.py`) due to unsupported Python package dependencies
- 📦 `requirements.txt` and `cf-requirements.txt` are used in local builds only
