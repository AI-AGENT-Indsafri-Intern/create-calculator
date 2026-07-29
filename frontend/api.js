// Change BASE_URL or adjust how endpoints are passed
const BASE_URL = "http://127.0.0.1:8000/api";

async function callApi(endpoint, method = "GET", data = null) {
    const body_object = {
        method,
        headers: {
            "Content-Type": "application/json"
        }
    };

    if (data) {
        body_object.body = JSON.stringify(data);
    }

    const response = await fetch(BASE_URL + endpoint, body_object);
    const result = await response.json();

    if (!response.ok) {
        throw new Error(result.detail || "Something went wrong.");
    }

    return result;
}


async function addNumbers() {

    const num1 = Number(document.getElementById("number1").value);
    const num2 = Number(document.getElementById("number2").value);

    const response = await fetch(
        `http://127.0.0.1:8000/add?num1=${num1}&num2=${num2}`
    );

    const data = await response.json();

    document.getElementById("result").innerText = data.result;
}
