document.getElementById('importOrderForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        email: document.getElementById('email').value,
        carModel: document.getElementById('carModel').value,
        specifications: document.getElementById('specifications').value,
        color: document.getElementById('color').value,
        year: document.getElementById('year').value,
        orderDate: document.getElementById('orderDate').value,
        trackingNumber: `TN${Math.floor(Math.random() * 1000000)}`,
        carrier: 'DHL',
        departureDate: new Date().toISOString().split('T')[0],
        arrivalDate: new Date(new Date().getTime() + 7*24*60*60*1000).toISOString().split('T')[0],
        currentLocation: 'Warehouse',
        status: 'In Transit'
    };

    // Trigger a custom event with the formData as detail
    document.dispatchEvent(new CustomEvent('newOrder', { detail: formData }));

    alert('Import order placed successfully!');

    // Redirect to shipment page
    window.location.href = 'shipments.html';
});
