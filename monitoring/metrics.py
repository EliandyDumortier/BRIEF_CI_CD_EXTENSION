from prometheus_client import Counter

# Counts how many times endpoints are called
items_requests_total = Counter(
    "items_requests_total",
    "Total number of requests on items endpoints",
    ["method", "endpoint"],
)

# Counts created items
items_created_total = Counter(
    "items_created_total",
    "Total number of items created",
)

# Counts deleted items
items_deleted_total = Counter(
    "items_deleted_total",
    "Total number of items deleted",
)
