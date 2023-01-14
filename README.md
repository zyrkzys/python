# python
various python projects

## Dangerous Pickles
This notebook has examples of how the ```pickle``` module can be used to produce an output, a serialized text file, which loads malicious code upon its deserialization. I also included an example of the ```fickling``` package, which allows for easy insertion of lines of executable code into the body of existing pickles. Lastly, I close with an example of creating and loading a pickle that runs system commands (in bash) to create a bash shell, redirect the output to a FIFO in /tmp, and connect it the a ```nc``` listener. Do not misuse!

## ```asyncio``` 
These are examples of Python's ```asyncio``` module, including two scripts. The notebook works, but it's better to segment out the asyncio code into scripts so it will run without the weird context of the Jupyter iPython interpreter, which causes some issues with the event loops ```asyncio``` spawns.
