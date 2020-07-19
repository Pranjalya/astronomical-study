## Interview with Emily Petroff

_Doctor of Astrophysics, ASTRON, Netherlands_

#### Research

* So, I mainly work in pulsars and also on these new types of objects that we call fast radio bursts. So pulsars, if you're familiar with them, are these rapidly rotating neutron stars. They're very dense leftovers from a supernova explosion. They're much denser than normal matter. They spin extremely quickly. And they have these jets that come out of the poles. And so, they spin around like the lighthouse. And with a radio telescope, you can actually see that jet as it spins around, kind of gives off a sort of a blip every time It passes our line of sight, it looks like a lighthouse. 

* But we also use those radio telescopes to find these very bright radio flashes called fast radio bursts. We don't know exactly where they're coming from. They look a lot like the pulses that we see from pulsars, but we only see them very rarely or maybe only once ever.

* And they seem to be coming from very far outside our galaxy. So, maybe enormous explosions or super energetic progenitors somewhere else far away in the universe. 

#### Biggest Data Challenge

* I think the first challenge is just the processing. Because we want to find these things as quickly as  possible. So we not only want to process quickly, but we want to process quickly enough that we can find them in real time. And we're actually able to do that now, which was an enormous challenge to overcome. But essentially it kind of came down to how we parse the data, processing it at the telescope in small chunks rather than processing one big file afterwards. 

* The way that we have tried to edge ahead of the telescope is, essentially, taking advantage of graphics processing units. So, instead of doing our processing on a CPU where you can only work in one stream, or you can only work in series, we have started taking advantage of the GPUs, where you can actually parallelize your processing fairly efficiently. Especially if you have a repetitive task, like doing this frequency permutation. And in that case, we can sort of speed up by parallelizing over multiple GPU threads and then achieve near real-time processing speed. __So we're actually able now to process the data in about 16 second chunks as it comes off the telescope and immediately get information on whether we found a burst or not__. 

#### Data tools recommendations

* Taking advantage of visualization.

*  Code can find it for you, but if you're ever in doubt, plotting that up, or plotting it up against some interference or something like that, you can immediately see the difference between those two pictures. And actually really helps you understand what's in your data, rather than just having a code tell you what's in your data. 

#### What do you like most about this research?

* I think the thing that I like most about my research is that I get to, just in research in general, I get to ask my own questions and answer them. The data comes in to that in a huge way, which is, you can ask these questions until you're blue in the face in terms of like, I wonder what this looks like, or will I ever find this thing. You'll never actually get the answers until you start looking through the data. 

* But at the same time, you look through all those plots and you find that one really exciting thing, and it answers your questions or kind of leads you down this path of more questions. And I think that's the really exciting thing, is you kind of, even if you didn't find what you were expecting to find, you have this wealth of data to look through. And you can learn things that maybe you didn't even expect. And that's exactly where these fast radio bursts came from. And that's where the majority of the work from them has originated, is people looking through their data in any way, and saying, wow. I mean, we were looking for pulsars, but we found this really interesting other thing as well. 
