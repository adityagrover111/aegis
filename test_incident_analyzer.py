from incident_analyzer import summarize_incidents

def test_empty_incidents():
    result=summarize_incidents([])
    assert result["total_incidents"] == 0
    assert result["critical_incidents"] == 0
    assert result["by_service"] == {}

def test_multiple_incidents():
    incidents = [
        {"service": "auth", "severity": "critical"},
        {"service": "auth", "severity": "high"},
        {"service": "payments", "severity": "critical"}
    ]

    result=summarize_incidents(incidents)
    assert result["total_incidents"]==3
    assert result["critical_incidents"]==2
    assert result["by_service"]=={"auth": 2, "payments": 1}