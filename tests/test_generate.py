import pytest
@pytest.mark.skip('requires downstream mocks')
def test_generate(client):
    r = client.post('/api/v1/generate', json={'text':'Hi'})
    assert r.status_code == 200
