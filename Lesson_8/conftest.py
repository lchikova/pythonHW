import os
import pytest
from projects_api import ProjectsApi

@pytest.fixture(scope="session")
def api():
    base_url = os.environ.get('YOUGILE_API_URL', 'https://ru.yougile.com')
    token = os.environ.get('YOUGILE_TOKEN')
    if not token:
        raise RuntimeError("Требуется указать токен в переменной окружения YOUGILE_TOKEN")
    return ProjectsApi(base_url, token)
