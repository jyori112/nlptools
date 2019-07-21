from distutils.core import setup

setup(
    name="nlptools",
    version="0.1dev",
    packages=["nlptools"],
    author="Jin SAKUMA",
    entry_points={
        "console_scripts": [
            "nlptools=nlptools.cli:cli",
            "emb=nlptools.embeddings:cli"
        ]
    },
    install_requires=[
        'click'
    ]
)


