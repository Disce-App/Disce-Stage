document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    var setNavOpen = function (open) {
      links.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', String(open));
    };
    toggle.addEventListener('click', function () {
      setNavOpen(!links.classList.contains('open'));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('open')) {
        setNavOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (links.classList.contains('open') &&
          !links.contains(e.target) && !toggle.contains(e.target)) {
        setNavOpen(false);
      }
    });
  }

  // Duplicate ticker content for a seamless loop.
  // The keyframe travels to -50%, so the track must end up as exactly two
  // copies of the same run, and one run must be at least a viewport wide.
  //
  // The track already holds one run and every extra run is an identical copy,
  // so the track width grows linearly: width(n) = n * (runWidth + gap) - gap.
  // One width read plus the flex gap therefore describe every candidate run,
  // so all reads happen before the single write. The previous version wrote
  // innerHTML and then read scrollWidth on every iteration, forcing up to
  // eight synchronous layouts (layout thrashing).
  var track = document.querySelector('.ticker-track');
  if (track) {
    var base = track.innerHTML;
    var gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    var runWidth = track.scrollWidth;
    var viewport = window.innerWidth;
    var copies = 1;
    while (copies < 9 && copies * (runWidth + gap) - gap < viewport) {
      copies++;
    }
    var run = base;
    for (var i = 1; i < copies; i++) {
      run += base;
    }
    track.innerHTML = run + run;
  }

  // Ticker pause/resume (A11Y-06, WCAG 2.2.2). Wired only when the page
  // renders both the ticker and its control; reduced-motion hides the control.
  var tickerSection = document.querySelector('.ticker-section');
  var tickerToggle = document.querySelector('.ticker-toggle');
  if (tickerSection && tickerToggle) {
    tickerToggle.addEventListener('click', function () {
      var paused = !tickerSection.classList.contains('is-paused');
      tickerSection.classList.toggle('is-paused', paused);
      tickerToggle.setAttribute('aria-pressed', String(paused));
    });
  }

  // Language. German is the default; a stored choice wins over it.
  // No browser sniffing: a first-time visitor always gets German.
  var LANG_KEY = 'disce-lang';
  function readLang() {
    try { return localStorage.getItem(LANG_KEY) === 'en' ? 'en' : 'de'; }
    catch (e) { return 'de'; }
  }
  function applyLang(lang) {
    document.documentElement.classList.remove('pre-en');
    document.body.classList.toggle('lang-en', lang === 'en');
    document.body.classList.toggle('lang-de', lang === 'de');
    document.documentElement.setAttribute('lang', lang);
    document.querySelectorAll('.lang-switch button').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.setLang === lang));
    });
    var t = document.querySelector('title[data-title-' + lang + ']');
    if (t) document.title = t.getAttribute('data-title-' + lang);
  }
  applyLang(readLang());
  document.querySelectorAll('.lang-switch button').forEach(function (b) {
    b.addEventListener('click', function () {
      var lang = b.dataset.setLang;
      try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
      applyLang(lang);
    });
  });
});
