# PEG_DEBUG [200 pts]

**Category:** Pegasus
**Solves:** 11

## Description
>b"You manage to connect to the JTAG interface of the console! However, the\r\ndebug interface provided over JTAG is partially locked down and only\r\nprovides non-intrusive debugging capabilities. Maybe that will be enough\r\nto bypass the password protection on the device?\r\n\r\n-----\r\n\r\n### Note:\r\n\r\nThere are intentionally no files delivered as part of this challenge. You\r\nneed to use the interactive debugger to solve it.\r\n\r\nYou can connect to this challenge over SSH for an enhanced interactive\r\ndebugging experience with tab-completion, arrow keys, suggestions, etc.\r\nThe debugger is also available over a standard TCP socket, which may be\r\neasier to use from a script. After connecting to the debugger (either SSH\r\nor plain TCP), you then connect to another port from a second terminal to\r\naccess the programs I/O. That is, youll have one terminal window connected\r\nto the debugger, and another connected to the programs stdin/stdout.\r\n\r\n### 1A. Connect to debugger (enhanced SSH version)\r\n\r\n```\r\nssh -o StrictHostKeyChecking=no -p 22702 peg-debug@sunshinectf.games\r\n```\r\n\r\n### 1B. Connect to debugger (plain TCP version)\r\n\r\n```\r\nnc sunshinectf.games 22701\r\n```\r\n\r\n### 2. Connect to program I/O (in another terminal)\r\n\r\n```\r\nnc sunshinectf.games 22700\r\n```\r\n\r\nThen, paste the PEGASUS debug session ID that the debugger connection printed.\r\n\r\nAuthor: kcolley"

**Hint**
* -

## Solution

### Flag

