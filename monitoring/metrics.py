from prometheus_client import Counter, Histogram

# Count total HTTP requests on items endpoints
ITEMS_REQUEST_COUNT = Counter(
    "items_requests_total",
    "Total number of requests on /items endpoints",
    ["method", "endpoint", "status"],
)

# Measure request latency
ITEMS_REQUEST_LATENCY = Histogram(
    "items_request_latency_seconds",
    "Latency of requests on /items endpoints",
    ["method", "endpoint"],
)
