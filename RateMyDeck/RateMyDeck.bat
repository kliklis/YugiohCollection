echo off
REM QUICK ARGUMENT EXPLANATION:
REM     main_path :               Source/main.py
REM     log_intensity(0 to 3):    3
REM     export(1(on)/0(off)):     1
REM     deck_path :               Resources/Decks/Deck.txt
REM     combo_path :              Resources/Combos/Combos.txt
REM     YOU CAN CHANGE THE ARGUMENT BELOW

python Source/main.py 2 1 Resources/Decks/Deck.txt Resources/Combos/Combos.txt
pause