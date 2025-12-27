import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


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
    model = llm.get_model("anthropic/claude-3-5-haiku-latest")

    resp = model.prompt("Write me a haiku about running")
    return (resp,)


@app.cell
def _(resp):
    resp.json()
    return


if __name__ == "__main__":
    app.run()
