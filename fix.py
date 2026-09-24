import os, re

site_dir = r'C:\Users\baris\OneDrive\Desktop\opencode otomasyon\kpss-ortaogretim-website'

with open(os.path.join(site_dir, 'index.html'), 'r', encoding='utf-8') as f:
    content = f.read()

# Quiz HTML sections
quiz_html = '''
    <!-- Deneme Sýnavý -->
    <section class="section" id="deneme-sinavi">
        <div class="container">
            <div class="quiz-container">
                <!-- Start Screen -->
                <div id="startScreen">
                    <div class="start-screen">
                        <h2>📝 KPSS Ortaöðretim Deneme Sýnavý</h2>
                        <p>Konu daðýlýmýna uygun olarak hazýrlanmýþ 20 soruluk deneme sýnavý. Zamaný dolduðunda veya bitirdiðinizde sonuçlarý göreceksiniz.</p>
                        <div class="start-info">
                            <div class="start-info-item">
                                <div class="info-icon">⏱️</div>
                                <h4>20 Soru</h4>
                                <p>Her konu alt bölümden sorular</p>
                            </div>
                            <div class="start-info-item">
                                <div class="info-icon">📋</div>
                                <h4>5 Konu</h4>
                                <p>Türkçe, Matematik, Tarih, Coğrafya, Vatandaþlýk</p>
                            </div>
                            <div class="start-info-item">
                                <div class="info-icon">📊</div>
                                <h4>Otomatik Deðerlendirme</h4>
                                <p>Doðru, yanlýþ, boş, net ve puan</p>
                            </div>
                            <div class="start-info-item">
                                <div class="info-icon">🎯</div>
                                <h4>KPSS Uyumu</h4>
                                <p>Ortaöðretim seviyesi sorular</p>
                            </div>
                        </div>
                        <button class="btn btn-primary" onclick="startQuiz()" style="font-size: 1.1rem; padding: 16px 48px;">📝 Deneme Sýnavýný Baþlat</button>
                    </div>
                </div>

                <!-- Quiz Screen -->
                <div id="quizScreen" style="display:none;">
                    <div class="quiz-header">
                        <h2>📝 Deneme Sýnavý</h2>
                    </div>
                    <div class="quiz-progress">
                        <div class="quiz-progress-item">
                            <div class="label">Soru</div>
                            <div class="value" id="progressCurrent">1</div>
                        </div>
                        <div class="quiz-progress-item">
                            <div class="label">Doðru</div>
                            <div class="value correct" id="progressCorrect">0</div>
                        </div>
                        <div class="quiz-progress-item">
                            <div class="label">Yanlýþ</div>
                            <div class="value wrong" id="progressWrong">0</div>
                        </div>
                        <div class="quiz-progress-item">
                            <div class="label">Boþ</div>
                            <div class="value blank" id="progressBlank">0</div>
                        </div>
                        <div class="quiz-progress-item">
                            <div class="label">Kalan</div>
                            <div class="value" id="progressRemaining">19</div>
                        </div>
                    </div>
                    <div id="questionArea"></div>
                    <div class="navigation-buttons">
                        <button class="btn btn-secondary" id="prevBtn" onclick="prevQuestion()" disabled>← Önceki</button>
                        <button class="btn btn-primary" id="nextBtn" onclick="nextQuestion()">Sonraki →</button>
                    </div>
                </div>

                <!-- Result Section -->
                <div class="result-section" id="resultSection">
                    <h2 class="result-title">📊 Sýnav Sonuçlarý</h2>
                    <div class="result-stats">
                        <div class="result-stat correct">
                            <div class="stat-label">✅ Doðru</div>
                            <div class="stat-value" id="resCorrect">0</div>
                        </div>
                        <div class="result-stat wrong">
                            <div class="stat-label">❌ Yanlýþ</div>
                            <div class="stat-value" id="resWrong">0</div>
                        </div>
                        <div class="result-stat blank">
                            <div class="stat-label">⬜ Boþ</div>
                            <div class="stat-value" id="resBlank">0</div>
                        </div>
                        <div class="result-stat net">
                            <div class="stat-label">📐 Net</div>
                            <div class="stat-value" id="resNet">0</div>
                        </div>
                        <div class="result-stat points">
                            <div class="stat-label">⭐ Puan</div>
                            <div class="stat-value" id="resPoints">0</div>
                        </div>
                        <div class="result-stat">
                            <div class="stat-label">📋 Genel Kültük Net</div>
                            <div class="stat-value" id="resGenelKultuk">0</div>
                        </div>
                    </div>
                    <div class="result-message" id="resMessage"></div>
                    <div class="result-breakdown">
                        <h4>📈 Konu Bazlý Detay</h4>
                        <div id="breakdownArea"></div>
                    </div>
                    <div style="margin-top: 24px; display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                        <button class="btn btn-primary" onclick="retryQuiz()">🔄 Tekrar Dene</button>
                        <a href="index.html" class="btn btn-secondary">📚 Ana Sayfaya</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

# Insert quiz HTML before </body> but after </script>
if '<!-- Deneme Sýnavý -->' not in content:
    content = content.replace('</script>\n\n</body>', '</script>\n' + quiz_html + '\n</body>')
    print('Quiz HTML inserted')
else:
    print('Quiz HTML already exists')

with open(os.path.join(site_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Final length: {len(content)} chars')
print('DONE')
