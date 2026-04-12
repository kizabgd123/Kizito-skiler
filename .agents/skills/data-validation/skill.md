# ✅ Skill: Data Validation (Cerberus)

> **Svrha:** Zamena manuelnih provera u `verify_ssot_parameters` deklarativnim šemama za validaciju podataka.

---

## 💎 GitHub Gem: Cerberus
- **Repo:** [https://github.com/pyeve/cerberus](https://github.com/pyeve/cerberus)
- **Zašto:** Lagan, proširiv, i omogućava definisanje pravila validacije u obliku Python rečnika.

---

## 🚀 Workflow

### 1. Instalacija
```bash
pip install cerberus
```

### 2. Definisanje šeme
```python
schema = {
    'system_parameters': {
        'type': 'dict',
        'schema': {
            'cpu_timeout_seconds': {'type': 'integer', 'min': 1, 'max': 3600}
        }
    },
    'validation_thresholds': {
        'type': 'dict',
        'schema': {
            'baseline_oof_score': {'type': 'float', 'min': 0.0, 'max': 1.0}
        }
    }
}
```

### 3. Implementacija u kodu
Zameni manuelne provere sa:
```python
from cerberus import Validator

v = Validator(schema)
if v.validate(config):
    print("Konfiguracija je validna.")
else:
    print(f"Greške u konfiguraciji: {v.errors}")
```

---

## 📋 Pravila
- Uvek definiši `min` i `max` vrednosti za numeričke parametre.
- Koristi `required: True` za kritične parametre.
- Validaciju vrši odmah nakon učitavanja podataka iz eksternog izvora.
