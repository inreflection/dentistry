window.addEventListener('load', function() {
  var boxes = document.querySelectorAll('.news-box');
  var maxHeight = 0;

  boxes.forEach(function(box) {
    var boxHeight = box.offsetHeight;
    if (boxHeight > maxHeight) {
      maxHeight = boxHeight;
    }
  });

  boxes.forEach(function(box) {
    box.style.height = maxHeight + 'px';
  });
});