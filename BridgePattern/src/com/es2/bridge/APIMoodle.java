package com.es2.bridge;

import java.util.LinkedHashMap;
import java.util.Map;

public class APIMoodle implements APIServiceInterface {

    protected LinkedHashMap<String, String> content;

    public APIMoodle() {
        content = new LinkedHashMap<>();
    }

    @Override
    public String setContent(String contentValue) {
        String id = String.valueOf(content.size() + 1);
        content.put(id, contentValue);
        return id;
    }

    @Override
    public String getContent(String contentId) {
        if ("0".equals(contentId)) {
            StringBuilder sb = new StringBuilder();
            for (Map.Entry<String, String> entry : content.entrySet()) {
                sb.append(entry.getValue());
            }
            return sb.toString();
        } else {
            return content.get(contentId);
        }
    }
}

