const toggleButton = document.querySelector('.navbar-toggle');
const navbarMenu = document.getElementById('navbarMenu');

if (toggleButton && navbarMenu) {
    toggleButton.addEventListener('click', () => {
        navbarMenu.classList.toggle('show');
    });
}

function initNotasCards() {
    const notasGrid = document.querySelector('.notas-grid');
    if (!notasGrid) {
        return;
    }

    const defaultHtml = notasGrid.dataset.defaultHtml || notasGrid.innerHTML;
    notasGrid.dataset.defaultHtml = defaultHtml;

    function restoreGrid() {
        notasGrid.innerHTML = notasGrid.dataset.defaultHtml;
        initNotasCards();
    }

    notasGrid.querySelectorAll('.notas-card').forEach(card => {
        card.addEventListener('click', () => {
            notasGrid.innerHTML = `
                <div class="notas-card expanded">
                    <div class="expanded-header">
                        <button type="button" class="minimize-button">×</button>
                    </div>
                    <div class="expanded-body">
                        <h1>Em construção</h1>
                    </div>
                </div>
            `;
            const minimizeButton = notasGrid.querySelector('.minimize-button');
            if (minimizeButton) {
                minimizeButton.addEventListener('click', restoreGrid);
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', initNotasCards);
