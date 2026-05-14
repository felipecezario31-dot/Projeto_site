// Menu mobile
const toggleButton = document.querySelector('.navbar-toggle');
const navbarMenu = document.getElementById('navbarMenu');

if (toggleButton && navbarMenu) {
    toggleButton.addEventListener('click', () => {
        navbarMenu.classList.toggle('show');
    });

    // Fechar menu ao clicar em um link
    navbarMenu.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navbarMenu.classList.remove('show');
        });
    });
}

// Cards interativos
const notasGrid = document.querySelector('.notas-grid');

if (notasGrid) {
    const originalContent = notasGrid.innerHTML;

    notasGrid.querySelectorAll('.notas-card').forEach(card => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('.minimize-button')) return;

            notasGrid.innerHTML = `
                <div class="notas-card expanded">
                    <button type="button" class="minimize-button" aria-label="Fechar">×</button>
                    <div class="expanded-body">
                        <h1>EM CONSTRUÇÃO</h1>
                    </div>
                </div>
            `;

            const minimizeBtn = notasGrid.querySelector('.minimize-button');
            if (minimizeBtn) {
                minimizeBtn.addEventListener('click', () => {
                    notasGrid.innerHTML = originalContent;
                    initCards();
                });
            }
        });
    });
}

function initCards() {
    const grid = document.querySelector('.notas-grid');
    if (!grid) return;

    grid.querySelectorAll('.notas-card').forEach(card => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('.minimize-button')) return;

            grid.innerHTML = `
                <div class="notas-card expanded">
                    <button type="button" class="minimize-button" aria-label="Fechar">×</button>
                    <div class="expanded-body">
                        <h1>EM CONSTRUÇÃO</h1>
                    </div>
                </div>
            `;

            const minimizeBtn = grid.querySelector('.minimize-button');
            if (minimizeBtn) {
                minimizeBtn.addEventListener('click', () => {
                    grid.innerHTML = originalContent;
                    initCards();
                });
            }
        });
    });
}
