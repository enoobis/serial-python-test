import requests

def fetch_balance():
    url = "https://mw-api-test.dengi.kg/api/json/json.php"
    payload = {
        "cmd": "statusPayment",
        "version": 1005,
        "sid": "6554503425",
        "mktime": "1709811507",
        "lang": "ru",
        "data": {
            "invoice_id": "938714053163",
            "order_id": "test02",
            "mark": 1,
        },
        "hash": "9edbedbb813ae4017fa982b623030244",
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    payments = data.get("data", {}).get("payments", [])
    return sum(int(payment["amount"]) for payment in payments)

