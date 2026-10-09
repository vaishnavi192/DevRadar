const API_URL = "http://127.0.0.1:8000";

export async function analyzeProduct(product) {
  const response = await fetch(`${API_URL}/api/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(product),
  });

  if (!response.ok) {
    throw new Error("Analysis request failed");
  }

  return response.json();
}