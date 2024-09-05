document.addEventListener('DOMContentLoaded', function() {
    const shipmentInfo = document.getElementById('shipmentInfo');
    const shipmentList = document.getElementById('shipmentList');

    function displayShipmentDetails(shipment) {
        // Display specific shipment details in Shipment Details section
        shipmentInfo.innerHTML = `
            <p><strong>Order:</strong> <span>${shipment.order}</span></p>
            <p><strong>Tracking Number:</strong> <span>${shipment.trackingNumber}</span></p>
            <p><strong>Carrier:</strong> <span>${shipment.carrier}</span></p>
            <p><strong>Departure Date:</strong> <span>${shipment.departureDate}</span></p>
            <p><strong>Arrival Date:</strong> <span>${shipment.arrivalDate}</span></p>
            <p><strong>Current Location:</strong> <span>${shipment.currentLocation}</span></p>
            <p><strong>Status:</strong> <span>${shipment.status}</span></p>
        `;
    }

    function displayAllShipments(shipments) {
        // Clear existing content in shipmentList
        shipmentList.innerHTML = '';

        // Display all shipments in All Shipments section
        shipments.forEach(function(shipment) {
            const shipmentItem = document.createElement('div');
            shipmentItem.classList.add('shipment-item');
            shipmentItem.innerHTML = `
                <p><strong>Order:</strong> <span>${shipment.order}</span></p>
                <p><strong>Tracking Number:</strong> <span>${shipment.trackingNumber}</span></p>
                <p><strong>Carrier:</strong> <span>${shipment.carrier}</span></p>
                <p><strong>Departure Date:</strong> <span>${shipment.departureDate}</span></p>
                <p><strong>Arrival Date:</strong> <span>${shipment.arrivalDate}</span></p>
                <p><strong>Current Location:</strong> <span>${shipment.currentLocation}</span></p>
                <p><strong>Status:</strong> <span>${shipment.status}</span></p>
            `;
            shipmentList.appendChild(shipmentItem);
        });
    }

    // Listen for new order placed from importOrder.html
    document.addEventListener('newOrder', function(event) {
        const newOrder = event.detail;

        // Display the newly placed order in Shipment Details
        displayShipmentDetails(newOrder);

        // Optionally, handle storing the new order in session storage or elsewhere
        let shipments = JSON.parse(sessionStorage.getItem('shipments')) || [];
        shipments.push(newOrder);
        sessionStorage.setItem('shipments', JSON.stringify(shipments));

        // Display all shipments including the new order in All Shipments
        displayAllShipments(shipments);
    });

    // Retrieve and display any existing shipments from session storage on page load
    let shipments = JSON.parse(sessionStorage.getItem('shipments')) || [];
    displayAllShipments(shipments);
});
