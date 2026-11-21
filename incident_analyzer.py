from incident_loader import load_incidents



def summarize_incidents(incidents):
    total_incidents = len(incidents)
    critical_incidents = 0
    by_service = {}

    for incident in incidents:
        if incident["severity"] == "critical":
            critical_incidents += 1

        service = incident["service"]
        by_service[service] = by_service.get(service, 0) + 1

    return {
        "total_incidents": total_incidents,
        "critical_incidents": critical_incidents,
        "by_service": by_service
    }

if __name__ == "__main__":
    incidents = load_incidents("data/incidents.json")
    summary = summarize_incidents(incidents)
    print(summary)