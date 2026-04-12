# 🚀 Kizito-skiler: Advanced Automation Framework

Dobrodošli u **Kizito-skiler**, napredni operativni okvir za automatizaciju i upravljanje skillovima. Ovaj projekat transformiše pasivnu dokumentaciju u **aktivni, samoodrživi sistem** koristeći najbolje prakse iz open-source zajednice (GitHub Gems).

---

## 💎 Implementirani GitHub Gemovi

Ovaj projekat koristi tri ključna stuba za robusnost i skalabilnost:

| Gem | Svrha | Prednost |
|:---|:---|:---|
| **[Dynaconf](https://github.com/dynaconf/dynaconf)** | Config Management | Slojevito učitavanje (default -> settings -> env) bez hardkodovanja. |
| **[Loguru](https://github.com/Delgan/loguru)** | Structured Logging | Automatsko generisanje mašinski čitljivih JSON logova (`WORK_LOG.json`). |
| **[Cerberus](https://github.com/pyeve/cerberus)** | Data Validation | Deklarativna provera svih parametara pre izvršenja koda. |

---

## 🛠️ Automatizacija (Makefile)

Sistemom se upravlja isključivo kroz `Makefile`, što eliminiše greške i ubrzava rad:

- `make setup`: Instalira sve potrebne biblioteke i Gemove.
- `make verify`: Pokreće SSOT (Single Source of Truth) verifikaciju parametara.
- `make skill-check`: **Aktivna kontrola** – proverava da li je kôd usklađen sa definisanim skillovima.
- `make run`: Sigurno pokretanje aplikacije (automatski prvo radi verifikaciju).
- `make clean`: Čisti privremene fajlove i logove.

---

## 🔍 Skill-Checker Sistem

U srcu projekta je `skill_checker.py`, alat koji osigurava da se standardi ne krše:
- Proverava prisustvo `settings.toml` (Config Management).
- Verifikuje implementaciju `Loguru` (Structured Logging).
- Potvrđuje postojanje `Cerberus` šema (Data Validation).

---

## 📂 Struktura Projekta

```text
.
├── .agents/skills/      # Definicije skillova i workflow-a
├── settings.toml        # Centralna konfiguracija (Dynaconf)
├── verify_ssot.py       # Refaktorisana logika sa Gemovima
├── skill_checker.py     # Automatizovani kontrolor kvaliteta
├── Makefile             # Komandni centar projekta
└── README.md            # Ovo uputstvo
```

---

## 🚀 Kako početi?

1. **Klonirajte repozitorijum**:
   ```bash
   git clone <url-repozitorijuma>
   cd Kizito-skiler
   ```

2. **Postavite okruženje**:
   ```bash
   make setup
   ```

3. **Proverite usklađenost**:
   ```bash
   make skill-check
   ```

4. **Pokrenite verifikaciju**:
   ```bash
   make verify
   ```

---

> 💡 **Filozofija:** "Solve the problem first, skill-ify later." Ovaj projekat je živi dokaz te filozofije u akciji.
