# PredictorProgrammer 1 [50 pts]

**Category:** Scripting
**Solves:** 76

## Description
># PredictorProgrammer\r\n## Take that, friends and siblings!\r\n\r\nHave you ever played "Guess the Number?"\r\n\r\nYou know, "I\m thinking of a number from 1 to X, where X is a non-real number with some imaginary parts and could be transcendental but not e or pi?"\r\n\r\nNo? Gee I must have weird friends.\r\n\r\nWhat about "I\m thinking of a number from 1 to 10?"\r\n\r\nOh? You have?\r\n\r\nWell have I got a challenge for you!\r\n\r\nLast year, I procrastinated my security system, and took security in the challenge to the cliff of failure.\r\n\r\nHeh heh, turns out eval wasn\t safe to use... ever.\r\n\r\nThis year we take one step further! *_Minus the whole "user sends executable code to us that we then use python to execute," and all. That was a **minor** mistake._\r\n\r\nVisit `nc predictor.sunshinectf.games 22201`, and play a game of predicting the future!\r\n\r\nBut don\t worry that this game will get old! The flags in this game are split into three kingdoms, with one flag in each... you\ll never find them all! And since it\s random, no two games will ever be alike!\r\n\r\nFlag will be given by our backend in the standard `sun{}` format!\r\n\r\n## Notes\r\n\r\nI am not unreasonable.\r\n\r\nAll I ask is you predict the future with 100% accuracy.\r\n\r\nThat\s hard, that\s why I give you a couple chances to get it wrong.\r\n\r\nOnce you get a few numbers I feel you\ll get the hang of it.\r\n\r\nJust don\t use the previous numbers to predict the state of the RNG, that would totally not be predicting the future, as the state is set from the start, so you\d be predicting the past! And it would _ruin_ the whole concept of this challenge and make it an exercise in math and googling how to break linear congruential generators! That\s super boring, this is _strictly_ about predicting the future, which is fun!\r\n\r\n## Example Usages\r\n\r\n"Hi, I\m thinking of a number from 1 to 31"\r\n```python\r\n7\r\n```\r\nWrong. I was thinking of 17. You must not be from Florida!\r\n\r\n...\r\n\r\n\r\n8\r\nCorrect! You\ve guessed 3 numbers correctly, and have 1 life left! Only 16 more correct answers left to guess!\r\n\r\nNote: In the future we may change the support structure if we find there\s security issues with them.

**Hint**
* -

## Solution

### Flag

