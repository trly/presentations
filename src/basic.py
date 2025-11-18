import os
from anthropic import Anthropic


def get_user_message():
    try:
        return input(), True
    except EOFError:
        return "", False


class Agent:
    def __init__(self, client: Anthropic, get_user_message_fn):
        self.client = client
        self.get_user_message = get_user_message_fn

    def run(self):
        conversation = []

        print("Chat with Claude (use 'ctrl-c' or 'ctrl-d' to quit)")

        while True:
            print("\033[94mYou\033[0m: ", end="")
            user_input, ok = self.get_user_message()
            if not ok:
                break

            conversation.append({"role": "user", "content": user_input})

            message = self.run_inference(conversation)
            conversation.append(
                {"role": "assistant", "content": message.content})

            for content in message.content:
                if content.type == "text":
                    print(f"\033[93mClaude\033[0m: {content.text}")

    def run_inference(self, conversation):
        message = self.client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            messages=conversation,
        )
        return message


def main():
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    agent = Agent(client, get_user_message)

    agent.run()


if __name__ == "__main__":
    main()
