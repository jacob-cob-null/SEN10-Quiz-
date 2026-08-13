"""
Gotham Emergency Dispatch — Sprint 1 Vertical Prototype
Sprint Goal: Citizen submits ONE emergency report type (Fire/Police/Medical)
w/ location -> appears on dispatcher list in real-time (polling).
"""
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory store (Sprint 1 — no DB, that's backlog item for Sprint 2)
REPORTS = []

UNITS = {
    "Fire": ["Engine 7", "Engine 12", "Ladder 3"],
    "Police": ["Unit 22", "Unit 45", "GCPD Patrol 9"],
    "Medical": ["Ambulance 4", "Ambulance 11"],
}

@app.route("/")
def citizen_portal():
    return render_template("citizen.html")

@app.route("/dispatcher")
def dispatcher_view():
    return render_template("dispatcher.html")

@app.route("/api/reports", methods=["POST"])
def submit_report():
    data = request.get_json(force=True)
    emergency_type = data.get("type")
    location = data.get("location")
    description = data.get("description", "")

    if emergency_type not in UNITS or not location:
        return jsonify({"error": "type and location required"}), 400

    report = {
        "id": str(uuid.uuid4())[:8],
        "type": emergency_type,
        "location": location,
        "description": description,
        "status": "UNASSIGNED",
        "assigned_unit": None,
        "timestamp": datetime.utcnow().strftime("%H:%M:%S"),
    }
    REPORTS.append(report)
    return jsonify(report), 201

@app.route("/api/reports", methods=["GET"])
def list_reports():
    return jsonify(list(reversed(REPORTS)))

@app.route("/api/reports/<report_id>/assign", methods=["POST"])
def assign_unit(report_id):
    data = request.get_json(force=True)
    unit = data.get("unit")
    for r in REPORTS:
        if r["id"] == report_id:
            r["assigned_unit"] = unit
            r["status"] = "ASSIGNED"
            return jsonify(r)
    return jsonify({"error": "not found"}), 404

@app.route("/api/units/<emergency_type>")
def get_units(emergency_type):
    return jsonify(UNITS.get(emergency_type, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
