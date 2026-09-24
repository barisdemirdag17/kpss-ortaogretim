@echo off
cd /d "C:\Users\baris\OneDrive\Desktop\opencode otomasyon\kpss-ortaogretim-website"
"C:\Program Files\Git\bin\git.exe" add -A
"C:\Program Files\Git\bin\git.exe" commit -m "Merge: Deneme sinavini tek sayfaya birlestirdi"
"C:\Program Files\Git\bin\git.exe" push origin main
echo DONE
pause
