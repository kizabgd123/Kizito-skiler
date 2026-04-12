# 🛠️ Makefile za Projekat Usisivac

.PHONY: install setup verify run test clean skill-check

# 1. Instalacija svih zavisnosti (Gem-ova)
install: setup
setup:
	@echo "📦 Instalacija zavisnosti..."
	pip install dynaconf loguru cerberus pytest

# 2. Verifikacija SSOT parametara (Dynaconf + Cerberus + Loguru)
verify:
	@echo "✅ Verifikacija SSOT parametara..."
	python3 verify_ssot.py

# 3. Pokretanje glavne aplikacije
run: verify
	@echo "🚀 Pokretanje aplikacije..."
	python3 main.py

# 4. Pokretanje testova
test:
	@echo "🧪 Pokretanje testova..."
	pytest

# 5. Provera usklađenosti sa skillovima
skill-check:
	@echo "🔍 Pokretanje Skill-Checkera..."
	python3 skill_checker.py

# 6. Čišćenje privremenih fajlova
clean:
	@echo "🧹 Čišćenje..."
	rm -rf __pycache__ .pytest_cache WORK_LOG.json
