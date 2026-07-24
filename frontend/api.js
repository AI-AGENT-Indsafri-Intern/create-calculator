const BASE_URL = "http://127.0.0.1:8000/api";

async function callApi(endpoint, method = "GET", data = null) {

    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json"
        }
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(BASE_URL + endpoint, options);

    const result = await response.json();

    if (!response.ok) {
        throw new Error(result.detail || "Something went wrong.");
    }

    return result;
}