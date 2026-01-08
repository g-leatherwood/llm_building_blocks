import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import llm
    from dotenv import load_dotenv

    load_dotenv(".env")
    return (llm,)


@app.cell
def _(llm):
    llm.get_models()
    return


@app.cell
def _(llm):
    claude_model = llm.get_model("anthropic/claude-3-5-haiku-latest")

    claude_resp = claude_model.prompt("Write me a haiku about running")
    return claude_model, claude_resp


@app.cell
def _(claude_resp):
    claude_resp.json()
    return


@app.cell
def _(llm):
    gpt_model = llm.get_model("gpt-4o-mini")

    gpt_resp = gpt_model.prompt("Write me a haiku about running")
    return gpt_model, gpt_resp


@app.cell
def _(gpt_resp):
    gpt_resp.json()
    return


@app.cell
def _(gpt_model):
    from pydantic import BaseModel

    class Haiku(BaseModel):
        poem: str

    class Haikus(BaseModel):
        topic: str
        haikus: list[Haiku]

    out = gpt_model.prompt("Haiku about Running", schema=Haikus)
    return BaseModel, Haikus, out


@app.cell
def _(out):
    import json

    json.loads(out.json()["content"])
    return (json,)


@app.cell
def _(Haikus, claude_model):
    claude_out = claude_model.prompt("Haiku about Running", schema=Haikus)

    return (claude_out,)


@app.cell
def _(claude_out):
    claude_out.json()["content"][0]["input"]["haikus"]
    return


@app.cell
def _(gpt_model):
    convo = gpt_model.conversation()

    _ = convo.prompt("Give me a haiku about running")
    print(_.text())
    print("\n")
    _ = convo.prompt("Give me another one about trailrunning")
    print(_.text())
    return


@app.cell
def _(claude_model, mo):
    conversation = claude_model.conversation()
    chat_widget = mo.ui.chat(lambda messages: conversation.prompt(messages[-1].content))
    chat_widget
    return


@app.cell
def _(BaseModel, gpt_model, json, mo):
    class Summary(BaseModel):
        title: str
        summary: str
        pros: list[str]
        cons: list[str]

    def summary(text_in):
        resp = gpt_model.prompt(
            f"Make a summary of the following text: {text_in}",
        schema=Summary)
        return json.loads(resp.json()["content"])

    text_widget = mo.ui.text_area(
        label="Input to summary function"
    ).form()

    text_widget
    return summary, text_widget


@app.cell
def _(summary, text_widget):
    from pprint import pprint

    pprint(summary(text_widget.value))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
