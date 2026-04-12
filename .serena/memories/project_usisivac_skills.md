# Project Usisivac Skills and Automation

## Tech Stack
- Python 3.11
- Dynaconf (Config Management)
- Loguru (Structured Logging)
- Cerberus (Data Validation)

## Automation Commands
- `make setup`: Install dependencies
- `make verify`: Run SSOT verification with Dynaconf/Cerberus/Loguru
- `make skill-check`: Run automated skill compliance check
- `make run`: Run application after verification

## Key Files
- `settings.toml`: Central configuration
- `verify_ssot.py`: Refactored core logic using GitHub Gems
- `skill_checker.py`: Automated compliance script