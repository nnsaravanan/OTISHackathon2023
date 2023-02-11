import http.client, urllib.request, urllib.parse, urllib.error, base64
import os


def get_otis_api_key() -> str:
    """ Returns the OTIS API key from the OTIS_API_KEY environment github.
    """
    key = os.environ.get("OTIS_API_KEY")
    if key is None:
        raise RuntimeError("OTIS_API_KEY environment variable is not set")
    return key


def elevator_status(unit_number: str, country_code: str, customer_id: str, contract_no: str) -> bytes:
    headers = {
        # Request headers
        f"Ocp-Apim-Subscription-Key": get_otis_api_key(),
    }

    params = urllib.parse.urlencode({
        "unit_number": unit_number,
        "country_code": country_code,
        "customer_id": customer_id,
        "contract_no": contract_no,
    })

    try:
        conn = http.client.HTTPSConnection('developer-portal-api-stage.otiselevator.com')
        conn.request("GET", f"/elevatorstatus/api/elevators/{unit_number}/{country_code}/v1/elevatorstatus/?customer_id={customer_id}&contract_no={contract_no}", "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data

