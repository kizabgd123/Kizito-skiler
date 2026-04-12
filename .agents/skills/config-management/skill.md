# 🛠️ Skill: Advanced Configuration Management (Dynaconf)

> **Svrha:** Zamena manuelnog učitavanja JSON konfiguracija robusnim, slojevitim sistemom za upravljanje postavkama.

---

## 💎 GitHub Gem: Dynaconf
- **Repo:** [https://github.com/dynaconf/dynaconf](https://github.com/dynaconf/dynaconf)
- **Zašto:** Podržava više formata (JSON, YAML, TOML), env varijable, validaciju i slojevito učitavanje (default -> settings -> local).

---

## 🚀 Workflow

### 1. Instalacija
```bash
pip install dynaconf
```

### 2. Inicijalizacija
Kreiraj `settings.toml` (ili konvertuj postojeći `trinity_config.json`):
```toml
[default]
cpu_timeout_seconds = 300

[validation_thresholds]
baseline_oof_score = 0.85
```

### 3. Implementacija u kodu
Zameni `verify_ssot_parameters` sa:
```python
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
    environments=True,
    load_dotenv=True,
)

# Pristup parametrima
timeout = settings.cpu_timeout_seconds
```

---

## 📋 Pravila
- Nikada ne čuvaj tajne u `settings.toml`.
- Koristi `.secrets.toml` za osetljive podatke (dodaj u `.gitignore`).
- Koristi `settings.validators` za proveru tipova podataka pri startu.
