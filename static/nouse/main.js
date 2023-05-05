console.log('Chill box');

const subscriptionForm = document.querySelector('.subscription-form');

function foodSetValidation(event) {
    const checkedFoodSet = document.querySelectorAll('input[name="food_set"]:checked');
    if (checkedFoodSet.length === 0) {
        event.preventDefault();
        alert('กรุณาเลือกอย่างน้อย 1 รายการ');
    }
}

if (!!subscriptionForm) {
    subscriptionForm.addEventListener('submit', foodSetValidation);
}