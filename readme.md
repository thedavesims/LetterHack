#LetterHack

##A stupid simple Letterpress word finder

Prints out the 5 longest words that are possible given the letters that appear in the Letterpress grid and words that appear in the wordlist.

    $./letterhack.py YOURLISTOFLETTERS
    Top 5 Words by length: 
    storyteller
    irresolutely
    roisterously
    stertorously
    storytellers

When giving a shorter list, will also show works that use all those letters. This is useful for game enders.

    $ ./letterhack.py SHRT
    Top 5 Words by length: 
    sh
    Top 5 Words by that are supersets: 
    harts
    horst
    hurst
    hurts
    ruths
    shirt
    short
    tahrs
    trash
    airths


Finally, if you add a second param, the words that contain all those letters using the first argument as a superset are shown. This is useful for longer game-enders and to attack certain areas of the board.

    $ ./letterhack.py YOURLISTOFLETTERS YFU
    Top 5 Words by length: 
    storyteller
    irresolutely
    roisterously
    stertorously
    storytellers
    Top 5 preferred Words by length: 
    stultify
    yourself
    restfully
    tristfully
    fruitlessly


Makes use of the public domain ENABLE word list. Letterpress may use a different word list.