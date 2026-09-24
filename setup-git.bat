@echo off
cd /d "C:\Users\baris\OneDrive\Desktop\opencode otomasyon\kpss-ortaogretim-website"
"C:\Program Files\Git\bin\git.exe" init
"C:\Program Files\Git\bin\git.exe" config user.email "deploy@kpss-ortaogretim.com"
"C:\Program Files\Git\bin\git.exe" config user.name "KPSS Rehber"
"C:\Program Files\Git\bin\git.exe" add -A
"C:\Program Files\Git\bin\git.exe" commit -m "Initial commit: KPSS Ortaogretim Website"
echo DONE - Repository ready!
pause
