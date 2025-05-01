export async function addCommuteToDB(formFields) {
  console.log(formFields);
  const start_address = formFields.startingLocation;
  const end_address = formFields.destination;
  const arriveby = formFields.arrivalTime;
  const response = await fetch("http://localhost:5000/addRoute", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // Authorization: "Bearer " + idToken,
    },
    body: JSON.stringify({ start_address, end_address, arrivalby }),
  });

  if (!response.ok) {
    throw new Error("Failed to save address");
  }

  return await response.json();
}
