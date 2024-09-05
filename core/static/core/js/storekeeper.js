document.addEventListener('DOMContentLoaded', (event) => {
    const addCarForm = document.getElementById('add-car-form');
    const orderList = document.getElementById('order-list');
    const inventoryList = document.getElementById('inventory-list');

    // Function to add a new car to the inventory
    addCarForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const carName = document.getElementById('car-name').value;
        const carMake = document.getElementById('car-make').value;
        const carYear = document.getElementById('car-year').value;
        const carPrice = document.getElementById('car-price').value;
        const carImage = document.getElementById('car-image').value;
        const carColors = document.getElementById('car-colors').value;
        const numCar = document.getElementById('num-car').value;

        // Check if the car is already in the inventory
        let carFound = false;
        let carListItems = inventoryList.getElementsByTagName('li');
        for (let i = 0; i < carListItems.length; i++) {
            if (carListItems[i].innerText.startsWith(carName)) {
                carFound = true;
                let currentUnits = parseInt(carListItems[i].innerText.split(': ')[1]);
                carListItems[i].innerText = `${carName}: ${currentUnits + parseInt(numCar)} units`;
                break;
            }
        }

        // If the car is not in the inventory, add it
        if (!carFound) {
            let newInventoryItem = document.createElement('li');
            newInventoryItem.innerText = `${carName}: 1 unit`;
            inventoryList.appendChild(newInventoryItem);
        }

        // Clear the form
        addCarForm.reset();
    });

    // Function to confirm an order
    orderList.addEventListener('click', function (event) {
        if (event.target.classList.contains('confirm-order-button')) {
            let orderItem = event.target.parentElement;
            let orderDetails = orderItem.querySelector('.order-details');
            let carName = orderDetails.innerText.split(': ')[1].split(' ')[0];

            // Check if the car is already in the inventory
            let carFound = false;
            let carListItems = inventoryList.getElementsByTagName('li');
            for (let i = 0; i < carListItems.length; i++) {
                if (carListItems[i].innerText.startsWith(carName)) {
                    carFound = true;
                    let currentUnits = parseInt(carListItems[i].innerText.split(': ')[1]);
                    carListItems[i].innerText = `${carName}: ${currentUnits + 1} units`;
                    break;
                }
            }

            // If the car is not in the inventory, add it
            if (!carFound) {
                let newInventoryItem = document.createElement('li');
                newInventoryItem.innerText = `${carName}: 1 unit`;
                inventoryList.appendChild(newInventoryItem);
            }

            // Remove the confirmed order from the order list
            orderList.removeChild(orderItem);
        }
    });
});
