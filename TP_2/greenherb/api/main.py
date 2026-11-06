from fastapi import FastAPI

from api.routes import (
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


api = FastAPI(
    title="GREENHERB API",
    description="Sprint 1 API scaffold for GREENHERB.",
    version="1.0.0",
)

api.include_router(auth_routes.router)
api.include_router(users_routes.router)
api.include_router(herbs_routes.router)
api.include_router(plans_routes.router)
api.include_router(batches_routes.router)
api.include_router(tasks_routes.router)
api.include_router(measurements_routes.router)
api.include_router(alerts_routes.router)
api.include_router(automation_routes.router)
api.include_router(reports_routes.router)
api.include_router(audit_routes.router)


@api.get("/", tags=["health"])
def health_check():
    return {"status": "ok", "service": "GREENHERB API"}
