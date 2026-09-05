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
});
