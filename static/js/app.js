/* Theme Name:  Kasy- Responsive Landing page template
  File Description: Main JS file of the template
*/



//  Window scroll sticky class add
function windowScroll() {
  const navbar = document.getElementById("navbar");
  if (
      document.body.scrollTop >= 50 ||
      document.documentElement.scrollTop >= 50
  ) {
      navbar.classList.add("nav-sticky");
  } else {
      navbar.classList.remove("nav-sticky");
  }
}

window.addEventListener('scroll', (ev) => {
  ev.preventDefault();
  windowScroll();
})

// Swiper slider

var swiper6 = new Swiper(".mySwiper6", {
  grabCursor: true,
  effect: "creative",
  creativeEffect: {
    prev: {
      shadow: true,
      origin: "left center",
      translate: ["-5%", 0, -200],
      rotate: [0, 100, 0],
    },
    next: {
      origin: "right center",
      translate: ["5%", 0, -200],
      rotate: [0, -100, 0],
    },
    autoplay: {
      delay: 100,
      disableOnInteraction: false,
    },
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});


//  pricing

function check() {
  var checkBox = document.getElementById("checbox");
  var text1 = document.getElementsByClassName("text1");
  var text2 = document.getElementsByClassName("text2");

  for (var i = 0; i < text1.length; i++) {
      if (checkBox.checked == true) {
          text1[i].style.display = "block";
          text2[i].style.display = "none";
      } else if (checkBox.checked == false) {
          text1[i].style.display = "none";
          text2[i].style.display = "block";
      }
  }
}
check();



//
/********************* scroll top js ************************/
//

var mybutton = document.getElementById("back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 100 ||
    document.documentElement.scrollTop > 100
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


// 
// Typed Text animation (animation)
// 

try {
  var TxtType = function (el, toRotate, period) {
      this.toRotate = toRotate;
      this.el = el;
      this.loopNum = 0;
      this.period = parseInt(period, 10) || 2000;
      this.txt = '';
      this.tick();
      this.isDeleting = false;
  };
  TxtType.prototype.tick = function () {
      var i = this.loopNum % this.toRotate.length;
      var fullTxt = this.toRotate[i];
      if (this.isDeleting) {
          this.txt = fullTxt.substring(0, this.txt.length - 1);
      } else {
          this.txt = fullTxt.substring(0, this.txt.length + 1);
      }
      this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';
      var that = this;
      var delta = 200 - Math.random() * 100;
      if (this.isDeleting) { delta /= 2; }
      if (!this.isDeleting && this.txt === fullTxt) {
          delta = this.period;
          this.isDeleting = true;
      } else if (this.isDeleting && this.txt === '') {
          this.isDeleting = false;
          this.loopNum++;
          delta = 500;
      }
      setTimeout(function () {
          that.tick();
      }, delta);
  };
  function typewrite() {
      if (toRotate === 'undefined') {
          changeText()
      }
      else
          var elements = document.getElementsByClassName('typewrite');
      for (var i = 0; i < elements.length; i++) {
          var toRotate = elements[i].getAttribute('data-type');
          var period = elements[i].getAttribute('data-period');
          if (toRotate) {
              new TxtType(elements[i], JSON.parse(toRotate), period);
          }
      }
      // INJECT CSS
      var css = document.createElement("style");
      css.type = "text/css";
      css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid transparent}";
      document.body.appendChild(css);
  };
  window.onload(typewrite());
} catch(err) {
}


// home3 swiper slider 

var swiper = new Swiper(".mySwiper", {
  spaceBetween: 0,
  slidesPerView: 6,
  freeMode: true,
  watchSlidesProgress: true,
});
var swiper2 = new Swiper(".mySwiper2", {
  spaceBetween: 1,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  thumbs: {
    swiper: swiper,
  },
});

// Animaten js

 AOS.init();
