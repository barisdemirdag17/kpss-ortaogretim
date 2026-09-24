@echo off
cd /d "C:\Users\baris\OneDrive\Desktop\opencode otomasyon\kpss-ortaogretim-website"
"C:\Program Files\Git\bin\git.exe" rm combine-deploy.bat combine.py force-push.bat 2>nul
"C:\Program Files\Git\bin\git.exe" add -A
"C:\Program Files\Git\bin\git.exe" commit -m "Clean up temporary files"
"C:\Program Files\Git\bin\git.exe" push origin main
echo DONE
