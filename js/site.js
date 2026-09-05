document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
  }

  // Duplicate ticker content for a seamless loop.
  // The keyframe travels to -50%, so the track must end up as exactly two
  // copies of the same run, and one run must be at least a viewport wide.
  var track = document.querySelector('.ticker-track');
  if (track) {
    var base = track.innerHTML;
    var run = base;
    track.innerHTML = run;
    for (var i = 0; i < 8 && track.scrollWidth < window.innerWidth; i++) {
      run += base;
      track.innerHTML = run;
    }
    track.innerHTML = run + run;
  }

  // Accordion (FAQ-style)
  document.querySelectorAll('.accordion-trigger').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.accordion-item');
      var panel = item.querySelector('.accordion-panel');
      var isOpen = item.classList.contains('open');

      document.querySelectorAll('.accordion-item.open').forEach(function (openItem) {
        if (openItem !== item) {
          openItem.classList.remove('open');
          openItem.querySelector('.accordion-panel').style.maxHeight = null;
        }
      });

      if (isOpen) {
        item.classList.remove('open');
        panel.style.maxHeight = null;
      } else {
        item.classList.add('open');
        panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  });

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
