# LyricSynthesis
Creating lyrics through machine learning. The eventual goal is to go from lyric
generation all through speech. An added bonus would be to have instruments created
as well.


# Todo

| Task       | Status           |
| ------------- |:-------------:|
| Rip Lyrics    | completed |
| Lyric Synthesis | working |
| Find Audio Sources | in progress |
| Format Audio Sources | not started |
| Train Audio Model | not started |



# Requirements
### Anaconda
It helps to keep everything tidy through virtual environments.

```conda create --name LyricSynth tensorflow-gpu==1.15.2```
 or
```conda create --name LyricSynth tensorflow==1.15.2```
 depending if you want to run this on your CPU or GPU

 To enter the virtual environment:
  conda activate LyricSynth
 And then to exit:
  conda deactivate

# Credits
Special thanks to [OpenAI](https://openai.com/) for creating
[GPT-2](https://github.com/openai/gpt-2), and to Max Woolf
([@minimaxir](https://minimaxir.com/)) for creating the wrapper I used for GPT-2.
