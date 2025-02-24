# 🚀 Product Availability Monitor  

Automated system to detect product availability changes on websites, with sound notifications and parallel monitoring.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)

## 🌟 Main Features
- ✅ Simultaneous monitoring of multiple URLs
- 🔍 Smart detection of stock indicator text
- 🔊 Sound notification system
- ⚡ Multi-threaded execution
- 🛡️ Robust handling of HTTP errors

## 📥 Installation

### Requisitos previos
- Python 3.8 or higher
- Windows operating system (for sound alerts)


### Install main dependencies

    pip install requests beautifulsoup4
    pip install winsound


## 🚦 Quick Setup

1. Edit the `main.py` file:

### Configure your URLs and parameters

    product_urls = [
    "https://tienda-ejemplo.com/producto-1",
    "https://tienda-ejemplo.com/producto-2"
    ]
    sold_out_keyword = "AGOTADO" # Texto exacto que indica falta de stock
    interval = 60 # Intervalo de verificación en segundos



## 📚 Dependencies
| Library | Function | Version |
|----------|---------|---------|
| `requests` | HTTP request handling | 2.31.0+ |
| `beautifulsoup4` | HTML content parsing | 4.12.0+ |
| `winsound` | Sound alerts (Windows) | Included in Python |



>[!NOTE]  
>**Key Considerations**
>- The recommended minimum interval is 60 seconds
>- Sound alerts only work on Windows
>- Check each website's scraping policies
>- Update HTML selectors if the page structure changes


## ⚖️ License
This project is distributed under the MIT license. Use it responsibly.