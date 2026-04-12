# 📜 Skill: Structured Logging (Loguru)

> **Svrha:** Zamena manuelnog upisivanja JSON blokova u `WORK_LOG.md` modernim, strukturiranim logging sistemom.

---

## 💎 GitHub Gem: Loguru
- **Repo:** [https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)
- **Zašto:** Jednostavan API, automatska rotacija logova, JSON serijalizacija, i podrška za asinhrono logovanje.

---

## 🚀 Workflow

### 1. Instalacija
```bash
pip install loguru
```

### 2. Konfiguracija
```python
from loguru import logger
import sys

# Konfiguriši logovanje u fajl sa JSON formatom
logger.add("WORK_LOG.json", format="{time} {level} {message}", serialize=True, rotation="10 MB")
```

### 3. Implementacija u kodu
Zameni manuelno upisivanje u `WORK_LOG.md` sa:
```python
# Umesto manuelnog json.dump u fajl:
logger.info("SSOT parametri uspešno učitani", 
            extra={"config_path": config_path, "parameters": loaded_parameters})

# Za greške:
logger.error("Greška pri učitavanju konfiguracije", 
             extra={"config_path": config_path})
```

---

## 📋 Pravila
- Koristi `serialize=True` za mašinski čitljive logove (JSON).
- Koristi `rotation` i `retention` da sprečiš prevelike log fajlove.
- Loguj kontekstualne podatke kroz `extra` polja umesto u samoj poruci.
