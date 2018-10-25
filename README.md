# plainclothes

*An algorithm for encrypting arbitrary data as innocuous English text.*

Plainclothes is a project I started as a way to practice my language modeling skills. 
It builds up a lossless text compression algorithm in steps, downloading English training
data from Wikipedia and the Gutenberg corpus, training a Kneser-Ney smoothed ngram language 
model on that data, then builds a lossless Huffman encoding compression scheme using the
language model. 

It can, of course, be used to compress text files, but I prefer the much more fun and much 
less useful application of "decompressing" files that were never compressed. You can give 
Plainclothes any data and it will "decompress" it, turning it into a text file that looks 
as much as possible like regular, innocuous English. Conceivably, this could be used to 
disguise sensitive information, even encrypt it (since the training corpus is generated
on the fly, you could conceivably keep your training corpus secret, at which point the 
cryptographic security of the decompression becomes an interesting problem). Realistically,
it will be used to create goofy, semantically nonsensical text and build my skills as
an NLP developer.

## Interacting with the CLI:

usage: `python cli.py <command> [<args>]`

`cli.py download [ gutenberg | wikipedia ]`
- Downloads pages off the internet and stores them as plain ASCII text in `sources/`.
- Specify one or more sources as arguments
- If no arguments are passed, downloads from all sources

`cli.py collect`
- Collects all sources into `sources/corpus.txt`

`cli.py ngrams [ n ]`
- Computes character ngrams of length up to n.
