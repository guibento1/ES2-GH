package com.es2.bridge;

import java.util.HashMap;

public class APIRequest {

    protected HashMap<String, APIServiceInterface> services;
    protected int nextServiceId;

    public APIRequest() {
        services = new HashMap<>();
        nextServiceId = 1;
    }

    public String addService(APIServiceInterface service) {
        String id = String.valueOf(nextServiceId);
        services.put(id, service);
        nextServiceId++;
        return id;
    }

    public String getContent(String serviceId, String contentId)
            throws ServiceNotFoundException {
        APIServiceInterface service = services.get(serviceId);
        if (service == null) {
            throw new ServiceNotFoundException();
        }
        return service.getContent(contentId);
    }

    public String setContent(String serviceId, String content)
            throws ServiceNotFoundException {
        APIServiceInterface service = services.get(serviceId);
        if (service == null) {
            throw new ServiceNotFoundException();
        }
        return service.setContent(content);
    }
}
