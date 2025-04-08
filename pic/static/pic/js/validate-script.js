document.addEventListener('DOMContentLoaded', function() {
    const phoneInput = document.getElementById('phoneInput');
    const errorMessage = document.getElementById('errorMessage');
    const form = document.getElementById('phoneForm');

    // Маска ввода
    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');

        if (value.startsWith('7') || value.startsWith('8')) {
            value = value.substring(1);
        }

        let formatted = '+7 (';
        if (value.length > 0) formatted += value.substring(0, 3);
        if (value.length > 3) formatted += ') ' + value.substring(3, 6);
        if (value.length > 6) formatted += '-' + value.substring(6, 8);
        if (value.length > 8) formatted += '-' + value.substring(8, 10);

        e.target.value = formatted;
    });

    // Валидация перед отправкой
    form.addEventListener('submit', function(e) {
        const cleanNumber = phoneInput.value.replace(/\D/g, '');

        if (cleanNumber.length !== 11 || !cleanNumber.startsWith('7')) {
            e.preventDefault();
            errorMessage.textContent = 'Введите корректный номер телефона (11 цифр, начинается с 7)';
            phoneInput.classList.add('error');
        } else {
            errorMessage.textContent = '';
            phoneInput.classList.remove('error');
        }
    });
});