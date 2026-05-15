from fastapi import FastAPI

from app.routes import (
    alerts_routes,
    audit_routes,
    auth_routes,
    automation_routes,
    batches_routes,
    herbs_routes,
    measurements_routes,
    plans_routes,
    reports_routes,
    tasks_routes,
    users_routes,
)


app = FastAPI(
    title="GREENHERB API",
    description="Sprint 1 API scaffold for GREENHERB.",
    version="1.0.0",
)

app.include_router(auth_routes.router)
app.include_router(users_routes.router)
app.include_router(herbs_routes.router)
app.include_router(plans_routes.router)
app.include_router(batches_routes.router)
app.include_router(tasks_routes.router)
app.include_router(measurements_routes.router)
app.include_router(alerts_routes.router)
app.include_router(automation_routes.router)
app.include_router(reports_routes.router)
app.include_router(audit_routes.router)


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "service": "GREENHERB API"}
