## A conversation with Jon Jenkins

_Working at NASA Ames Research Center for the last 20 plus years on finding extra solar planets orbiting other stars_

* It was almost a fairy tale at the time, people didn't believe that CCD sensors had the precision or that the stars would cooperate and be quiet enough so that you could find these very small signatures when planets cross the phase of their star from our point of view.

* __STEPS__ : 
    1. We begin with the data at the image level where we have postage stamps or images of the target stars that we're observing up to 170 000 at a time with Kepler that are observed and we collect data for each half hour. 

        And we store that data on board then we transmit it to the ground once per month.

        But you have to correct and calibrate the image data to remove on-ship artifacts like you have to flat field, you have to remove the sky background, those sorts of  things. 
    
        And then you sum up the pixels underneath the image of each star as a first estimate of the brightness of the star. 

    2. The second thing that we do which is even more challenging is identifying movement instrumental signatures. 

        And the promise that when you're looking for planets like Earth, they're really small compared to the stars like the Sun. A Jupiter crossing a Sun size star will cause a 1% drop up in the brightness that's because the Sun is about ten times bigger than Jupiter. While Earth is ten times smaller than Jupiter, and so that means that you're talking about a percent of a percent. 

        And that's why it's so hard to find Earth's around other stars even though this method has been quite successful at doing that. So it turns out that the instrumental signatures, the change in the focus of the instrument, other changes that are going on inside the instrument as we're on our orbit around the Sun with Kepler. Plus what stars are doing themselves, they have star spots like the Sun does.

        And those star spots can be present a larger signature in terms of the change of the brightness of the star every time then the transits themselves. 

    3. This third and critical step is to identify and remove those instrumental signatures so that you can actually then do the job of detecting these weak signatures of transing planets.

        May last anywhere from about an hour to half a day, and that's what really saves us in that star spots are relatively gradual, they take place over timescales of weeks, whereas the transits themselves are very short blips. 

        And so that allows us to separate most of the noise out in frequency space.

* Over time, it's been amazing how much the sensitivity has improved for the ground bass systems. For example, there's so much to factor five and prove one in the sensitivity of the radio blasty searches each in every year. So that's means that while they we're pretty much limited to find in 2 meters size objects at the beginning now we're finding examples of Earth mass objects like approximately that was just announced just a month or so ago. So that's phenomenal that we only have to knock on the door of our next door neighbor to find the closest Earth mass planet. It's just mind boggling. The question that Kepler was posed to answer was how common are Earth size planets and inhabitable of something like stars and Kepler went a long way to answering that question.

* And so one of the big surprises though, was that we find, with Kepler data, that every main sequence star has on average at least one planet. So that means that if you look up into the night sky, that just about every star you see has at least one planet, so planets are ubiquitous. 

##### Challenges

* One of the challenges for Kepler was keeping up with the data. And that is with our own local cluster that we built up, our little mini-supercomputer that we had, 700 computer cores in the end. And we were able to keep up with the data, but what we couldn't do was we could not go back routinely to reprocess the data from start to finish with the improved algorithm, because we learn more about the instrument, as we learn more about the sky. 

* And so about 3.5 years into the mission then we started porting all of our code over to run on the NASA Pleiades supercomputer at the NASA Advanced Supercomputing facility here at Ames. And that allows us to process all 17 quarterly segments of data, simultaneously. And we can reprocess all four years of data then, in a couple of months. Rather than taking two or years, which is what it would have taken our own, much smaller cluster of computers.

* One of the technologies that's developed over the last several years, I think is very exciting, has a lot of promise, is *compressive sensing*. 

    That allows us to compress the data using very simple algorithms and get very high compression rates. And the cost is that we have to have much more sophisticated decompression algorithms to reconstruct the data.

    And I think that's a very exciting field, and so I would strongly encourage people to look at compressive sensing as a way to go to help us deal with this headlong torrent of data that's headed our way that's going to crush us beneath it.

##### Thoughts

For example, I designed the compression algorithms that we use on board the spacecraft to compress the data. And we routinely achieve a compression rate of somewhere around 4.5 to 5 bits per pixel measurement and we start out at 23.

So that's a really good compression factor there. On the other hand just about everything else that went on with the pipeline ended up having monkey wrenches thrown at it either by the instrument or by the sky. So to be honest, we had to rewrite about 80% of the science algorithm or at least modify them significantly to be able to handle things that were happening with the instrument or with the sky that we just simply could not anticipate. 

That's the great joy of doing something like this, you're doing something for the first time. It's like you've got a brand new instrument. It's like you've been on a canoe, looking down in the water and all the bright fishes that are swimming on the reef. And suddenly you dive in with a pair of goggles and a scuba gear, and you're able to get up close to all of these animals and see every single spot and stripe. Well, you end up seeing all the flaws in your instrument as well. But that's part of the joy of being in a field like this that it's a great set of challenges technically to design and build these things. And then once you get there then you have a lot of work to do to actually do what you set out to do in the first place, because you simply cannot predict how it's going to turn out. 

And that's fun, it's fun to have meeting, choosing problems to solve. It's a great joy when you're facing a very challenging technical problem. To recognize that it's similar to a problem that you'd encountered in a different context. And that oftentimes, problems are solved by perspective. That they seem hard from one perspective and difficult and maybe impossible. But oftentimes, you can transform them, or turn the puzzle slightly, and identify a way to solve that problem, because it's similar to another problem that you solve. 

That's also a great joy to work with other people that can have their own ideas, bring their own ideas to the table. And that sharpens your skills and makes you more capable of solving different kinds of problems in the future. So I'd say if this were easy to do I don't think that people like me would be doing it. 
