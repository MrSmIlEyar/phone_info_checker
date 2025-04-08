document.addEventListener('DOMContentLoaded', () => {
    const phoneInput = document.getElementById('phoneInput');
    const checkButton = document.getElementById('checkButton');
    const resultContainer = document.getElementById('resultContainer');

    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        let formatted = '+7';

        if (value.length > 1) {
            value = value.substring(1);
            formatted += ' (' + value.substring(0, 3);
            if (value.length > 3) formatted += ') ' + value.substring(3, 6);
            if (value.length > 6) formatted += '-' + value.substring(6, 8);
            if (value.length > 8) formatted += '-' + value.substring(8, 10);
        }

        e.target.value = formatted;
    });

    checkButton.addEventListener('click', async () => {
        const cleanNumber = phoneInput.value.replace(/\D/g, '');

        if (cleanNumber.length !== 11 || !cleanNumber.startsWith('7')) {
            showError('Введите корректный номер телефона');
            return;
        }

        try {
            const response = await fetch(`/api/check-phone/?phone=${cleanNumber}`);
            const data = await response.json();

            if (data.error) {
                showError(data.error);
            } else {
                showResult(data);
            }
        } catch (error) {
            showError('Ошибка соединения с сервером');
        }
    });

    function showResult(data) {
        resultContainer.style.display = 'block';
        document.getElementById('resultPhone').textContent = data.phone;
        document.getElementById('resultOperator').textContent = data.operator;
        document.getElementById('resultRegion').textContent = data.region.split('|').join(' ');
        document.getElementById('resultTerritory').textContent = data.territory.split('|').join(' ');
        document.getElementById('resultInn').textContent = data.inn;
    }

    function showError(message) {
        const errorElement = document.getElementById('errorMessage');
        errorElement.textContent = message;
        resultContainer.style.display = 'none';
        setTimeout(() => errorElement.textContent = '', 3000);
    }
});