from distutils.core import setup

setup(
    name="nlptools",
    version="0.1dev",
    packages=["nlptools"],
    author="Jin SAKUMA",
    entry_points={
        "console_scripts": [
            "nlptools=nlptools.cli:cli",
            "emb=nlptools.embeddings:cli",
            "sshuf=nlptools.sshuf:cli",
            "utils=nlptools.utils:cli"
        ]
    },
    install_requires=[
        'click',
        'numpy'
    ]
)


