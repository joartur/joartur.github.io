document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('share-button').addEventListener('click', function (e) {
        e.preventDefault();

        if (navigator.share) {
            navigator.share({
                title: 'Meu Perfil - Jô Artunes',
                text: 'Confira meus projetos',
                url: 'https://abre.ai/g5q6'
            })
                .then(() => console.log('Compartilhado com sucesso'))
                .catch((error) => console.error('Erro ao compartilhar:', error));
        } else {
            const shareURL = 'https://abre.ai/g5q6';
            window.open(shareURL, '_blank');
        }
    });
});

function selectButton(button) {
    button.classList.add('selected-button');
    button.classList.remove('not-selected-button');
}

function unselectButton(button) {
    button.classList.remove('selected-button');
    button.classList.add('not-selected-button');
}

const menuButtons = document.querySelectorAll('#menu a');

menuButtons.forEach(button => {
    button.addEventListener('click', () => {
        menuButtons.forEach(unselectButton);
        selectButton(button);
    });
});

selectButton(menuButtons[0]);