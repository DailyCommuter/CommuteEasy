export async function addCommuteToDB(formFields) {
  
  const start_address = formFields.startingLocation;
  const end_address = formFields.destination;
  const arriveby = formFields.arrivalTime;
  // console.log(formFields.startingLocation)

  const response = await fetch("http://localhost:5000/addRoute", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // Authorization: "Bearer " + idToken,
    },
    body: JSON.stringify({ start_address, end_address, arriveby }),
  });
  console.log(response)

  if (!response.ok) {
    throw new Error("Failed to save address");
  }
  
  const result = await response.json();
  const page = "http://localhost:5000/"+result.redirect_url
  window.location.href = page;  // Force browser redirect
  
}