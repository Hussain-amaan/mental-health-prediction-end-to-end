const API_BASE = "http://127.0.0.1:8000";

/**
 * Send prediction request to FastAPI
 * @param {Object} payload
 * @returns {Promise<Object>}
 */
async function predictMentalHealth(payload) {

    const response = await fetch(`${API_BASE}/predict`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {

        const error = await response.json().catch(() => ({}));

        throw new Error(
            error.detail || `HTTP ${response.status}`
        );
    }

    return await response.json();
}