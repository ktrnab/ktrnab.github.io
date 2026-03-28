// ── Active nav highlight on scroll ──
const sections = document.querySelectorAll('section[id], .hero[id]');
const navLinks = document.querySelectorAll('nav a');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute('id');
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
      });
    }
  });
}, { threshold: 0.3 });

sections.forEach(s => observer.observe(s));

// ── Scroll-in fade animations ──
const fadeEls = document.querySelectorAll('.timeline-item, .card, .contact-card');

const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      entry.target.style.animationDelay = `${i * 60}ms`;
      entry.target.classList.add('visible');
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

fadeEls.forEach(el => {
  el.classList.add('fade-in');
  fadeObserver.observe(el);
});

// ── Scroll-to-top button ──
const scrollBtn = document.createElement('button');
scrollBtn.id = 'scroll-top';
scrollBtn.setAttribute('aria-label', 'Scroll to top');
scrollBtn.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 15l-6-6-6 6"/></svg>`;
document.body.appendChild(scrollBtn);

window.addEventListener('scroll', () => {
  scrollBtn.classList.toggle('show', window.scrollY > 500);
});

scrollBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
