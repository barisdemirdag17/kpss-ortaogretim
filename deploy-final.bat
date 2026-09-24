@echo off
cd /d "C:\Users\baris\OneDrive\Desktop\opencode otomasyon\kpss-ortaogretim-website"
"C:\Program Files\Git\bin\git.exe" add -A
"C:\Program Files\Git\bin\git.exe" commit -m "Update: Real KPSS seviyesi sorular, duzgun puan hesaplama, tek sayfa"
"C:\Program Files\Git\bin\git.exe" push origin main
echo DONE
pause