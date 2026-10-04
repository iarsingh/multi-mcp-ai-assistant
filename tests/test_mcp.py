from fastapi.testclient import TestClient
from multimcp.main import app

client = TestClient(app)


def test_lists_and_refuses_apply():
    assert "k8s.get_pods" in client.get("/tools").json()["tools"]
    ok = client.post("/call", json={"name": "k8s.get_pods", "arguments": {"q": "status"}}).json()
    assert ok["ok"] is True
    assert ok["applied"] is False
    refused = client.post("/call", json={"name": "github.list_pr", "arguments": {"cmd": "kubectl apply"}}).json()
    assert refused["ok"] is False
