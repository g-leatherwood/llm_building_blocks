import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    slider = mo.ui.slider(1, 100, 1, label="a =")
    slider
    return (slider,)


@app.cell
def _(slider):
    a = slider.value
    return (a,)


@app.cell
def _():
    b = 2
    return (b,)


@app.cell
def _(a, b):
    a + b
    return


if __name__ == "__main__":
    app.run()
