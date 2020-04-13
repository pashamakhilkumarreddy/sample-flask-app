document.addEventListener('DOMContentLoaded', () => {
  const _navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  if (_navbarBurgers.length) {
    _navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {
        const target = el.dataset.target;
        const _target = document.getElementById(target);
        el.classList.toggle('is-active');
        _target.classList.toggle('is-active');
      })
    })
  }
})