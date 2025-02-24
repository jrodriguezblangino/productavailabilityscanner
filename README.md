🌍 Available languages:  
- 🇪🇸 [Español](README.md)  
- 🇬🇧 [English](README.en.md)  



# 🚀 Monitor de Disponibilidad de Productos

Sistema automatizado para detectar cambios de disponibilidad de productos en sitios web, con notificaciones sonoras y monitoreo paralelo.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)

## 🌟 Características Principales
- ✅ Monitoreo simultáneo de múltiples URLs
- 🔍 Detección inteligente de texto indicador de stock
- 🔊 Sistema de notificaciones sonoras
- ⚡ Ejecución multi-hilos
- 🛡️ Manejo robusto de errores HTTP

## 📥 Instalación

### Requisitos previos
- Python 3.8 o superior
- Sistema operativo Windows (para alertas sonoras)


### Instalar dependencias principales

    pip install requests beautifulsoup4
    pip install winsound


## 🚦 Configuración Rápida

1. Editar el archivo `main.py`:

### Configurar tus URLs y parámetros

    product_urls = [
    "https://tienda-ejemplo.com/producto-1",
    "https://tienda-ejemplo.com/producto-2"
    ]
    sold_out_keyword = "AGOTADO" # Texto exacto que indica falta de stock
    interval = 60 # Intervalo de verificación en segundos



## 📚 Dependencias
| Librería | Función | Versión |
|----------|---------|---------|
| `requests` | Manejo de solicitudes HTTP | 2.31.0+ |
| `beautifulsoup4` | Análisis de contenido HTML | 4.12.0+ |
| `winsound` | Alertas sonoras (Windows) | Incluida en Python |



>[!NOTE]  
>**Consideraciones Clave**
>- El intervalo mínimo recomendado es de 60 segundos
>- Las alertas sonoras solo funcionan en Windows
>- Verificar políticas de scraping de cada sitio web
>- Actualizar los selectores HTML si cambia la estructura de la página


## ⚖️ Licencia
Este proyecto se distribuye bajo licencia MIT. Úsalo responsablemente.