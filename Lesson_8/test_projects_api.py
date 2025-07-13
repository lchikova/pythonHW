import pytest

def valid_project_data():
    return {"title": "Test Project"}

def invalid_project_data():
    return {}

@pytest.mark.parametrize("data,expected_status", [
    (valid_project_data(), 201),
])
def test_create_project_positive(api, data, expected_status):
    resp = api.create_project(data)
    print("[CREATE PROJECT POSITIVE]", resp.status_code, resp.json())
    assert resp.status_code == expected_status
    proj_id = resp.json()["id"]
    get_resp = api.get_project(proj_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == data["title"]

@pytest.mark.parametrize("data,expected_status", [
    (invalid_project_data(), 400),
])
def test_create_project_negative(api, data, expected_status):
    resp = api.create_project(data)
    print("[CREATE PROJECT NEGATIVE]", resp.status_code, resp.json())
    assert resp.status_code == expected_status

def test_get_project_positive(api):
    data = valid_project_data()
    resp = api.create_project(data)
    print("[CREATE FOR GET PROJECT]", resp.status_code, resp.json())
    proj_id = resp.json()["id"]
    get_resp = api.get_project(proj_id)
    print("[GET PROJECT POSITIVE]", get_resp.status_code, get_resp.json())
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == proj_id
    assert get_resp.json()["title"] == data["title"]

def test_get_project_negative(api):
    resp = api.get_project("nonexistent_id")
    print("[GET PROJECT NEGATIVE]", resp.status_code, resp.json())
    assert resp.status_code == 404

def test_update_project_positive(api):
    data = valid_project_data()
    resp = api.create_project(data)
    print("[CREATE FOR UPDATE PROJECT]", resp.status_code, resp.json())
    proj_id = resp.json()["id"]
    new_title = "Updated title"
    update_resp = api.update_project(proj_id, {"title": new_title})
    print("[UPDATE PROJECT POSITIVE]", update_resp.status_code, update_resp.json())
    assert update_resp.status_code == 200
    get_resp = api.get_project(proj_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_title

def test_update_project_negative(api):
    resp = api.update_project("nonexistent_id", {"title": "Any"})
    print("[UPDATE PROJECT NEGATIVE - WRONG ID]", resp.status_code, resp.json())
    assert resp.status_code == 404
    data = valid_project_data()
    create_resp = api.create_project(data)
    proj_id = create_resp.json()["id"]
    bad_resp = api.update_project(proj_id, {})
    print("[UPDATE PROJECT NEGATIVE - BAD DATA]", bad_resp.status_code, bad_resp.json())
    assert bad_resp.status_code == 200
    get_resp = api.get_project(proj_id)
    assert get_resp.json()["title"] == data["title"]
