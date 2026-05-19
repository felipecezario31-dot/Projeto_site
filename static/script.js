// Menu mobile
const toggleButton = document.querySelector('.navbar-toggle');
const navbarMenu = document.getElementById('navbarMenu');

if (toggleButton && navbarMenu) {
    toggleButton.addEventListener('click', () => {
        navbarMenu.classList.toggle('show');
    });

    navbarMenu.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navbarMenu.classList.remove('show');
        });
    });
}

// Cards interativos
const notasGrid = document.querySelector('.notas-grid');

if (notasGrid) {
    // Guarda os cards originais como elementos, não como HTML
    const cardsOriginais = Array.from(notasGrid.querySelectorAll('.notas-card'));

    // Cria o card expandido uma vez só
    const cardExpandido = document.createElement('div');
    cardExpandido.classList.add('notas-card', 'expanded');
    cardExpandido.innerHTML = `
        <button type="button" class="minimize-button" aria-label="Fechar">×</button>
        <div class="expanded-body">
            <h1>EM CONSTRUÇÃO</h1>
        </div>
    `;

    // Botão de fechar — restaura os cards originais
    cardExpandido.querySelector('.minimize-button').addEventListener('click', () => {
        notasGrid.innerHTML = '';
        cardsOriginais.forEach(card => notasGrid.appendChild(card));
    });

    // Clique em cada card — substitui pelo expandido
    cardsOriginais.forEach(card => {
        card.addEventListener('click', () => {
            notasGrid.innerHTML = '';
            notasGrid.appendChild(cardExpandido);
        });
    });
}
