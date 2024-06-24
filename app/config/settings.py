"""Use este arquivo para definir variaveis de ambiente usadas em todo o projeto."""

import os
from pathlib import Path

# Id do projeto.
APP_ID = 0

# Diretório do projeto.
APP_DIRECTORY = Path(__file__).resolve().parent.parent

# Diretório do usuário.
USER_DIRECTORY = Path(os.path.expanduser("~"))

# Serviços de armazenamento online.
ONEDRIVE_GERAL = USER_DIRECTORY / "XP Investimentos/Manchester - Mesa RV - 0"
ONEDRIVE_BROKERS = USER_DIRECTORY / "XP Investimentos/Manchester - Mesa RV - Brokers - 0"
ONEDRIVE_BACKOFFICE = USER_DIRECTORY / "XP Investimentos/Manchester - Mesa RV - Backoffice - 0"
