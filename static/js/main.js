document.addEventListener('DOMContentLoaded', () => {
    createSnow();

    const addButtons = document.querySelectorAll('.btn-add');
    addButtons.forEach(button => {
        button.addEventListener('click', function() {
            const originalText = this.innerText;
            this.innerText = 'Добавлено! 🎄';
            this.style.background = '#10b981';
            setTimeout(() => {
                this.innerText = originalText;
                this.style.background = '';
            }, 2000);
        });
    });

    const phoneInput = document.querySelector('input[name="phone"]');
    if (phoneInput) {
        phoneInput.addEventListener('input', (e) => {
            let val = e.target.value.replace(/\D/g, '');
            if (val.startsWith('7')) val = val.substr(1);
            if (val.length > 10) val = val.substr(0, 10);

            let result = '+7 ';
            if (val.length > 0) result += '(' + val.substr(0, 3);
            if (val.length > 3) result += ') ' + val.substr(3, 3);
            if (val.length > 6) result += '-' + val.substr(6, 2);
            if (val.length > 8) result += '-' + val.substr(8, 2);
            e.target.value = result;
        });
    }

    const cardInput = document.getElementById('input-number') || document.querySelector('input[placeholder="Номер карты"]');
    const dateInput = document.getElementById('input-date') || document.querySelector('input[placeholder="ММ/ГГ"]');
    const cvvInput = document.getElementById('input-cvv') || document.querySelector('input[placeholder="CVV"]');

    const cardDisp = document.getElementById('v-number') || document.querySelector('.card-number');
    const dateDisp = document.getElementById('v-date') || document.querySelector('.card-date div');
    const bankCard = document.getElementById('card-visual') || document.querySelector('.bank-card');

    cardInput?.addEventListener('input', (e) => {
        let val = e.target.value.replace(/\D/g, '');
        if (val.length > 16) val = val.substr(0, 16);
        let formatted = val.match(/.{1,4}/g)?.join(' ') || '';
        e.target.value = formatted;
        if (cardDisp) cardDisp.innerText = formatted || '#### #### #### ####';
    });

    dateInput?.addEventListener('input', (e) => {
        let val = e.target.value.replace(/\D/g, '');
        if (val.length > 4) val = val.substr(0, 4);
        if (val.length >= 2) {
            val = val.slice(0, 2) + '/' + val.slice(2);
        }
        e.target.value = val;
        if (dateDisp) dateDisp.innerText = val || '12/25';
    });

    cvvInput?.addEventListener('focus', () => {
        if (bankCard) bankCard.style.transform = 'rotateY(20deg) scale(1.05)';
    });
    cvvInput?.addEventListener('blur', () => {
        if (bankCard) bankCard.style.transform = 'rotateY(0deg) scale(1)';
    });

    const authForm = document.querySelector('form');
    authForm?.addEventListener('submit', (e) => {
        const submitBtn = authForm.querySelector('.btn-submit');
        if (submitBtn && !submitBtn.classList.contains('btn-add')) {
            submitBtn.innerText = 'Обработка...';
            submitBtn.style.opacity = '0.7';
        }
    });
});

function createSnow() {
    const snowflakeCount = 30;
    const body = document.body;
    for (let i = 0; i < snowflakeCount; i++) {
        const snowflake = document.createElement('div');
        snowflake.className = 'snowflake';
        snowflake.style.left = Math.random() * 100 + 'vw';
        snowflake.style.animationDuration = Math.random() * 3 + 3 + 's';
        snowflake.style.opacity = Math.random();
        snowflake.innerHTML = '❄';
        body.appendChild(snowflake);
    }
}
