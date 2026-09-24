// KPSS ORTAOGRETIM - ANA JAVASCRIPT

(function() {
    'use strict';

    // ===== NAVIGATION =====
    var navbar = document.getElementById('navbar');
    var navToggle = document.getElementById('navToggle');
    var navMenu = document.getElementById('navMenu');

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    navToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        var spans = navToggle.querySelectorAll('span');
        if (navMenu.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 6px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(5px, -6px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });

    navMenu.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            var spans = navToggle.querySelectorAll('span');
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        });
    });

    // ===== SUBJECT TOGGLE =====
    window.toggleSubject = function(subjectId) {
        var detail = document.getElementById(subjectId + '-detail');
        if (detail) {
            detail.classList.toggle('active');
        }
    };

    // ===== SCORE CALCULATOR =====
    window.hesaplaPuan = function() {
        var dogruYetenek = parseInt(document.getElementById('dogru-yetenek').value) || 0;
        var yanlisYetenek = parseInt(document.getElementById('yanlis-yetenek').value) || 0;
        var dogruKultur = parseInt(document.getElementById('dogru-kultur').value) || 0;
        var yanlisKultur = parseInt(document.getElementById('yanlis-kultur').value) || 0;

        if (dogruYetenek + yanlisYetenek > 60 || dogruKultur + yanlisKultur > 60) {
            alert('Doeru + Yanli toplami 60'tan cok olamaz!');
            return;
        }

        var netYetenek = dogruYetenek - (yanlisYetenek / 4);
        var netKultur = dogruKultur - (yanlisKultur / 4);
        var toplamNet = netYetenek + netKultur;
        var toplamPuan = Math.round(toplamNet);

        var resultScore = document.getElementById('result-score');
        var resultLabel = document.getElementById('result-label');

        resultScore.style.opacity = '0';
        resultScore.style.transform = 'scale(0.5)';

        setTimeout(function() {
            resultScore.textContent = toplamPuan.toFixed(1);
            resultScore.style.transition = 'all 0.5s ease';
            resultScore.style.opacity = '1';
            resultScore.style.transform = 'scale(1)';

            var label = '';
            if (toplamPuan >= 80) label = 'Cok Basarili! Yuksek Puan';
            else if (toplamPuan >= 60) label = 'Iyi Basari! Konusturabilir';
            else if (toplamPuan >= 40) label = 'Orta Basari. Daha Calismali!';
            else if (toplamPuan >= 20) label = 'Gelistim Asamasinda';
            else label = 'Zorlanmaya Devam Et!';

            resultLabel.textContent = label;
            
            // Show detail breakdown
            var detYetenek = document.getElementById('det-yetenek-net');
            var detKultur = document.getElementById('det-kultur-net');
            var detToplam = document.getElementById('det-toplam-net');
            var detSection = document.getElementById('calc-detail');
            if (detYetenek && detKultur && detToplam && detSection) {
                detYetenek.textContent = netYetenek.toFixed(2);
                detKultur.textContent = netKultur.toFixed(2);
                detToplam.textContent = toplamNet.toFixed(2);
                detSection.style.display = 'block';
            }
        }, 200);
    };

    // ===== INPUT VALIDATION =====
    document.querySelectorAll('#puan-hesaplama input').forEach(function(input) {
        input.addEventListener('input', function(e) {
            var value = parseInt(e.target.value);
            if (isNaN(value)) value = 0;
            if (value < 0) value = 0;
            var max = parseInt(e.target.max);
            if (value > max) {
                value = max;
                e.target.value = max;
            }
            e.target.value = value;
        });
    });

    // ===== SMOOTH SCROLL =====
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                var offsetTop = target.offsetTop - 70;
                window.scrollTo({ top: offsetTop, behavior: 'smooth' });
            }
        });
    });

    // ===== INTERSECTION OBSERVER ANIMATIONS =====
    var observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.card, .type-card, .plan-card, .resource-card').forEach(function(el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });

    // ===== CLEAR RESULT ON INPUT CHANGE =====
    document.querySelectorAll('#puan-hesaplama input').forEach(function(input) {
        input.addEventListener('change', function() {
            var rs = document.getElementById('result-score');
            var rl = document.getElementById('result-label');
            rs.textContent = '-';
            rl.textContent = 'Tahmini Puan';
            rs.style.opacity = '1';
            rs.style.transform = 'scale(1)';
        });
    });

})();
