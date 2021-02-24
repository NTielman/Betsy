// sign in modal
const signInButton = document.querySelector('#sign_in');
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');

signInButton.addEventListener('click', () => {
    modal.classList.add('is-active');
});
modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active');
});