# farmbot9000

this is a program that automatically sends preconfigured messages into a discord channel.  
please notice this was only tested with windows 10 using chromedriver 110.0.5481.77

## installation

- install the requirements from `requirements.txt`
- create a `driver` folder and place a [chromedriver executable](https://chromedriver.chromium.org/) into it

## usage

1. open the `messages.txt` file and set up your messages
2. make changes to `config.ini` if needed
3. run `main.py`
4. a window for logging into discord will pop up
5. login and select the server and channel
6. click the box where you type messages
7. go back to the python console and press enter

## config.ini parameters

### timer

- **timerSeconds**: time in seconds between messages
- **useRandomTime**: if `True`, `randomTimeMargin` will be used
- **randomTimeMargin**: seconds to be added or subtracted from `timerSeconds`

### messages

- **filePath**: file where messages are stored
- **useRandomMessage**: if `True` the message to be sent will be randomly selected. if `False`, the messages will be sent in order
- **updateMessagesOnCycle**: the message list will be updated after a message is sent
- **clearInput**: the message box will be cleared before typing another message
- **useMessagePasting**: messages will be copied to clipboard and pasted instead of typed
- **useEmptyChars**: empty characters will be randomly pasted into the message so they won't appear in the search bar

### browser

- **disableSeleniumLogs**: prevent selenium logs from polluting the console
- **saveSession**: save cookies so there's no need to login every time

### config

- **updateConfigOnCycle**: update this file after a message is sent
