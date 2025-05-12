const banners = document.querySelectorAll('.hero > div:first-child > div');
let posX = 0;
let baseSpeed = 0.25;
let scrollSpeed = 0;
let lastScrollTop = window.scrollY;

function animateBackground() {
  scrollSpeed *= 0.9;
  const totalSpeed = baseSpeed + scrollSpeed;
  banners.forEach((banner, key) => {
    const dir = key % 2 === 0 ? 1 : -1;
    const offset = posX * dir;
    banner.style.backgroundPosition = `${offset}px 0`;
  });
  posX -= totalSpeed;
  requestAnimationFrame(animateBackground);
}

window.addEventListener('scroll', () => {
  const currentScroll = window.scrollY;
  const delta = currentScroll - lastScrollTop;
  scrollSpeed = Math.min(Math.max(delta * 0.25, -20), 20);
  lastScrollTop = currentScroll;
});

animateBackground();