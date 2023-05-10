# Audio Interactive Chatbot

This is an AI-powered chatbot that can interact with users via text-based input or audio input. The chatbot uses OpenAI's GPT-3.5-turbo model to generate responses to users' inputs.
Audio based communication can only happen in english as things stand now.

## Getting started
### Prerequisites

To run this chatbot you will need:

* Python 3.x installed on your system
* An OpenAI API key

#### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/MarcoLorenzoCampo/audio_interactive_chatbot
```

2. Install the required Python packages using the following command:
```bash
pip install -r requirements.txt
```

#### Usage

1. Set your OpenAI API key as an environment variable using the following command:

##### On Windows

```bash
setx OPENAI_API_KEY "your_key_value"
```
##### On Unix Systems

```bash
export OPENAI_API_KEY = "your_key_value"
```

 2. Run the chatbot_logic.py script with the necessary parameters:

 ```bash
python gui.py [--speak] [--talk]
```

* The --speak flag will produce a text-to-speech playback of the AI's responses to your inputs.
* The --talk flag will give you a time window to produce a question via speech input.

Flags are not mandatory since their value can be updated in gui as well.
